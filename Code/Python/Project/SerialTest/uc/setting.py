# coding: utf-8
import sys
import datetime
import PyQt5.QtGui as QG
import PyQt5.QtCore as QC
import PyQt5.QtWidgets as QW
import functools as FT

sys.path.append('SerialTest\\ui')
sys.path.append('SerialTest\\ut')

import ui.MainWindow
import ut.uart
import ui.theme.qss

class Setting:

    def __init__(self, __win: ui.MainWindow.MainWindow, __file:str):
        self.win = __win
        self.file = __file
        self.settings = QC.QSettings(self.file, QC.QSettings.Format.IniFormat)
        self.LoadAll()
        self.Connect()

    def Connect(self):
        self.win.titleBar.closeButton.clicked.connect(self.SaveOther)

        for i in range(len(self.win.sendTextEdit)):
            self.win.sendTextEdit[i].textChanged.connect(FT.partial(self.SendTextSave,i))

        for i in range(len(self.win.cmdLineEdit)):
            self.win.cmdLineEdit[i].textChanged.connect(FT.partial(self.CmdsSave,i))

    def LoadAll(self):
        self.win.sendTextEdit[0].setText(self.settings.value('sendTextEdit0', '', str))
        self.win.sendTextEdit[1].setText(self.settings.value('sendTextEdit1', '', str))
        self.win.sendTextEdit[2].setText(self.settings.value('sendTextEdit2', '', str))

        for i in range(len(self.win.cmdLineEdit)):
            self.win.cmdLineEdit[i].setText(self.settings.value('cmdsLineEdit'+str(i), '', str))


    def SaveOther(self):
        pass


    def SendTextSave(self, index):
        self.settings.setValue('sendTextEdit' + str(index), self.win.sendTextEdit[index].toPlainText())

    def CmdsSave(self, index):
        self.settings.setValue('cmdsLineEdit' + str(index), self.win.cmdLineEdit[index].text())
