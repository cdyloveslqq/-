import tkinter as tk
import random
import threading
import time


def dow():
    window = tk.Tk()
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    a = random.randrange(0, width)
    b = random.randrange(0, height)
    window.title('520快乐')  # 弹窗的名字，都可以修改的
    window.geometry("200x50" + "+" + str(a) + "+" + str(b))  # 弹窗大小，不建议修改
    tk.Label(window,
             text='爱你呦我的青青',  # 标签的文字，随便改
             bg='lightcyan',  # 背景颜色
             font=('楷体', 17),  # 字体和字体大小
             width=15, height=2  # 标签长宽
             ).pack()  # 固定窗口位置
    window.mainloop()




