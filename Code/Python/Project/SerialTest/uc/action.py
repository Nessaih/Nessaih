# coding: utf-8
import sys
import datetime
import PyQt5.QtGui as QG
import PyQt5.QtCore as QC
import PyQt5.QtWidgets as QW

sys.path.append('SerialTest\\ui')
sys.path.append('SerialTest\\ut')

import ui.MainWindow
import ut.uart
import ui.theme.qss

display_setting = {'newline': False, 'trx': False, 'time': False, 'date': False, 'hex': False}
send_block_index = 0
send_block_setting = {'period': 0, 'period_enable': False, 'newline': False, 'hex': False}

is_port_close = True


def CommandsHideShow():
    state = self.win.cmdsGroupBox.isVisible()
    self.win.cmdsGroupBox.setVisible(not state)


class Action:

    def __init__(self, __win: ui.MainWindow.MainWindow, __uart: ut.uart.Uart):
        self.win = __win
        self.uart = __uart
        # print(self.win is self.win)
        self.Connect()

    def Connect(self):
        self.uart.receiver.received.connect(self.ReceiveCallback)                               # 接收回调
        self.win.portComboBox.clicked.connect(lambda: self.RefreshPortCallback())               # 端口刷新
        self.win.onoffButton.clicked.connect(self.OnOffPortCallback)                            # 端口开关
        self.win.clearButton.clicked.connect(self.ClearReceiveScreenCallback)                   # 接收清屏
        self.win.newlinedisplayCheckBox.stateChanged.connect(self.ShowNewlineCallback)          # 接收换行
        self.win.timedisplayCheckBox.stateChanged.connect(self.ShowTimeCallback)                # 接收时间显示
        self.win.datedisplayCheckBox.stateChanged.connect(self.ShowDateCallback)                # 接收日期显示
        self.win.sendTableWidget.currentChanged.connect(self.SwitchSendBlock)                   # 发送区切换
        self.win.hexdisplayComboBox.currentIndexChanged['int'].connect(self.ShowHexCallback)    # HEX、ASCII显示切换
        self.win.showCmdsAction.triggered.connect(self.CommandsHideShow)                        # 发送命令区隐藏、显示
        self.win.periodSendCheckBox.stateChanged.connect(self.PeriodSendCallback)               # 定时发送
        self.win.newlineSendCheckBox.stateChanged.connect(self.NewlineSendCallback)             # 发送新行
        self.win.hexSendComboBox.currentIndexChanged['int'].connect(self.HexSendCallback)       # HEX、ASCII发送切换
        self.win.sendButton.clicked.connect(self.SendClickedCallback)                           # 发送按钮
        self.win.cmdsButtonGroup.buttonClicked[int].connect(self.CmdsClicked)                   # 发送命令

    def CommandsHideShow(self):
        state = self.win.cmdsGroupBox.isVisible()
        self.win.cmdsGroupBox.setVisible(not state)

    def RefreshPortCallback(self):
        __ports = self.uart.GetPorts()
        self.win.portComboBox.clear()
        if 0 < len(__ports):
            for p in __ports:
                self.win.portComboBox.addItem(p['port'])
        else:
            self.win.portComboBox.addItem('')

    def OnOffPortCallback(self):
        global is_port_close
        __port = str(self.win.portComboBox.currentText())

        if self.win.onoffButton.isChecked():
            if self.uart.ClosePort(__port):
                self.win.onoffButton.setText(QC.QCoreApplication.translate("MainWindow", "打开串口"))
                self.win.portComboBox.setEnabled(True)
                self.win.rateComboBox.setEnabled(True)
                self.win.databitsComboBox.setEnabled(True)
                self.win.parityComboBox.setEnabled(True)
                self.win.stopbitComboBox.setEnabled(True)
                is_port_close = True
            else:
                QW.QMessageBox.critical(self.win.central, "Port Error", "此串口不能被关闭！")
        else:
            parity_list = ['N', 'O', 'E']
            __rate = int(self.win.rateComboBox.currentText())
            __databits = int(self.win.databitsComboBox.currentText())
            __parity = parity_list[self.win.parityComboBox.currentIndex()]
            __stopbit = int(self.win.stopbitComboBox.currentText())
            if self.uart.OpenPort(__port, __rate, __databits, __parity, __stopbit):
                self.win.onoffButton.setText(QC.QCoreApplication.translate("MainWindow", "关闭串口"))
                self.win.portComboBox.setEnabled(False)
                self.win.rateComboBox.setEnabled(False)
                self.win.databitsComboBox.setEnabled(False)
                self.win.parityComboBox.setEnabled(False)
                self.win.stopbitComboBox.setEnabled(False)
                is_port_close = False
            else:
                QW.QMessageBox.critical(self.win.central, "Port Error", "此串口不能被打开！")

    def ClearReceiveScreenCallback(self):
        self.win.receiveTextBrowser.clear()

    def ShowNewlineCallback(self):
        if self.win.newlinedisplayCheckBox.isChecked():
            display_setting['newline'] = True
        else:
            display_setting['newline'] = False

    def ShowTrxCallback(self):
        pass

    def ShowTimeCallback(self):
        if self.win.timedisplayCheckBox.isChecked():
            display_setting['time'] = True
        else:
            display_setting['time'] = False

    def ShowDateCallback(self):
        if self.win.datedisplayCheckBox.isChecked():
            display_setting['date'] = True
        else:
            display_setting['date'] = False

    def ShowHexCallback(self, index: int):
        if 0 == index:
            display_setting['hex'] = False
        else:
            display_setting['hex'] = True

    def PeriodSendCallback(self):
        text = self.win.periodLineEdit.text()
        if text.strip():
            period = int(text)
        else:
            period = 0
        send_block_setting['period'] = period
        if self.win.periodSendCheckBox.isChecked():
            send_block_setting['period_enable'] = True
        else:
            send_block_setting['period_enable'] = False

    def NewlineSendCallback(self):
        if self.win.newlineSendCheckBox.isChecked():
            send_block_setting['newline'] = True
        else:
            send_block_setting['newline'] = False

    def HexSendCallback(self, index: int):
        if 0 == index:
            send_block_setting['hex'] = False
        else:
            send_block_setting['hex'] = True

    def SwitchSendBlock(self):
        global send_block_index
        send_block_index = self.win.sendTableWidget.currentIndex()
        print(send_block_index)

    def ReceiveCallback(self, data: dict):

        def __show_datetime():
            t = datetime.datetime.now().strftime('%Y-%m-%d ,%H:%M:%S ').split(',')
            text = ''
            if display_setting['date']:
                text += t[0]
            if display_setting['time']:
                text += t[1]
            self.win.receiveTextBrowser.insertPlainText(text)
            # self.win.receiveTextBrowser.insertHtml('<font color=red>' + text + '</font>')

        def __show_trx():
            if display_setting['trx']:
                self.win.receiveTextBrowser.insertPlainText('RX')

        def __show_data(buf):
            end = ''
            if display_setting['newline']:
                end = '\n'

            if display_setting['hex']:
                out_arry = ['{:02X} '.format(buf[i]) for i in range(len(buf))]
                text = ''.join(out_arry) + end
                self.win.receiveTextBrowser.insertPlainText(text)
                self.win.receiveTextBrowser.moveCursor(QG.QTextCursor.End)
            else:
                text = buf.decode('utf-8', 'ignore') + end
                self.win.receiveTextBrowser.insertPlainText(text)
                self.win.receiveTextBrowser.moveCursor(QG.QTextCursor.End)

        def __show_ascii(buf):
            pass

        if data['valid']:
            buf = data['data']
            __show_datetime()
            __show_trx()
            __show_data(buf)

    def SendClickedCallback(self):
        global is_port_close
        if is_port_close:
            QW.QMessageBox.critical(self.win.widget, "Send Error", "串口未打开！")
        else:
            global send_block_setting,send_block_index
            text = self.win.sendTextEdit[send_block_index].toPlainText()
            if send_block_setting['newline']:
                text += '\r\n'
            self.uart.SendBytes(bytes(text, encoding='utf8'))

    def CmdsClicked(self,index):
        print('clicked ', index)



if __name__ == '__main__':
    print('test')