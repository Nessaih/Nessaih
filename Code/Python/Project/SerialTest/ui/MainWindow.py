import PyQt5.QtGui as QG
import PyQt5.QtCore as QC
import PyQt5.QtWidgets as QW

import ctypes

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

import sys, os

sys.path.append(os.path.abspath(os.path.join(__file__, '../..')))
import ui.res.res
import ui.TitleBar
import ui.theme.qss
import widget.combo

WINDOW_DEFAULT_WIDTH = 640
WINDOW_DEFAULT_HEIGHT = 480
WINDOW_SET_LAY_HEIGHT = 168
WINDOW_DISPLAY_SET_WIDTH = 130



def GetRootPath():
    if hasattr(sys, '_MEIPASS'):
        root = sys._MEIPASS
    else:
        root = os.path.dirname(__file__)
    return root


def GetResourcePath():
    resource = GetRootPath() + '\\theme\\qss\\'
    return resource


class MainWindow(QW.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.InitWindow()

    def InitTitleBar(self):
        self.titleBar = ui.TitleBar.TitleBar(self)

    def InitReceiveBlcok(self):
        self.receiveGroupBox = QW.QGroupBox(self.central)
        self.receiveGroupBox.setTitle('发送区')
        receiveLay = QW.QVBoxLayout(self.receiveGroupBox)
        self.receiveGroupBox.setLayout(receiveLay)
        clearButtonLay = QW.QHBoxLayout()
        spacer = QW.QSpacerItem(40, 20, QW.QSizePolicy.Expanding, QW.QSizePolicy.Minimum)
        self.clearButton = QW.QPushButton(self.receiveGroupBox)
        self.clearButton.setText('清除屏幕')
        self.receiveTextBrowser = QW.QTextBrowser(self.receiveGroupBox)

        # clearButtonLay.setContentsMargins(0, 0, 0, 0)
        clearButtonLay.addItem(spacer)
        clearButtonLay.addWidget(self.clearButton)
        receiveLay.addLayout(clearButtonLay)
        receiveLay.addWidget(self.receiveTextBrowser)
        self.leftLay.addWidget(self.receiveGroupBox)

    def InitPortSetBlcok(self):
        self.portGroupBox = QW.QGroupBox(self.central)
        policy = QW.QSizePolicy(QW.QSizePolicy.Fixed, QW.QSizePolicy.Fixed)
        policy.setHorizontalStretch(0)
        policy.setVerticalStretch(0)
        policy.setHeightForWidth(self.portGroupBox.sizePolicy().hasHeightForWidth())
        self.portGroupBox.setSizePolicy(policy)
        self.portGroupBox.setMinimumSize(QC.QSize(177, 168))
        self.portGroupBox.setMaximumSize(QC.QSize(177, 168))
        self.portGroupBox.setBaseSize(QC.QSize(177, 168))
        self.portGroupBox.setTitle('串口设置')

        self.onoffButton = QW.QPushButton(self.portGroupBox)
        self.onoffButton.setText('打开串口')
        self.onoffButton.setCheckable(True)

        portLabel = QW.QLabel(self.portGroupBox)
        rateLabel = QW.QLabel(self.portGroupBox)
        databitsLabel = QW.QLabel(self.portGroupBox)
        parityLabel = QW.QLabel(self.portGroupBox)
        stopbitLabel = QW.QLabel(self.portGroupBox)

        self.portComboBox = widget.combo.ComboBox(self.portGroupBox)
        self.rateComboBox = QW.QComboBox(self.portGroupBox)
        self.databitsComboBox = QW.QComboBox(self.portGroupBox)
        self.parityComboBox = QW.QComboBox(self.portGroupBox)
        self.stopbitComboBox = QW.QComboBox(self.portGroupBox)

        self.portComboBox.addItem('点击刷新')
        self.rateComboBox.addItems(['115200', '9600'])
        self.databitsComboBox.addItems(['8', '9', '7'])
        self.parityComboBox.addItems(['无校验', '奇校验', '偶校验'])
        self.stopbitComboBox.addItems(['1', '0.5', '1.5', '2'])

        portLabel.setText('端口号')
        rateLabel.setText('波特率')
        databitsLabel.setText('数据位')
        parityLabel.setText('数据位')
        stopbitLabel.setText('停止位')

        portGridLay = QW.QGridLayout()
        portGridLay.addWidget(portLabel, 0, 0)
        portGridLay.addWidget(rateLabel, 1, 0)
        portGridLay.addWidget(databitsLabel, 2, 0)
        portGridLay.addWidget(parityLabel, 3, 0)
        portGridLay.addWidget(stopbitLabel, 4, 0)

        portGridLay.addWidget(self.portComboBox, 0, 1)
        portGridLay.addWidget(self.rateComboBox, 1, 1)
        portGridLay.addWidget(self.databitsComboBox, 2, 1)
        portGridLay.addWidget(self.parityComboBox, 3, 1)
        portGridLay.addWidget(self.stopbitComboBox, 4, 1)
        portGridLay.setColumnStretch(0, 1)
        portGridLay.setColumnStretch(1, 2)

        portGroupBoxLay = QW.QVBoxLayout(self.portGroupBox)
        portGroupBoxLay.addLayout(portGridLay)
        portGroupBoxLay.addWidget(self.onoffButton)
        self.setLay.addWidget(self.portGroupBox)

    def InitDisplaySetBlcok(self):


        self.displaysetGroupBox = QW.QGroupBox(self.central)

        policy = QW.QSizePolicy(QW.QSizePolicy.Fixed, QW.QSizePolicy.Fixed)
        policy.setHorizontalStretch(0)
        policy.setVerticalStretch(0)
        policy.setHeightForWidth(self.displaysetGroupBox.sizePolicy().hasHeightForWidth())
        self.displaysetGroupBox.setSizePolicy(policy)
        self.displaysetGroupBox.setMinimumSize(QC.QSize(WINDOW_DISPLAY_SET_WIDTH, WINDOW_SET_LAY_HEIGHT))
        self.displaysetGroupBox.setMaximumSize(QC.QSize(WINDOW_DISPLAY_SET_WIDTH, WINDOW_SET_LAY_HEIGHT))
        self.displaysetGroupBox.setBaseSize(QC.QSize(WINDOW_DISPLAY_SET_WIDTH, WINDOW_SET_LAY_HEIGHT))
        self.displaysetGroupBox.setTitle('显示设置')

        displaysetLay = QW.QGridLayout(self.displaysetGroupBox)
        self.displaysetGroupBox.setLayout(displaysetLay)

        self.newlinedisplayCheckBox = QW.QCheckBox(self.displaysetGroupBox)
        self.timedisplayCheckBox = QW.QCheckBox(self.displaysetGroupBox)
        self.datedisplayCheckBox = QW.QCheckBox(self.displaysetGroupBox)
        self.senddisplayCheckBox = QW.QCheckBox(self.displaysetGroupBox)
        self.hexdisplayComboBox = QW.QCheckBox(self.displaysetGroupBox)
        self.ascdisplayComboBox = QW.QCheckBox(self.displaysetGroupBox)

        self.newlinedisplayCheckBox.setText('换行')
        self.timedisplayCheckBox.setText('时间')
        self.datedisplayCheckBox.setText('日期')
        self.senddisplayCheckBox.setText('发送')
        self.hexdisplayComboBox.setText('HEX')
        self.ascdisplayComboBox.setText('ASC')

        displaysetLay.addWidget(self.timedisplayCheckBox, 0, 0)
        displaysetLay.addWidget(self.datedisplayCheckBox, 0, 1)
        displaysetLay.addWidget(self.senddisplayCheckBox, 1, 0)
        displaysetLay.addWidget(self.newlinedisplayCheckBox, 1, 1)
        displaysetLay.addWidget(self.hexdisplayComboBox, 2, 0)
        displaysetLay.addWidget(self.ascdisplayComboBox, 2, 1)

        self.setLay.addWidget(self.displaysetGroupBox)

    def InitSendSetBlcok(self):
        self.sendsetGroupBox = QW.QGroupBox(self.central)
        policy = QW.QSizePolicy(QW.QSizePolicy.Fixed, QW.QSizePolicy.Fixed)
        policy.setHorizontalStretch(0)
        policy.setVerticalStretch(0)
        policy.setHeightForWidth(self.sendsetGroupBox.sizePolicy().hasHeightForWidth())
        self.sendsetGroupBox.setSizePolicy(policy)
        self.sendsetGroupBox.setMinimumSize(QC.QSize(102, 168))
        self.sendsetGroupBox.setMaximumSize(QC.QSize(102, 168))
        self.sendsetGroupBox.setBaseSize(QC.QSize(102, 168))
        self.sendsetGroupBox.setTitle('发送设置')

        sendsetGroupBoxLay = QW.QVBoxLayout(self.sendsetGroupBox)
        self.sendsetGroupBox.setLayout(sendsetGroupBoxLay)

        periodLaber = QW.QLabel(self.sendsetGroupBox)
        self.periodLineEdit = QW.QLineEdit(self.sendsetGroupBox)
        self.periodSendCheckBox = QW.QCheckBox(self.sendsetGroupBox)
        self.newlineSendCheckBox = QW.QCheckBox(self.sendsetGroupBox)
        self.hexSendComboBox = QW.QComboBox(self.sendsetGroupBox)

        periodLaber.setText('周期')
        self.periodSendCheckBox.setText('周期发送')
        self.newlineSendCheckBox.setText('换行发送')
        self.hexSendComboBox.addItems(['ASCII发送', 'HEX发送'])
        periodinputLay = QW.QHBoxLayout()
        periodinputLay.addWidget(periodLaber)
        periodinputLay.addWidget(self.periodLineEdit)

        sendsetGroupBoxLay.addLayout(periodinputLay)
        sendsetGroupBoxLay.addWidget(self.periodSendCheckBox)
        sendsetGroupBoxLay.addWidget(self.newlineSendCheckBox)
        sendsetGroupBoxLay.addWidget(self.hexSendComboBox)
        self.setLay.addWidget(self.sendsetGroupBox)

    def InitSendBlcok(self):
        self.sendGroupBox = QW.QGroupBox(self.central)
        policy = QW.QSizePolicy(QW.QSizePolicy.Preferred, QW.QSizePolicy.Fixed)
        policy.setHorizontalStretch(0)
        policy.setVerticalStretch(0)
        policy.setHeightForWidth(self.sendGroupBox.sizePolicy().hasHeightForWidth())
        self.sendGroupBox.setSizePolicy(policy)
        self.sendGroupBox.setMinimumSize(QC.QSize(0, 168))
        self.sendGroupBox.setMaximumSize(QC.QSize(16777215, 168))
        self.sendGroupBox.setBaseSize(QC.QSize(102, 168))
        self.sendGroupBox.setTitle('发送区')
        sendGroupBoxLay = QW.QHBoxLayout(self.sendGroupBox)
        self.sendGroupBox.setLayout(sendGroupBoxLay)

        self.sendTableWidget = QW.QTabWidget(self.sendGroupBox)
        self.sendButton = QW.QPushButton('发送', self.sendGroupBox)
        policy = QW.QSizePolicy(QW.QSizePolicy.Preferred, QW.QSizePolicy.Preferred)
        policy.setHorizontalStretch(0)
        policy.setVerticalStretch(0)
        policy.setHeightForWidth(self.sendButton.sizePolicy().hasHeightForWidth())
        self.sendButton.setSizePolicy(policy)

        sendWidget: list[QW.QWidget] = []
        sendLay: list[QW.QVBoxLayout] = []
        self.sendTextEdit: list[QW.QTextEdit] = []

        for i in range(3):
            sendWidget.append(QW.QWidget())
            self.sendTextEdit.append(QW.QTextEdit(sendWidget[i]))
            sendLay.append(QW.QVBoxLayout(sendWidget[i]))
            sendLay[i].addWidget(self.sendTextEdit[i])
            self.sendTableWidget.addTab(sendWidget[i], '发送' + str(i))
        self.sendTableWidget.setCurrentIndex(0)

        sendGroupBoxLay.addWidget(self.sendTableWidget)
        sendGroupBoxLay.addWidget(self.sendButton)
        sendGroupBoxLay.setStretch(0, 1)
        sendGroupBoxLay.setStretch(1, 0)
        self.setLay.addWidget(self.sendGroupBox)

    def InitCommandsBlcok(self):
        self.cmdsGroupBox = QW.QGroupBox(self.central)
        self.cmdsGroupBox.setTitle('发送命令')
        self.cmdsGroupBoxLay = QW.QGridLayout(self.cmdsGroupBox)
        self.cmdsButtonGroup = QW.QButtonGroup(self.cmdsGroupBox)
        self.cmdsGroupBoxLay.setContentsMargins(5, 0, 0, 0)
        self.cmdsGroupBoxLay.setHorizontalSpacing(0)
        self.cmdsGroupBoxLay.setVerticalSpacing(0)

        # self.clientLay.addWidget(self.sendsetGroupBox)

        # 创建空列表并指定元素类型
        self.cmdLineEdit: list[QW.QLineEdit] = []
        self.cmdButton: list[QW.QPushButton] = []
        for i in range(18):
            self.cmdLineEdit.append(QW.QLineEdit(self.cmdsGroupBox))
            self.cmdButton.append(QW.QPushButton(self.cmdsGroupBox))
            self.cmdButton[i].setText(str(i))
            self.cmdsButtonGroup.addButton(self.cmdButton[i], i)
            self.cmdsGroupBoxLay.addWidget(self.cmdLineEdit[i], i, 0)
            self.cmdsGroupBoxLay.addWidget(self.cmdButton[i], i, 1)

    def InitMenu(self):
        self.menu: list[QW.QMenu] = []
        self.menu.append(QW.QMenu('窗口', self.titleBar.menubar))
        self.menu.append(QW.QMenu('编码', self.titleBar.menubar))
        self.menu.append(QW.QMenu('主题', self.titleBar.menubar))

        icon = QG.QIcon()
        icon.addPixmap(QG.QPixmap(":/icon/menu-unselected"), QG.QIcon.Selected, QG.QIcon.Off)
        icon.addPixmap(QG.QPixmap(":/icon/menu-selected"), QG.QIcon.Selected, QG.QIcon.On)

        self.showCmdsAction = QW.QAction('命令窗口', self.titleBar.menubar)
        self.showCmdsAction.setCheckable(True)
        self.showCmdsAction.setIcon(icon)
        self.menu[0].addAction(self.showCmdsAction)

        self.encodeActionGroup = QW.QActionGroup(self.menu[1])
        self.utfEncodeAction = QW.QAction('UTF-8', self.titleBar.menubar)
        self.utfEncodeAction.setCheckable(True)
        self.utfEncodeAction.setIcon(icon)
        self.encodeActionGroup.addAction(self.utfEncodeAction)
        self.menu[1].addAction(self.utfEncodeAction)

        self.gbkEncodeAction = QW.QAction('GBK', self.titleBar.menubar)
        self.gbkEncodeAction.setCheckable(True)
        self.gbkEncodeAction.setIcon(icon)
        self.encodeActionGroup.addAction(self.gbkEncodeAction)
        self.menu[1].addAction(self.gbkEncodeAction)

        self.gb2312EncodeAction = QW.QAction('GB2312', self.titleBar.menubar)
        self.gb2312EncodeAction.setCheckable(True)
        self.gb2312EncodeAction.setIcon(icon)
        self.encodeActionGroup.addAction(self.gb2312EncodeAction)
        self.menu[1].addAction(self.gb2312EncodeAction)

        self.qss = ui.theme.qss.Load(GetResourcePath())
        self.qssName = self.qss.GetThemes()
        self.qssThemeAction: list[QW.QAction] = list()
        self.qssThemeActionGroup = QW.QActionGroup(self.menu[2])
        self.qssThemeActionGroup.triggered.connect(self.selectThemeCallback)
        for i in range(len(self.qssName)):
            self.qssThemeAction.append(QW.QAction(self.qssName[i], self.titleBar.menubar))
            self.qssThemeAction[i].setCheckable(True)
            self.qssThemeAction[i].setIcon(icon)
            # self.qssThemeAction[i].triggered.connect(self.selectThemeCallback)
            self.menu[2].addAction(self.qssThemeAction[i])
            self.qssThemeActionGroup.addAction(self.qssThemeAction[i])  # 添加至组,Action会自动互斥

        for i in self.menu:
            self.titleBar.menubar.addAction(i.menuAction())

    def InitWindow(self):
        self.setWindowIcon(QG.QIcon(QG.QPixmap(":/icon/app")))
        self.setWindowFlags(QC.Qt.FramelessWindowHint)  #设置无边框窗口
        self.setMinimumSize(WINDOW_DEFAULT_WIDTH, WINDOW_DEFAULT_HEIGHT)  #设置最小窗口

        self.central = QW.QWidget(self)
        self.setCentralWidget(self.central)
        self.centralLay = QW.QVBoxLayout(self.central)
        self.central.setLayout(self.centralLay)
        self.clientLay = QW.QHBoxLayout()
        self.leftLay = QW.QVBoxLayout()
        self.setLay = QW.QHBoxLayout()

        self.InitTitleBar()
        self.InitMenu()
        self.InitReceiveBlcok()
        self.InitPortSetBlcok()
        self.InitDisplaySetBlcok()
        self.InitSendSetBlcok()
        self.InitSendBlcok()
        self.InitCommandsBlcok()

        self.leftLay.addLayout(self.setLay)
        self.clientLay.addLayout(self.leftLay)
        self.clientLay.addWidget(self.cmdsGroupBox)
        self.centralLay.addWidget(self.titleBar)
        self.centralLay.addLayout(self.clientLay)

        self.clientLay.setStretch(0, 3)
        self.clientLay.setStretch(1, 1)

        if len(self.qssName):
            style = self.qss.GetTheme(self.qssName[0])
            self.setStyleSheet(style)

    def selectThemeCallback(self, act: QW.QAction):
        style = self.qss.GetTheme(act.text())
        self.setStyleSheet(style)

    def setTitle(self, title: str):
        self.titleBar.titleLabel.setText(title)


if __name__ == '__main__':

    def print_cmd_button_click(id):
        print('Buttonclicked', id)

    app = QW.QApplication(sys.argv)
    win = MainWindow()
    win.resize(900, 600)
    win.setTitle('主窗口')
    win.cmdsButtonGroup.buttonClicked[int].connect(print_cmd_button_click)
    win.show()
    sys.exit(app.exec_())
