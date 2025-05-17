from PySide6.QtWidgets import QLabel, QVBoxLayout, QTextEdit, QTreeWidget, QTreeWidgetItem
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QFont

from dock_widget_base import DockWidgetBase


class DetailDock(DockWidgetBase):
    """详情窗口类"""
    
    def __init__(self, parent=None):
        super().__init__(parent, "详情")
        
        # 创建窗口内容
        self.setup_ui()
        
        # 添加工具栏按钮
        self.add_toolbar_actions()
    
    def setup_ui(self):
        """设置UI组件"""
        # 创建属性树
        self.property_tree = QTreeWidget()
        self.property_tree.setHeaderLabels(["属性", "值"])
        self.property_tree.setColumnWidth(0, 150)
        self.layout.addWidget(self.property_tree)
        
        # 添加一些示例属性
        self.add_sample_properties()
        
        # 创建详细信息文本框
        self.details_text = QTextEdit()
        self.details_text.setReadOnly(True)
        self.details_text.setMinimumHeight(150)
        self.layout.addWidget(self.details_text)
        
        # 设置一些示例文本
        self.details_text.setText("这里显示详细信息...")
    
    def add_toolbar_actions(self):
        """添加工具栏按钮"""
        refresh_action = QAction("刷新", self)
        refresh_action.triggered.connect(self.refresh_view)
        self.toolbar.addAction(refresh_action)
        
        expand_action = QAction("展开全部", self)
        expand_action.triggered.connect(self.expand_all)
        self.toolbar.addAction(expand_action)
        
        collapse_action = QAction("折叠全部", self)
        collapse_action.triggered.connect(self.collapse_all)
        self.toolbar.addAction(collapse_action)
    
    def add_sample_properties(self):
        """添加示例属性"""
        # 基本信息组
        basic_group = QTreeWidgetItem(self.property_tree, ["基本信息"])
        basic_group.setExpanded(True)
        
        name_item = QTreeWidgetItem(basic_group, ["名称", "示例项目"])
        id_item = QTreeWidgetItem(basic_group, ["ID", "12345"])
        path_item = QTreeWidgetItem(basic_group, ["路径", "/项目/音频/示例"])
        
        # 音频属性组
        audio_group = QTreeWidgetItem(self.property_tree, ["音频属性"])
        audio_group.setExpanded(True)
        
        format_item = QTreeWidgetItem(audio_group, ["格式", "WAV"])
        channels_item = QTreeWidgetItem(audio_group, ["声道", "立体声"])
        sample_rate_item = QTreeWidgetItem(audio_group, ["采样率", "44100 Hz"])
        bit_depth_item = QTreeWidgetItem(audio_group, ["位深度", "16 bit"])
    
    def refresh_view(self):
        """刷新视图"""
        # 这里可以添加刷新逻辑
        pass
    
    def expand_all(self):
        """展开所有节点"""
        self.property_tree.expandAll()
    
    def collapse_all(self):
        """折叠所有节点"""
        self.property_tree.collapseAll() 