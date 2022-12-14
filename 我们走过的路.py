# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '我们走过的路.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QMainWindow
import threading
import time
from turtle import *
class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
    def tree(self):
        import turtle as t  # as就是取个别名，后续调用的t都是turtle
        import random as r
        import time

        n = 100.0

        speed("fastest")  # 定义速度
        screensize(bg='black')  # 定义背景颜色，可以自己换颜色
        left(90)
        forward(3 * n)
        color("orange", "yellow")  # 定义最上端星星的颜色，外圈是orange，内部是yellow
        begin_fill()
        left(126)

        for i in range(5):  # 画五角星
            forward(n / 5)
            right(144)  # 五角星的角度
            forward(n / 5)
            left(72)  # 继续换角度
        end_fill()
        right(126)

        def drawlight():  # 定义画彩灯的方法
            if r.randint(0, 30) == 0:  # 如果觉得彩灯太多，可以把取值范围加大一些，对应的灯就会少一些
                color('tomato')  # 定义第一种颜色
                circle(6)  # 定义彩灯大小
            elif r.randint(0, 30) == 1:
                color('orange')  # 定义第二种颜色
                circle(3)  # 定义彩灯大小
            else:
                color('dark green')  # 其余的随机数情况下画空的树枝

        color("dark green")  # 定义树枝的颜色
        backward(n * 4.8)

        def tree(d, s):  # 开始画树
            if d <= 0: return
            forward(s)
            tree(d - 1, s * .8)
            right(120)
            tree(d - 3, s * .5)
            drawlight()  # 同时调用小彩灯的方法
            right(120)
            tree(d - 3, s * .5)
            right(120)
            backward(s)

        tree(15, n)
        backward(n / 2)

        for i in range(200):  # 循环画最底端的小装饰
            a = 200 - 400 * r.random()
            b = 10 - 20 * r.random()
            up()
            forward(b)
            left(90)
            forward(a)
            down()
            if r.randint(0, 1) == 0:
                color('tomato')
            else:
                color('wheat')
            circle(2)
            up()
            backward(a)
            right(90)
            backward(b)

        t.color("dark red", "red")  # 定义字体颜色
        t.write("Merry Christmas", align="center", font=("Comic Sans MS", 40, "bold"))  # 定义文字、位置、字体、大小

        def drawsnow():  # 定义画雪花的方法
            t.ht()  # 隐藏笔头，ht=hideturtle
            t.pensize(2)  # 定义笔头大小
            for i in range(200):  # 画多少雪花
                t.pencolor("white")  # 定义画笔颜色为白色，其实就是雪花为白色
                t.pu()  # 提笔，pu=penup
                t.setx(r.randint(-350, 350))  # 定义x坐标，随机从-350到350之间选择
                t.sety(r.randint(-100, 350))  # 定义y坐标，注意雪花一般在地上不会落下，所以不会从太小的纵座轴开始
                t.pd()  # 落笔，pd=pendown
                dens = 6  # 雪花瓣数设为6
                snowsize = r.randint(1, 10)  # 定义雪花大小
                for j in range(dens):  # 就是6，那就是画5次，也就是一个雪花五角星
                    # t.forward(int(snowsize))  #int（）取整数
                    t.fd(int(snowsize))
                    t.backward(int(snowsize))
                    # t.bd(int(snowsize))  #注意没有bd=backward，但有fd=forward，小bug
                    t.right(int(360 / dens))  # 转动角度

        drawsnow()  # 调用画雪花的方法
        t.done()  # 完成,否则会直接关闭

    def painter1(self):
        import 恋爱画板
        恋爱画板.main()
    def painter2(self):
        import 恋爱画板2
        threads = []
        for i in range(10):  # 需要的弹框数量，别太多了，电脑不好的话怕你死机
            t = threading.Thread(target=恋爱画板2.dow)
            threads.append(t)
            time.sleep(0.1)
            threads[i].start()
    def painter3(self):
        import 恋爱画板3
        恋爱画板3.main()
    def memory(self):
        import 回忆相册
        self.c=回忆相册.Ui_MainWindow()
        self.c.show()
    def video(self):
        import 我们的故事呀
        movie = 我们的故事呀.Movie_MP4(r"image\一生的许诺.mp4")
        movie.play()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(924, 610)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        self.menu_6 = QtWidgets.QMenu(self.menubar)
        self.menu_6.setObjectName("menu_6")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionlove_painter1 = QtWidgets.QAction(MainWindow)
        self.actionlove_painter1.setObjectName("actionlove_painter1")
        self.actionlove_painter2 = QtWidgets.QAction(MainWindow)
        self.actionlove_painter2.setObjectName("actionlove_painter2")
        self.actionlove_painter3 = QtWidgets.QAction(MainWindow)
        self.actionlove_painter3.setObjectName("actionlove_painter3")
        self.actionlet_us_go = QtWidgets.QAction(MainWindow)
        self.actionlet_us_go.setObjectName("actionlet_us_go")
        self.actionchemistry_test = QtWidgets.QAction(MainWindow)
        self.actionchemistry_test.setObjectName("actionchemistry_test")
        self.actionstart = QtWidgets.QAction(MainWindow)
        self.actionstart.setObjectName("actionstart")
        self.actionstart_2 = QtWidgets.QAction(MainWindow)
        self.actionstart_2.setObjectName("actionstart_2")
        self.actiongo = QtWidgets.QAction(MainWindow)
        self.actiongo.setObjectName("actiongo")
        self.menu.addAction(self.actionlove_painter1)
        self.menu.addAction(self.actionlove_painter2)
        self.menu.addAction(self.actionlove_painter3)
        self.menu_2.addAction(self.actionlet_us_go)
        self.menu_3.addAction(self.actiongo)
        self.menu_4.addAction(self.actionstart)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_6.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        MainWindow.setStyleSheet("#MainWindow{border-image:url(image/mainbackground.jpg)}")
        self.retranslateUi(MainWindow)
        self.actionlove_painter1.triggered.connect(self.painter1)
        self.actionlove_painter2.triggered.connect(self.painter2)
        self.actionlove_painter3.triggered.connect(self.painter3)
        self.actionlet_us_go.triggered.connect(self.tree)
        self.actionstart.triggered.connect(self.memory)
        self.actiongo.triggered.connect(self.video)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "我们走过的路"))
        self.menu.setTitle(_translate("MainWindow", "恋爱画板"))
        self.menu_2.setTitle(_translate("MainWindow", "我还给青青一颗圣诞树"))
        self.menu_4.setTitle(_translate("MainWindow", "璀璨回忆"))
        self.menu_3.setTitle(_translate("MainWindow", "我们的故事"))
        self.actionlove_painter1.setText(_translate("MainWindow", "love painter1"))
        self.actionlove_painter2.setText(_translate("MainWindow", "love painter2"))
        self.actionlove_painter3.setText(_translate("MainWindow", "love painter3"))
        self.actionlet_us_go.setText(_translate("MainWindow", "let us go!"))
        self.actionstart.setText(_translate("MainWindow", "start!"))
        self.actiongo.setText(_translate("MainWindow", "the last gift for you"))


import sys
if __name__=='__main__':
    app=QtWidgets.QApplication(sys.argv)
    Mainwindow=QtWidgets.QMainWindow()
    ui=Ui_MainWindow()
    ui.setupUi(Mainwindow)
    Mainwindow.show()
    sys.exit(app.exec_())