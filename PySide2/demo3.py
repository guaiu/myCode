#!/usr/bin/env python
# -*- coding: utf-8 -*-

# demo3 简单按钮的实现(基于内置信号与槽)

import sys
from PySide2.QtWidgets import QApplication, QPushButton
from PySide2.QtCore import Slot

@Slot()
def meow():
 print("喵喵？")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    button = QPushButton("Don't click me!")
    button.clicked.connect(meow)
    button.show()
    sys.exit(app.exec_())