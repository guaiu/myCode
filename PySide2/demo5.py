#!/usr/bin/env python
# -*- coding: utf-8 -*-

# demo5 简单对话框的实现(信号与槽)

import sys
import os

from PySide2.QtWidgets import (QLineEdit, QPushButton, QApplication,
    QVBoxLayout, QDialog,QLabel)
from PySide2.QtCore import Slot

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        # Create widgets
        self.edit = QLineEdit("喵喵")
        self.buttonPrint = QPushButton("打印文本")
        self.buttonClear = QPushButton("清空文本")
        self.buttonCls = QPushButton('清空屏幕')
        self.label = QLabel('在这里输入')
        
        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.edit)
        layout.addWidget(self.buttonPrint)
        layout.addWidget(self.buttonClear)
        layout.addWidget(self.buttonCls)
        
        # Set dialog layout
        self.setLayout(layout)
        
        # Connect signal to slot
        self.buttonPrint.clicked.connect(self.printEdit)
        self.buttonClear.clicked.connect(self.clearEdit)
        self.buttonCls.clicked.connect(self.clearScreen)

    # Set slot functions
    @Slot()
    def printEdit(self):
        print (self.edit.text())
        
    @Slot()    
    def clearEdit(self):
        self.edit.clear()
        
    @Slot()
    def clearScreen(self):
        os.system('cls')
        

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    
    # Create and show the form
    form = Form()
    form.show()
    
    # Run the main Qt loop
    sys.exit(app.exec_())