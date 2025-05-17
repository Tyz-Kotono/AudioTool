from PySide6.QtWidgets import (
    QLabel, QVBoxLayout, QTableWidget, QTableWidgetItem,
    QPushButton, QHBoxLayout, QWidget, QHeaderView
)
from PySide6.QtCore import Qt, QDateTime
from PySide6.QtGui import QAction, QColor, QBrush

from dock_widget_base import DockWidgetBase


class EventDock(DockWidgetBase):
    """事件窗口类"""
    
    def __init__(self, parent=None):
        super().__init__(parent, "事件")
        
        # 创建窗口内容
        self.setup_ui()
        
        # 添加工具栏按钮
        self.add_toolbar_actions()
    
    def setup_ui(self):
        """设置UI组件"""
        # 创建按钮区域
        button_container = QWidget()
        button_layout = QHBoxLayout(button_container)
        button_layout.setContentsMargins(0, 0, 0, 0)
        
        self.clear_button = QPushButton("清除")
        self.clear_button.clicked.connect(self.clear_events)
        
        button_layout.addWidget(self.clear_button)
        button_layout.addStretch()
        
        self.layout.addWidget(button_container)
        
        # 创建表格
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["时间", "类型", "来源", "描述"])
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.table.setAlternatingRowColors(True)
        self.layout.addWidget(self.table)
        
        # 调整列宽
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)
        
        # 添加示例事件
        self.add_sample_events()
    
    def add_toolbar_actions(self):
        """添加工具栏按钮"""
        refresh_action = QAction("刷新", self)
        refresh_action.triggered.connect(self.refresh_view)
        self.toolbar.addAction(refresh_action)
        
        export_action = QAction("导出", self)
        export_action.triggered.connect(self.export_events)
        self.toolbar.addAction(export_action)
    
    def add_sample_events(self):
        """添加示例事件"""
        event_types = ["信息", "警告", "错误"]
        event_sources = ["系统", "音频引擎", "用户操作"]
        event_descriptions = [
            "项目已加载",
            "无法加载音频文件",
            "用户请求了声音播放",
            "音频格式不支持",
            "项目已保存"
        ]
        
        # 添加10个示例事件
        for i in range(10):
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)
            
            # 随机选择事件类型和颜色
            event_type = event_types[i % len(event_types)]
            if event_type == "信息":
                color = QColor(230, 255, 230)  # 浅绿色
            elif event_type == "警告":
                color = QColor(255, 255, 200)  # 浅黄色
            else:
                color = QColor(255, 230, 230)  # 浅红色
            
            # 创建单元格项目
            time_item = QTableWidgetItem(
                QDateTime.currentDateTime().addSecs(-i * 3600).toString("yyyy-MM-dd hh:mm:ss")
            )
            type_item = QTableWidgetItem(event_type)
            source_item = QTableWidgetItem(event_sources[i % len(event_sources)])
            desc_item = QTableWidgetItem(event_descriptions[i % len(event_descriptions)])
            
            # 设置背景颜色
            brush = QBrush(color)
            time_item.setBackground(brush)
            type_item.setBackground(brush)
            source_item.setBackground(brush)
            desc_item.setBackground(brush)
            
            # 设置单元格
            self.table.setItem(row_position, 0, time_item)
            self.table.setItem(row_position, 1, type_item)
            self.table.setItem(row_position, 2, source_item)
            self.table.setItem(row_position, 3, desc_item)
    
    def add_event(self, event_type, source, description):
        """添加新事件"""
        row_position = 0
        self.table.insertRow(row_position)
        
        # 根据事件类型选择颜色
        if event_type == "信息":
            color = QColor(230, 255, 230)  # 浅绿色
        elif event_type == "警告":
            color = QColor(255, 255, 200)  # 浅黄色
        else:
            color = QColor(255, 230, 230)  # 浅红色
        
        # 创建单元格项目
        time_item = QTableWidgetItem(
            QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss")
        )
        type_item = QTableWidgetItem(event_type)
        source_item = QTableWidgetItem(source)
        desc_item = QTableWidgetItem(description)
        
        # 设置背景颜色
        brush = QBrush(color)
        time_item.setBackground(brush)
        type_item.setBackground(brush)
        source_item.setBackground(brush)
        desc_item.setBackground(brush)
        
        # 设置单元格
        self.table.setItem(row_position, 0, time_item)
        self.table.setItem(row_position, 1, type_item)
        self.table.setItem(row_position, 2, source_item)
        self.table.setItem(row_position, 3, desc_item)
    
    def clear_events(self):
        """清除所有事件"""
        self.table.setRowCount(0)
    
    def refresh_view(self):
        """刷新视图"""
        # 这里可以添加刷新逻辑
        pass
    
    def export_events(self):
        """导出事件"""
        # 这里可以添加导出逻辑
        pass 