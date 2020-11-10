#!/usr/bin/env python
# -*- coding: utf-8 -*-

# topic_slot   PySide2信号与槽
# topic_slot_2 自定义信号 与 槽 的使用(自定义一个信号类)

from PySide2.QtWidgets import QApplication
from PySide2.QtCore import Qt, QObject, Signal, Slot


class CustomClass(QObject):  
    """ 这是一个自定义的类，在这个类里面要使用 Qt 的信号，因此必须继承 QObject 类 """    
    # guaiu注：这个类把发射信号和槽的功能合二为一了，事实上可以分开定义
    # 一个发射信号类和一个槽类，使类分工明确，参考demo4.py
    
    
    # 定义一个信号，注意信号的定义只能写在类属性中，不能作为对象属性定义在构造方法中。  
    custom_signal1 = Signal()    
    
    # 定义一个带参数的信号，此时只需声明参数的类型即可  
    custom_signal2 = Signal(int, str)    
    
    def __init__(self):    
        QObject.__init__(self)      
        
    def send_signal(self):    
        """ 调用该方法时向外部发送信号 """    
        self.custom_signal1.emit()              # 使用 emit() 方法发射信号    
        self.custom_signal2.emit(1, "hello")    # 带参数的信号则需一起发送参数        
        
    @Slot()
    def slot_deal_signal1(self):  
        """    定义槽函数，用于处理 custom_signal1 信号  """  
        print("get custom signal 1.")    
        
    @Slot(int, str)
    def slot_deal_signal2(self, num: int, text: str):  
        """  定义槽函数：用于处理 custom_signal2 信号  
        注意此时装饰器以及函数的参数列表应该与信号中定义的参数列表一致  
        """  
        print("get custom signal 2.")  
        print("the first arg is:", num)  
        print("the second arg is:", text)    
        

if __name__ == '__main__':        
    # 实例化这个类
    cs = CustomClass()

    # 连接信号与槽
    cs.custom_signal1.connect(cs.slot_deal_signal1)
    cs.custom_signal2.connect(cs.slot_deal_signal2)

    # 发射信号
    cs.send_signal()