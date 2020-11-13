#!/usr/bin/env python
# -*- coding: utf-8 -*-

# demo6 时间打印器(基于信号槽机制的自定义线程类)

import time
import sys
from PySide2.QtCore import QObject, Signal, Slot, QThread
from PySide2.QtWidgets import QApplication, QPushButton, QDialog, QVBoxLayout


class GetTimeQThread(QThread, QObject):  
    """   自定义线程类：用于打印当前时间   
    注意这里使用 Python 多继承的概念，同时继承了 QThread 类和 QObjet 类  
    """    
    
    # 定义信号：每隔一秒钟触发信号，并将当前时间信息发射出去  
    # 注意这里使用了带参数的信号，待发射的时间信息为 str 类型  
    clock_signal = Signal(str)    
    
    def __init__(self):    
        # 父类初始化    
        #QThread.__init__(self)    
        #QObject.__init__(self)
        super().__init__()
        self.switch = True
        
    def run(self):    
        """ 重写 run 方法：实现子线程处理逻辑 """
        print('子线程启动了喵喵')
        while self.switch:           
            self.clock_signal.emit(time.asctime())   # 直接将时间信息发射出去
            time.sleep(1)                            # 休眠1秒            
        print('子线程关掉了喵喵')
            
        
class MainWindow(QDialog):
   
    def __init__(self):
        super().__init__()
        self.button = QPushButton('开始打印')
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)       
        self.button.clicked.connect(self.ctrlMyThread)
        
        self.threadAlive = False
        
    @Slot(str)
    def printTime(self,currentTime: str):  
        """ 定义槽函数：接收子线程传送过来的时间信息，并打印出来   
        :param currentTime: 由子线程发射过来的时间信息  
        """  
        print(currentTime)            

    @Slot()
    def ctrlMyThread(self):
        if self.threadAlive == False:
            # 实例化子线程对象  
            self.myQThread = GetTimeQThread()        
            # 连接子线程的信号到主线程的槽函数中  
            self.myQThread.clock_signal.connect(self.printTime)    
            # 启动子线程  
            self.myQThread.start()
            self.threadAlive = True
            self.button.setText('结束打印')
        else:
            self.myQThread.switch = False
            self.threadAlive = False
            self.button.setText('开始打印')

        
if __name__ == "__main__":  
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show() 
    sys.exit(app.exec_())