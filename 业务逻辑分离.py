from PyQt5 import QtWidgets,QtGui,QtCore
from 小窗口 import Ui_MainWindow
class window(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(window,self).__init__(parent)
        self.setupUi(self)
    #从此刻开始编写业务逻辑代码
        zhanghao = QtCore.QRegExp('\w{6}[cdy]{3}')
        self.lineEdit.setValidator(QtGui.QRegExpValidator(zhanghao, self))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setValidator(QtGui.QIntValidator(10000000, 99999999))
        self.label_3.setText("<a href='https://www.baidu.com/'>百度一下<a>")
        self.label_3.setOpenExternalLinks(True)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)

if __name__=='__main__':
    import sys
    app=QtWidgets.QApplication(sys.argv)
    mainwindow=window()
    mainwindow.show()
    sys.exit(app.exec_())
