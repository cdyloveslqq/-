from PyQt5.QtWidgets import QApplication,QLabel,QWidget,QVBoxLayout
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap,QPalette
import sys

class WindowDemo(QMainWindow):
    def __init__(self):
        super(WindowDemo, self).__init__()
        label4=QLabel(self)
        #设置标签4的文本，含有超链接
        label4.setText("<a href='http://www.4399.com/flash/35538.htm'>欢迎百度</a>")
        label4.setToolTip('这是一个超链接标签')
        label4.setOpenExternalLinks(True)
        #点击文本框绑定槽函数

