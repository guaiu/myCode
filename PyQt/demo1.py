#!/usr/bin/env python
# -*- coding: utf-8 -*-

# demo1 标签功能的实现

import sys
from PySide2.QtWidgets import QApplication,QLabel

def simpleLabel(myStr):
    app = QApplication(sys.argv)
    label = QLabel(myStr)
    label.show()
    app.exec_()
    
if __name__ == '__main__':
    myStr = input('please input your str: ')
    simpleLabel(myStr)