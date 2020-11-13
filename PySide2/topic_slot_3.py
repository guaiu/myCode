#!/usr/bin/env python
# -*- coding: utf-8 -*-

# topic_slot   PySide2信号与槽
# topic_slot_3 PySide2信号和槽传递额外参数

import sys

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
 
class MyForm(QMainWindow):
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        button1 = QPushButton('Button 1')
        button2 = QPushButton('Button 2')
        button1.clicked.connect(lambda: self.on_button(1))
        button2.clicked.connect(lambda: self.on_button(2))
 
        layout = QHBoxLayout()
        layout.addWidget(button1)
        layout.addWidget(button2)
 
        main_frame = QWidget()
        main_frame.setLayout(layout)
 
        self.setCentralWidget(main_frame)
    
    @Slot(int)
    def on_button(self, n:int):
        print('Button {0} clicked'.format(n))
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MyForm()
    form.show()
    app.exec_()