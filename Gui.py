import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import (QWidget, QToolTip,
                             QPushButton, QApplication, QLabel)
from pygtrans import Translate

client = Translate(proxies={"https": "socks5://localhost:1089"})  # 设置代理


def querys(ask):
    text = client.translate(ask)
    return text.translatedText


class MyTranslate(QWidget):

    def __init__(self):
        super().__init__()
        self.lbl = None
        self.clipboard = None
        self.initUI()

    def initUI(self):
        self.clipboard = app.clipboard()
        self.clipboard.dataChanged.connect(self.change_deal)
        self.lbl = QLabel(self)
        self.lbl.setText("Welcome!")
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)  # 置于顶部
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('MyTranslate')
        self.show()

    def change_deal(self):
        if self.windowState()!=QtCore.Qt.WindowActive:
            self.setWindowState(QtCore.Qt.WindowActive)  # 活动窗口
        data = self.clipboard.mimeData()
        self.lbl.setText(querys(data.text()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyTranslate()
    sys.exit(app.exec_())
