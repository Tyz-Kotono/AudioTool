# TestWindow - 可停靠窗口UI系统

这是基于PySide6的可停靠窗口UI系统的测试版本。

## 文件说明

- `main.py` - 主程序入口
- `main_window.py` - 主窗口类
- `dock_widget_base.py` - 所有可停靠窗口的基类
- `detail_dock.py` - 详情窗口类
- `list_dock.py` - 列表窗口类
- `event_dock.py` - 事件窗口类
- `requirements.txt` - 依赖需求文件

## 功能特性

- 窗口可以放在顶部或底部区域（支持多个并列或堆叠）
- 支持自由拖拽、浮动、小窗化
- 支持垂直并列
- 每个窗口类型都是单独的类

## 运行方法

确保已安装PySide6：

```bash
pip install -r requirements.txt
```

然后运行主程序：

```bash
python main.py
``` 