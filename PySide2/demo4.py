#!/usr/bin/env python
# -*- coding: utf-8 -*-

# demo4 自定义信号类和槽类

#import sys

from PySide2.QtWidgets import QApplication
from PySide2.QtCore import Qt, QObject, Signal, Slot

#定义信号类，继承QObject
class mySignalClass(QObject):
    ''' 定义一个信号，注意信号的定义
    只能写在类属性中，不能作为对象属
    性定义在构造方法中。
    '''
    
    # 调用Signal()方法，无参数类型
    mySignal_1 = Signal()
    
    # 调用Signal()方法，声明参数类型和数量
    mySignal_2 = Signal(int,str)
    
    def __init__(self):
        super(mySignalClass, self).__init__()
        #也可以写成QObject.__init__(self)
        
    def sendSignal(self):
        ''' 调用该方法时向外部发送信号 '''
        self.mySignal_1.emit()
        #调用emit()方法发送信号
        self.mySignal_2.emit(10086,'喵喵')
        #带参数的信号则需一起发送参数


#定义槽类，继承QObject        
class mySlotClass(QObject):
    def __init__(self):
        super(mySlotClass, self).__init__()
        #也可以写成QObject.__init__(self)
        
    @Slot()
    def dealMySignal_1(self):
        ''' 定义槽函数1，无参数的槽函数不需要声明参数 '''
        print('处理信号1：')
        print('我没有手机！')
        
    @Slot(int,str)
    def dealMySignal_2(self, num:int, name:str):
        ''' 注意此时装饰器以及函数的参数列表应该与信号中定义的参数列表一致 '''
        print('处理信号2：')
        print('我的名字是{}，我的手机号码是{}'.format(name,num))
        
    
if __name__ == '__main__':
    
    #app = QApplication(sys.argv)
    
    #实例化信号对象
    send = mySignalClass()
    #实例化槽对象
    slot = mySlotClass()
    
    #信号实例绑定槽实例的槽函数
    send.mySignal_1.connect(slot.dealMySignal_1)
    send.mySignal_2.connect (slot.dealMySignal_2)
    
    #发射信号
    send.sendSignal()
    
    #可以解绑
    '''
    send.mySignal_1.disconnect(slot.dealMySignal_1)
    send.mySignal_2.disconnect (slot.dealMySignal_2
    '''
    
    #sys.exit(app.exec_())