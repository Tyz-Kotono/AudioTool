from PySide6.QtWidgets import QDockWidget, QWidget, QVBoxLayout, QLabel, QToolBar, QMenu
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction


class DockWidgetBase(QDockWidget):
    """所有可停靠窗口的基类"""
    
    def __init__(self, parent=None, title=""):
        super().__init__(title, parent)
        
        # 设置停靠窗口的属性
        self.setFeatures(
            QDockWidget.DockWidgetFeature.DockWidgetClosable |
            QDockWidget.DockWidgetFeature.DockWidgetMovable |
            QDockWidget.DockWidgetFeature.DockWidgetFloatable
        )
        
        # 允许停靠在所有区域
        self.setAllowedAreas(
            Qt.DockWidgetArea.AllDockWidgetAreas
        )
        
        # 创建窗口内容
        self.content_widget = QWidget()
        self.layout = QVBoxLayout(self.content_widget)
        self.layout.setContentsMargins(2, 2, 2, 2)
        self.setWidget(self.content_widget)
        
        # 创建工具栏
        self.toolbar = QToolBar()
        self.layout.addWidget(self.toolbar)
        
        # 创建上下文菜单
        self.context_menu = QMenu(self)
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_context_menu)
        
        # 创建浮动操作
        float_action = QAction("浮动", self)
        float_action.triggered.connect(self.toggle_floating)
        self.context_menu.addAction(float_action)
        
        # 创建水平/垂直拆分操作
        split_h_action = QAction("水平拆分", self)
        split_h_action.triggered.connect(self.split_horizontal)
        self.context_menu.addAction(split_h_action)
        
        split_v_action = QAction("垂直拆分", self)
        split_v_action.triggered.connect(self.split_vertical)
        self.context_menu.addAction(split_v_action)
    
    def toggle_floating(self):
        """切换浮动状态"""
        self.setFloating(not self.isFloating())
    
    def split_horizontal(self):
        """水平拆分"""
        # 这里需要主窗口的支持，暂时作为占位符
        pass
    
    def split_vertical(self):
        """垂直拆分"""
        # 这里需要主窗口的支持，暂时作为占位符
        pass
    
    def show_context_menu(self, pos):
        """显示上下文菜单"""
        self.context_menu.exec_(self.mapToGlobal(pos)) 