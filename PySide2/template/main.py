import sys
from PySide2.QtWidgets import QApplication
from main_windows import MainWindow


if __name__ == "__main__":  
    app = QApplication(sys.argv)     # 创建 Qt 应用程序实例  
    main_win = MainWindow()          # 创建主窗口实例  
    main_win.show()                  # 显示主窗口  
    sys.exit(app.exec_())            # 进入循环监听事件