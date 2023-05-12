# ---------------------------------------------------------import---------------------------------------------------------
import os, sys
import PyQt5.QtGui as QG
import PyQt5.QtCore as QC
import PyQt5.QtWidgets as QW
# ---------------------------------------------------------import---------------------------------------------------------


def GetPath():
    if hasattr(sys, '_MEIPASS'):
        execute_path = sys._MEIPASS
        install_path = os.path.split(sys.executable)[0]
    else:
        execute_path = os.path.dirname(__file__)
        install_path = os.path.split(sys.argv[0])[0]
        
    return (execute_path,install_path)


def CreateApplication():
    app = QW.QApplication(sys.argv)
    win = ui.MainWindow.MainWindow()
    win.setTitle('付伟专用串口助手')
    # win.setStyleSheet(style)
    win.show()

    return (app, win)


if __name__ == "__main__":

    root = GetPath()
    sys.path.append(root[0] + '\\ui')
    sys.path.append(root[0] + '\\ut')
    sys.path.append(root[0] + '\\widget')
    sys.path.append(root[0] + '\\init')

    import ui.theme.qss
    import ui.MainWindow
    import ui.TitleBar
    import ui.res.res
    import ut.uart
    import uc.action
    import uc.init
    import uc.setting

    ini = root[1] + '\\Settings.ini'
    app, win = CreateApplication()
    win.resize(900, 600)
    ut = ut.uart.Uart()
    uc.init.InitUi(win, ut)
    uc.action.Action(win, ut)
    uc.setting.Setting(win, ini)
    sys.exit(app.exec_())
