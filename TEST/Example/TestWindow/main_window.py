from PySide6.QtWidgets import (
    QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, 
    QHBoxLayout, QMenu, QMenuBar, QStatusBar, QToolBar
)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction, QIcon

from dock_widget_base import DockWidgetBase
from detail_dock import DetailDock
from list_dock import ListDock
from event_dock import EventDock


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # 设置窗口标题和大小
        self.setWindowTitle("Wwise UI")
        self.setMinimumSize(1200, 800)
        
        # 设置中央窗口部件
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        # 创建布局
        self.central_layout = QVBoxLayout(self.central_widget)
        
        # 创建菜单栏
        self.create_menu_bar()
        
        # 创建工具栏
        self.create_tool_bar()
        
        # 创建状态栏
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage("就绪")
        
        # 设置停靠窗口属性
        self.setDockOptions(
            QMainWindow.DockOption.AnimatedDocks |
            QMainWindow.DockOption.AllowNestedDocks |
            QMainWindow.DockOption.AllowTabbedDocks
        )
        
        # 创建并添加停靠窗口
        self.create_dock_widgets()
    
    def create_menu_bar(self):
        """创建菜单栏"""
        self.menu_bar = QMenuBar()
        self.setMenuBar(self.menu_bar)
        
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
        self.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.tool_bar)
        
        # 添加工具栏按钮
        self.tool_bar.addAction("详情")
        self.tool_bar.addAction("列表")
        self.tool_bar.addAction("事件")
    
    def create_dock_widgets(self):
        """创建所有停靠窗口"""
        # 创建详情窗口
        self.detail_dock = DetailDock(self)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.detail_dock)
        
        # 创建列表窗口
        self.list_dock = ListDock(self)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.list_dock)
        
        # 创建事件窗口
        self.event_dock = EventDock(self)
        self.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, self.event_dock) 