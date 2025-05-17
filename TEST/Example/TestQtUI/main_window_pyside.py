from PySide6.QtWidgets import (QMainWindow, QWidget, QLabel, QPushButton, 
                             QVBoxLayout, QHBoxLayout, QMenu, QMenuBar, 
                             QStatusBar, QToolBar)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction, QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # 设置窗口标题和大小
        self.setWindowTitle("Wwise UI (PySide6)")
        self.setMinimumSize(1200, 800)
        
        # 设置中央窗口部件
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        # 创建布局
        self.central_layout = QVBoxLayout(self.central_widget)
        
        # 创建标签
        self.label = QLabel("欢迎使用Wwise UI (PySide6版本)")
        self.label.setAlignment(Qt.AlignCenter)
        self.central_layout.addWidget(self.label)
        
        # 创建菜单栏
        self.create_menu_bar()
        
        # 创建工具栏
        self.create_tool_bar()
        
        # 创建状态栏
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage("就绪")
    
    def create_menu_bar(self):
        """创建菜单栏"""
        self.menu_bar = self.menuBar()
        
        # 创建文件菜单
        file_menu = QMenu("文件(&F)", self)
        self.menu_bar.addMenu(file_menu)
        
        exit_action = QAction("退出(&Q)", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # 创建视图菜单
        view_menu = QMenu("视图(&V)", self)
        self.menu_bar.addMenu(view_menu)
        
        # 创建窗口菜单
        window_menu = QMenu("窗口(&W)", self)
        self.menu_bar.addMenu(window_menu)
        
        # 创建帮助菜单
        help_menu = QMenu("帮助(&H)", self)
        self.menu_bar.addMenu(help_menu)
    
    def create_tool_bar(self):
        """创建工具栏"""
        self.tool_bar = QToolBar("主工具栏")
        self.tool_bar.setIconSize(QSize(32, 32))
        self.addToolBar(self.tool_bar)
        
        # 添加工具栏按钮
        self.tool_bar.addAction("详情")
        self.tool_bar.addAction("列表")
        self.tool_bar.addAction("事件") 