# coding: utf-8


'''
参考文档:
    1. 串口相关操作 
    https://blog.csdn.net/windowsyun/article/details/80001488

    2. 重写QComboBox, 实现点击QComboBox自动刷新串口列表。
    https://www.jb51.net/article/163876.htm
    
    问题: 做项目的时候用到QComboBox展示串口号, 但是有个问题是因为初始化的时候获取串口号列表, 
         软件运行起来后, 串口更新了也无法识别, 必须重启软件重新初始化才行。(因为一些原因无法
         做成弹框等形式) 查询资料发现QComboBox是没有类似clicked的信号, 所以没法直接用内置的信号槽处理。
    思路: 重写showPopup函数:
    原理: 继承QComboBox类, 在新的类中加入1个鼠标点击信号, 当showPopup()方法被调用时, 顺便发送出一个鼠标点击信号即可。
'''




import PyQt5.QtCore as QC
import PyQt5.QtWidgets as QW

class ComboBox(QW.QComboBox):
    clicked = QC.pyqtSignal()  # 创建一个信号
    def showPopup(self):
        self.clicked.emit()  # 发送信号
        super(ComboBox, self).showPopup()  # 调用父类中的showPopup函数