import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QDockWidget, QWidget, 
                              QTextEdit, QVBoxLayout, QLabel, QPushButton)
from PySide6.QtCore import Qt


class DockWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("PySide6 可停靠窗口测试")
        self.setMinimumSize(1000, 700)
        
        # 中央部件
        self.central = QTextEdit()
        self.central.setPlainText("中央区域\n\n可以拖动四周的窗口到不同位置")
        self.setCentralWidget(self.central)
        
        # 创建停靠窗口
        self.create_dock_windows()
        
        # 设置停靠窗口选项
        self.setDockOptions(
            QMainWindow.AnimatedDocks | 
            QMainWindow.AllowNestedDocks | 
            QMainWindow.AllowTabbedDocks
        )
        
        self.statusBar().showMessage("准备就绪")
        
    def create_dock_windows(self):
        # 左侧停靠窗口
        self.dock_left = QDockWidget("左侧窗口", self)
        self.dock_left.setAllowedAreas(Qt.AllDockWidgetAreas)
        
        left_content = QWidget()
        left_layout = QVBoxLayout(left_content)
        left_layout.addWidget(QLabel("左侧窗口内容"))
        left_layout.addWidget(QPushButton("左侧按钮"))
        
        self.dock_left.setWidget(left_content)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.dock_left)
        
        # 右侧停靠窗口
        self.dock_right = QDockWidget("右侧窗口", self)
        self.dock_right.setAllowedAreas(Qt.AllDockWidgetAreas)
        
        right_content = QWidget()
        right_layout = QVBoxLayout(right_content)
        right_layout.addWidget(QLabel("右侧窗口内容"))
        right_layout.addWidget(QPushButton("右侧按钮"))
        
        self.dock_right.setWidget(right_content)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock_right)
        
        # 底部停靠窗口
        self.dock_bottom = QDockWidget("底部窗口", self)
        self.dock_bottom.setAllowedAreas(Qt.AllDockWidgetAreas)
        
        bottom_content = QWidget()
        bottom_layout = QVBoxLayout(bottom_content)
        bottom_layout.addWidget(QLabel("底部窗口内容"))
        bottom_layout.addWidget(QPushButton("底部按钮"))
        
        self.dock_bottom.setWidget(bottom_content)
        self.addDockWidget(Qt.BottomDockWidgetArea, self.dock_bottom)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DockWindow()
    window.show()
    sys.exit(app.exec()) 