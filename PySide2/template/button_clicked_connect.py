from PySide2.QtWidgets import QPushButton
from PySide2.QtCore import Slot


@Slot()
def slot_function():  
    """  定义槽函数：处理按钮被单击时的事件  
    其中 @Slot() 为槽函数的装饰器，其实也可以不写装饰器，但为了便于区分普通的函数，还是建议加上装饰器。  
    """  
    pass


# 实例化一个 Qt 控件（如按钮）
btn = QPushButton()

# 直接将控件的某个信号（如按钮的 clicked 信号）使用 connect 方法连接到槽函数
btn.clicked.connect(slot_function)