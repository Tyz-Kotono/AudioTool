import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QDockWidget, QWidget, 
    QTextEdit, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QToolBar, QMenu, QMenuBar, QStatusBar, QTreeWidget, QTreeWidgetItem,
    QTableWidget, QTableWidgetItem, QHeaderView, QComboBox
)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction, QIcon, QColor, QBrush


class AdvancedDockWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Wwise UI 可停靠窗口高级测试")
        self.setMinimumSize(1200, 800)
        
        # 设置中央部件
        self.central_widget = QTextEdit()
        self.central_widget.setPlainText("这是中央区域\n\n您可以：\n- 拖动四周的窗口到不同位置\n- 从窗口菜单切换窗口可见性\n- 右键窗口标题栏查看选项")
        self.setCentralWidget(self.central_widget)
        
        # 创建菜单栏
        self.create_menu_bar()
        
        # 创建工具栏
        self.create_tool_bar()
        
        # 创建停靠窗口
        self.create_dock_widgets()
        
        # 设置停靠窗口选项
        self.setDockOptions(
            QMainWindow.DockOption.AnimatedDocks | 
            QMainWindow.DockOption.AllowNestedDocks | 
            QMainWindow.DockOption.AllowTabbedDocks
        )
        
        # 创建状态栏
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage("准备就绪")
        
    def create_menu_bar(self):
        """创建菜单栏"""
        self.menu_bar = self.menuBar()
        
        # 文件菜单
        file_menu = QMenu("文件(&F)", self)
        self.menu_bar.addMenu(file_menu)
        
        exit_action = QAction("退出(&Q)", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # 视图菜单
        self.view_menu = QMenu("视图(&V)", self)
        self.menu_bar.addMenu(self.view_menu)
        
        # 窗口菜单
        self.window_menu = QMenu("窗口(&W)", self)
        self.menu_bar.addMenu(self.window_menu)
        
        # 帮助菜单
        help_menu = QMenu("帮助(&H)", self)
        self.menu_bar.addMenu(help_menu)
        
    def create_tool_bar(self):
        """创建工具栏"""
        self.tool_bar = QToolBar("主工具栏")
        self.tool_bar.setIconSize(QSize(24, 24))
        self.addToolBar(self.tool_bar)
        
        layout_combo = QComboBox()
        layout_combo.addItems(["默认布局", "宽屏布局", "紧凑布局", "调试布局"])
        layout_combo.currentIndexChanged.connect(self.change_layout)
        self.tool_bar.addWidget(layout_combo)
        
        detail_action = QAction("详情", self)
        detail_action.triggered.connect(lambda: self.toggle_dock_visibility(self.detail_dock))
        self.tool_bar.addAction(detail_action)
        
        list_action = QAction("列表", self)
        list_action.triggered.connect(lambda: self.toggle_dock_visibility(self.list_dock))
        self.tool_bar.addAction(list_action)
        
        event_action = QAction("事件", self)
        event_action.triggered.connect(lambda: self.toggle_dock_visibility(self.event_dock))
        self.tool_bar.addAction(event_action)
        
    def create_dock_widgets(self):
        """创建所有停靠窗口"""
        # 详情窗口
        self.detail_dock = self.create_detail_dock()
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.detail_dock)
        
        # 列表窗口
        self.list_dock = self.create_list_dock()
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.list_dock)
        
        # 事件窗口
        self.event_dock = self.create_event_dock()
        self.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, self.event_dock)
        
        # 添加到窗口菜单
        self.window_menu.addAction(self.detail_dock.toggleViewAction())
        self.window_menu.addAction(self.list_dock.toggleViewAction())
        self.window_menu.addAction(self.event_dock.toggleViewAction())
        
    def create_detail_dock(self):
        """创建详情窗口"""
        dock = QDockWidget("详情", self)
        dock.setAllowedAreas(Qt.DockWidgetArea.AllDockWidgetAreas)
        
        # 设置窗口特性
        dock.setFeatures(
            QDockWidget.DockWidgetFeature.DockWidgetClosable |
            QDockWidget.DockWidgetFeature.DockWidgetMovable |
            QDockWidget.DockWidgetFeature.DockWidgetFloatable
        )
        
        # 创建内容
        content = QWidget()
        layout = QVBoxLayout(content)
        
        # 创建属性树
        tree = QTreeWidget()
        tree.setHeaderLabels(["属性", "值"])
        tree.setColumnWidth(0, 150)
        layout.addWidget(tree)
        
        # 添加示例属性
        basic_group = QTreeWidgetItem(tree, ["基本信息"])
        QTreeWidgetItem(basic_group, ["名称", "示例项目"])
        QTreeWidgetItem(basic_group, ["ID", "12345"])
        QTreeWidgetItem(basic_group, ["路径", "/项目/音频/示例"])
        
        audio_group = QTreeWidgetItem(tree, ["音频属性"])
        QTreeWidgetItem(audio_group, ["格式", "WAV"])
        QTreeWidgetItem(audio_group, ["声道", "立体声"])
        QTreeWidgetItem(audio_group, ["采样率", "44100 Hz"])
        
        basic_group.setExpanded(True)
        audio_group.setExpanded(True)
        
        dock.setWidget(content)
        return dock
    
    def create_list_dock(self):
        """创建列表窗口"""
        dock = QDockWidget("列表", self)
        dock.setAllowedAreas(Qt.DockWidgetArea.AllDockWidgetAreas)
        
        # 设置窗口特性
        dock.setFeatures(
            QDockWidget.DockWidgetFeature.DockWidgetClosable |
            QDockWidget.DockWidgetFeature.DockWidgetMovable |
            QDockWidget.DockWidgetFeature.DockWidgetFloatable
        )
        
        # 创建内容
        content = QWidget()
        layout = QVBoxLayout(content)
        
        # 创建树状视图
        tree = QTreeWidget()
        tree.setHeaderLabels(["名称", "类型", "大小"])
        tree.setColumnWidth(0, 200)
        layout.addWidget(tree)
        
        # 添加示例项目
        for i in range(5):
            item = QTreeWidgetItem(tree, [f"项目 {i+1}", "文件夹", "-"])
            for j in range(3):
                QTreeWidgetItem(item, [f"子项目 {i+1}-{j+1}", "音频文件", f"{(j+1)*100} KB"])
        
        dock.setWidget(content)
        return dock
    
    def create_event_dock(self):
        """创建事件窗口"""
        dock = QDockWidget("事件", self)
        dock.setAllowedAreas(Qt.DockWidgetArea.AllDockWidgetAreas)
        
        # 设置窗口特性
        dock.setFeatures(
            QDockWidget.DockWidgetFeature.DockWidgetClosable |
            QDockWidget.DockWidgetFeature.DockWidgetMovable |
            QDockWidget.DockWidgetFeature.DockWidgetFloatable
        )
        
        # 创建内容
        content = QWidget()
        layout = QVBoxLayout(content)
        
        # 创建表格
        table = QTableWidget(10, 3)
        table.setHorizontalHeaderLabels(["时间", "类型", "内容"])
        layout.addWidget(table)
        
        # 调整列宽
        header = table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        
        # 添加示例事件
        event_types = ["信息", "警告", "错误"]
        event_contents = ["项目已加载", "无法加载音频文件", "用户请求了声音播放"]
        
        for i in range(10):
            event_type = event_types[i % len(event_types)]
            
            # 根据事件类型选择颜色
            if event_type == "信息":
                color = QColor(230, 255, 230)  # 浅绿色
            elif event_type == "警告":
                color = QColor(255, 255, 200)  # 浅黄色
            else:
                color = QColor(255, 230, 230)  # 浅红色
            
            time_item = QTableWidgetItem(f"14:0{i}")
            type_item = QTableWidgetItem(event_type)
            content_item = QTableWidgetItem(event_contents[i % len(event_contents)])
            
            brush = QBrush(color)
            time_item.setBackground(brush)
            type_item.setBackground(brush)
            content_item.setBackground(brush)
            
            table.setItem(i, 0, time_item)
            table.setItem(i, 1, type_item)
            table.setItem(i, 2, content_item)
        
        dock.setWidget(content)
        return dock
    
    def toggle_dock_visibility(self, dock):
        """切换停靠窗口可见性"""
        dock.setVisible(not dock.isVisible())
    
    def change_layout(self, index):
        """改变布局配置"""
        # 首先移除所有停靠窗口
        self.removeDockWidget(self.detail_dock)
        self.removeDockWidget(self.list_dock)
        self.removeDockWidget(self.event_dock)
        
        # 确保所有窗口可见
        self.detail_dock.setVisible(True)
        self.list_dock.setVisible(True)
        self.event_dock.setVisible(True)
        
        if index == 0:  # 默认布局
            self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.detail_dock)
            self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.list_dock)
            self.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, self.event_dock)
        
        elif index == 1:  # 宽屏布局
            self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.detail_dock)
            self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.list_dock)
            self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.event_dock)
            self.splitDockWidget(self.list_dock, self.event_dock, Qt.Orientation.Vertical)
        
        elif index == 2:  # 紧凑布局
            self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.detail_dock)
            self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.list_dock)
            self.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, self.event_dock)
            self.splitDockWidget(self.detail_dock, self.list_dock, Qt.Orientation.Vertical)
        
        elif index == 3:  # 调试布局
            self.addDockWidget(Qt.DockWidgetArea.TopDockWidgetArea, self.detail_dock)
            self.addDockWidget(Qt.DockWidgetArea.TopDockWidgetArea, self.list_dock)
            self.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, self.event_dock)
            self.splitDockWidget(self.detail_dock, self.list_dock, Qt.Orientation.Horizontal)
        
        self.statusBar.showMessage(f"已切换到布局 {index+1}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')  # 设置应用程序样式
    
    window = AdvancedDockWindow()
    window.show()
    
    sys.exit(app.exec()) 