'''
    自定义标题栏，实现：
    1. 窗口最小化、最大化、关闭
    2. 菜单功能
    3. 标题功能
    4. 拖动功能
    5. 双击最大化
    6. 自定义缩放
'''

import sys
import PyQt5.QtGui as QG
import PyQt5.QtCore as QC
import PyQt5.QtWidgets as QW


TITLE_BAR_HEIGHT = 25
TITLE_BUTTON_WIDTH = 25
TITLE_LABEL_WIDTH = 25
TITLE_ICON_MENU_SPACE_WIDTH = 20
TITLE_MENU_WIDTH = 130

class TitleBar(QW.QWidget):

    def __init__(self, parent):
        super(TitleBar, self).__init__()
        self.win = parent
        self.InitWindow()

    def InitIcon(self):
        self.iconLabel = QW.QLabel(self)
        self.iconLabel.setFixedSize(TITLE_LABEL_WIDTH, TITLE_BAR_HEIGHT)
        # self.iconLabel.setAlignment(Qt.AlignCenter)
        self.iconLabel.setPixmap(QG.QPixmap(":/icon/app").scaledToHeight(26))

    def InitMenuBar(self):
        self.menubar = QW.QMenuBar(self)
        sizePolicy = QW.QSizePolicy(QW.QSizePolicy.Minimum, QW.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy)
        self.menubar.setMaximumSize(QC.QSize(TITLE_MENU_WIDTH, TITLE_BAR_HEIGHT))

    def InitTitle(self):
        self.titleLabel = QW.QLabel(self)
        self.titleLabel.setFixedHeight(TITLE_BAR_HEIGHT)
        self.titleLabel.setAlignment(QC.Qt.AlignCenter)
        self.titleLabel.setText('自定义标题栏')

    def InitButton(self):
        self.minButton = QW.QPushButton(self)
        self.restoreButton = QW.QPushButton(self)
        self.closeButton = QW.QPushButton(self)

        self.minButton.setFixedSize(TITLE_BUTTON_WIDTH, TITLE_BAR_HEIGHT)
        self.restoreButton.setFixedSize(TITLE_BUTTON_WIDTH, TITLE_BAR_HEIGHT)
        self.closeButton.setFixedSize(TITLE_BUTTON_WIDTH, TITLE_BAR_HEIGHT)

        self.minButton.setIcon(QG.QIcon(QG.QPixmap(":/icon/win-min")))
        self.restoreButton.setIcon(QG.QIcon(QG.QPixmap(":/icon/win-max")))
        self.closeButton.setIcon(QG.QIcon(QG.QPixmap(":/icon/win-close")))

        self.minButton.clicked.connect(self.MinWindow)
        self.restoreButton.clicked.connect(self.RestoreWindow)
        self.closeButton.clicked.connect(self.CloseWindow)

    def InitLayout(self):
        self.lay = QW.QHBoxLayout(self)
        self.setLayout(self.lay)
        self.lay.setSpacing(0)
        self.lay.setContentsMargins(0, 0, 0, 0)

        spacer =QW.QSpacerItem(TITLE_ICON_MENU_SPACE_WIDTH, TITLE_BAR_HEIGHT, QW.QSizePolicy.Fixed,QW.QSizePolicy.Minimum)

        self.lay.addWidget(self.iconLabel)
        self.lay.addItem(spacer)
        self.lay.addWidget(self.menubar)
        self.lay.addWidget(self.titleLabel)
        self.lay.addWidget(self.minButton)
        self.lay.addWidget(self.restoreButton)
        self.lay.addWidget(self.closeButton)

    def InitWindow(self):
        self.isPressed = False
        self.setFixedHeight(TITLE_BAR_HEIGHT)
        self.InitIcon()
        self.InitMenuBar()
        self.InitTitle()
        self.InitButton()
        self.InitLayout()

    def setTitle(self,title:str):
        self.titleLabel.setText(title)

    def MinWindow(self):
        self.win.showMinimized()

    def RestoreWindow(self):
        if self.win.isMaximized():
            self.win.showNormal()
        else:
            self.win.showMaximized()

    def CloseWindow(self):
        self.win.close()

    def mouseDoubleClickEvent(self, event):
        self.RestoreWindow()
        return QW.QWidget().mouseDoubleClickEvent(event)

    def mousePressEvent(self, event):
        self.isPressed = True
        self.startPos = event.globalPos()
        return QW.QWidget().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        self.isPressed = False
        return QW.QWidget().mouseReleaseEvent(event)

    def mouseMoveEvent(self, event):
        if self.isPressed:
            if self.win.isMaximized:
                self.win.showNormal()

            movePos = event.globalPos() - self.startPos
            self.startPos = event.globalPos()
            self.win.move(self.win.pos() + movePos)

        return QW.QWidget().mouseMoveEvent(event)


if __name__ == '__main__':
    
    def set_menu(obj, menubar):
        menu = []
        menu.append(QW.QMenu(menubar))
        menu.append(QW.QMenu(menubar))
        menu.append(QW.QMenu(menubar))

        action = []
        action.append(QW.QAction(obj))
        action.append(QW.QAction(obj))
        action.append(QW.QAction(obj))
        action.append(QW.QAction(obj))

        menu[0].addAction(action[0])
        menu[0].addAction(action[1])
        menu[0].addAction(action[2])
        menu[0].addAction(action[3])

        menubar.addAction(menu[0].menuAction())
        menubar.addAction(menu[1].menuAction())
        menubar.addAction(menu[2].menuAction())

        menu[0].setTitle('菜单1')
        menu[1].setTitle('菜单2')
        menu[2].setTitle('菜单3')

        action[0].setText('选择1')
        action[1].setText('选择2')
        action[2].setText('选择3')
        action[3].setText('选择4')

    import res.res

    app = QW.QApplication(sys.argv)
    win = QW.QMainWindow()
    win.resize(727, 30)
    bar = TitleBar(win)
    center = QW.QWidget(win)
    lay = QW.QVBoxLayout(center)
    center.setLayout(lay)
    lay.addWidget(bar)
    set_menu(win, bar.menubar)
    win.setCentralWidget(center)
    win.show()
    sys.exit(app.exec_())
