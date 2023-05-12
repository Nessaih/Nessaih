
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

uc_win: ui.MainWindow.MainWindow = None
uc_uart: ut.uart.Uart = None



def SetPeriodNumberInput():
    valid_input = QG.QRegExpValidator(QC.QRegExp('\d+'))
    uc_win.periodLineEdit.setValidator(valid_input)



class InitUi:
    def __init__(self, __win: ui.MainWindow.MainWindow, __uart: ut.uart.Uart):
        global uc_win, uc_uart
        uc_win = __win
        uc_uart = __uart
        self.__initui()

    def __initui(self):
        uc_win.onoffButton.toggle()
        SetPeriodNumberInput()
