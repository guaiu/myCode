# 导入可能用到的标准库模块
import <lib>

# 导入 PySide2 库模块
from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Slot

# 导入其他自定义的模块包
import <custom_modules>
from <custom_modules> import <custom_class_or_function>


class MainWindow(QWidget):  
    """ MainWindow 继承 QWidget 类 """    
    def __init__(self):    
        QWidget.__init__(self)        
    
        # 设置类属性    
        pass      
    
        # 设置窗口属性    
        pass      
    
        # 创建窗口内部控件，并设置样式    
        self._create_components()    
        self._set_styles()      
    
    def _create_components(self):    
        """ 创建窗口内部的子控件 """    
        pass
    
    def _set_styles(self):    
        """ 设置窗口及其子控件的样式 """    
        pass
    
    @Slot()  
    def _slot_xxx_www(self):    
        """ 槽函数：连接至xxx控件的www信号 """    
        pass
    
    def _other_protected_function(self):    
        """ 其他的 protected 访问权限的方法 """    
        pass
    
    def other_public_function(self):    
        """ 其他的 public 访问权限的方法 """    
        pass