from PySide6.QtWidgets import (
    QLabel, QVBoxLayout, QTreeView, QHeaderView, 
    QLineEdit, QHBoxLayout, QWidget, QAbstractItemView
)
from PySide6.QtCore import Qt, QSortFilterProxyModel, QModelIndex
from PySide6.QtGui import QAction, QStandardItemModel, QStandardItem

from dock_widget_base import DockWidgetBase


class ListDock(DockWidgetBase):
    """列表窗口类"""
    
    def __init__(self, parent=None):
        super().__init__(parent, "列表")
        
        # 创建窗口内容
        self.setup_ui()
        
        # 添加工具栏按钮
        self.add_toolbar_actions()
    
    def setup_ui(self):
        """设置UI组件"""
        # 创建搜索栏
        search_container = QWidget()
        search_layout = QHBoxLayout(search_container)
        search_layout.setContentsMargins(0, 0, 0, 0)
        
        search_label = QLabel("搜索:")
        self.search_edit = QLineEdit()
        self.search_edit.setPlaceholderText("输入搜索关键词...")
        self.search_edit.textChanged.connect(self.filter_items)
        
        search_layout.addWidget(search_label)
        search_layout.addWidget(self.search_edit)
        
        self.layout.addWidget(search_container)
        
        # 创建树形视图
        self.tree_view = QTreeView()
        self.tree_view.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tree_view.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tree_view.setAlternatingRowColors(True)
        self.tree_view.setSortingEnabled(True)
        self.tree_view.setUniformRowHeights(True)
        self.layout.addWidget(self.tree_view)
        
        # 创建模型
        self.source_model = QStandardItemModel()
        self.source_model.setHorizontalHeaderLabels(["名称", "类型", "大小", "修改日期"])
        
        # 创建过滤代理模型
        self.proxy_model = QSortFilterProxyModel()
        self.proxy_model.setSourceModel(self.source_model)
        self.proxy_model.setFilterCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.proxy_model.setFilterKeyColumn(-1)  # 在所有列上进行过滤
        
        # 将代理模型设置到视图
        self.tree_view.setModel(self.proxy_model)
        
        # 调整列宽
        header = self.tree_view.header()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        
        # 添加示例数据
        self.add_sample_data()
    
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
    
    def add_sample_data(self):
        """添加示例数据"""
        # 添加一些根项
        for i in range(3):
            root_item = QStandardItem(f"项目 {i+1}")
            type_item = QStandardItem("文件夹")
            size_item = QStandardItem("-")
            date_item = QStandardItem("2023-05-17")
            
            self.source_model.appendRow([root_item, type_item, size_item, date_item])
            
            # 为每个根项添加子项
            for j in range(5):
                child_item = QStandardItem(f"子项 {i+1}-{j+1}")
                child_type = QStandardItem("音频文件")
                child_size = QStandardItem(f"{(j+1) * 100} KB")
                child_date = QStandardItem("2023-05-17")
                
                root_item.appendRow([child_item, child_type, child_size, child_date])
    
    def filter_items(self, text):
        """根据输入文本过滤项目"""
        self.proxy_model.setFilterFixedString(text)
    
    def refresh_view(self):
        """刷新视图"""
        # 这里可以添加刷新逻辑
        pass
    
    def expand_all(self):
        """展开所有节点"""
        self.tree_view.expandAll()
    
    def collapse_all(self):
        """折叠所有节点"""
        self.tree_view.collapseAll() 