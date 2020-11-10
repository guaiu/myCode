#!/usr/bin/env python
# -*- coding: utf-8 -*-

# topic_slot   PySide2信号与槽
# topic_slot_1 内置信号 与 槽 的使用(使用控件的信号进行连接)

import sys
from PySide2.QtWidgets import QMessageBox,QPushButton,QApplication,QWidget
from PySide2.QtCore import Slot

@Slot()
def showMsg():
    """  定义槽函数：处理按钮被单击时的事件  
    其中 @Slot() 为槽函数的装饰器，其实也可
    以不写装饰器，但为了便于区分普通的函数，
    还是建议加上装饰器。  
    """ 
    # guaiu注：不使用@Slot装饰的槽函数尤其是在自定义信号类时
    # 调用的语法会略有不同，具体参考topic_slot1_2.py文件，我的
    # 代码为了统一语法槽函数尽量加上@Slot()
    widget=QWidget()
    QMessageBox.information(widget,'信息提示框','Ok 弹出测试信息')

if __name__ == '__main__':
    app=QApplication(sys.argv)

    button=QPushButton('测试点击按钮')
    button.clicked.connect(showMsg)
    #按钮的clicked信号使用connect方法连接到槽函数
    #使用窗口控件内置的信号连接槽函数
    button.show()

    app.exec_()