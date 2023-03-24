import sys
import PyQt5.QtWidgets as Qw
import PyQt5.QtCore as Qc

'''
例子：演示如何捕获按键、鼠标动作.
'''

class Example(Qw.QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):      

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Event handler')
        self.show()

    def keyPressEvent(self, event):
        if event.key() == Qc.Qt.Key_Escape:
            # 按下ESC键程序就会退出。
            self.close()
        else:
            print(event.key())

    def mousePressEvent(self, event):
        print(event.button())

if '__main__' == __name__:


    app = Qw.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())