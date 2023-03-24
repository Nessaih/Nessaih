"""PySide6 port of the linechart example from Qt v6.x"""

import os
import cairosvg
from PySide6.QtCore import (QCoreApplication, QDir, QFile, QFileInfo,
                            QIODevice, QTextStream, QUrl, Qt)
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox,
                               QDialog, QFileDialog, QGridLayout, QHBoxLayout,
                               QHeaderView, QLabel, QLineEdit,
                               QPushButton, QSizePolicy, QTableWidget,
                               QTableWidgetItem, QVBoxLayout, QWidget, QTextEdit)

# os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = 'D:\software\Anaconda3\Lib\site-packages\PySide6\plugins\platforms'

class Window(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # 输入选择
        directory_label = QLabel("选择文件夹:")
        self._directory_combo_box = self.create_combo_box(QDir.currentPath())
        self._browse_button = self.create_button("&打开...", self.browse)

        # 输出选择
        output_directory_label = QLabel("输出到的文件夹:")
        self._output_directory_combo_box = self.create_combo_box(QDir.currentPath())
        self._output_browse_button = self.create_button("&选择...", self.output_browse)


        self._find_button = self.create_button("&转换", self.convert_svg2png)
        self.create_files_table()

        buttons_layout = QHBoxLayout()
        buttons_layout.addStretch()
        buttons_layout.addWidget(self._find_button)

        main_layout = QGridLayout()
        main_layout.addWidget(directory_label, 0, 0)
        main_layout.addWidget(self._directory_combo_box, 0, 1)
        main_layout.addWidget(self._browse_button, 0, 2)

        main_layout.addWidget(output_directory_label, 2, 0)
        main_layout.addWidget(self._output_directory_combo_box, 2, 1)
        main_layout.addWidget(self._output_browse_button, 2, 2)

        main_layout.addWidget(self._files_table, 3, 0, 1, 3)
        main_layout.addLayout(buttons_layout, 5, 0, 1, 3)
        self.setLayout(main_layout)

        self.setWindowTitle("将svg转换成png")
        self.resize(500, 300)

    def browse(self):
        self.directory = QFileDialog.getExistingDirectory(self, "转换",
                QDir.currentPath())

        if self.directory:
            if self._directory_combo_box.findText(self.directory) == -1:
                self._directory_combo_box.addItem(self.directory)

            self._directory_combo_box.setCurrentIndex(self._directory_combo_box.findText(self.directory))

    def output_browse(self):
        self.output_directory = QFileDialog.getExistingDirectory(self, "输出到",
                QDir.currentPath())

        if self.output_directory:
            if self._directory_combo_box.findText(self.output_directory) == -1:
                self._directory_combo_box.addItem(self.output_directory)

            self._directory_combo_box.setCurrentIndex(self._directory_combo_box.findText(self.output_directory))



    def convert_svg2png(self):
        for root, dirs, files in os.walk(self.directory):  # 遍历所有的文件
            for f in files:

                svgFile = os.path.join(root, f)  # svg文件名
                if f[-3:] == "svg":  # 确保是svg
                    pngFile = self.output_directory + "/" + f.replace("svg", "png")  # png文件名
                    try:
                        cairosvg.svg2png(url=svgFile, write_to=pngFile, dpi=1900)
                    except:
                        self._files_table.append('error =>' + pngFile)
                        print('error =>' + pngFile)
                    finally:
                        self._files_table.append('file => ' + pngFile)
                        print('file => ' + pngFile)

    def create_button(self, text, member):
        button = QPushButton(text)
        button.clicked.connect(member)
        return button

    def create_combo_box(self, text=""):
        combo_box = QComboBox()
        combo_box.setEditable(True)
        combo_box.addItem(text)
        combo_box.setSizePolicy(QSizePolicy.Expanding,
                QSizePolicy.Preferred)
        return combo_box

    def create_files_table(self):
        self._files_table = QTextEdit()
        self._files_table.setReadOnly(True)



if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


