# 基于PySide6的可停靠窗口系统

本项目是原PyQt6应用程序的PySide6版本。

## 可用脚本

1. `test_pyside.py` - 简单的PySide6测试程序，显示一个按钮和标签
2. `main_pyside.py` - 主应用程序的简化版本
3. `dock_test.py` - 演示PySide6可停靠窗口的示例

## 如何运行

确保您已经安装PySide6：

```bash
pip install PySide6
```

然后运行任意测试脚本：

```bash
python test_pyside.py  # 简单测试
python main_pyside.py  # 主程序简化版
python dock_test.py    # 可停靠窗口测试
```

## PySide6与PyQt6主要区别

1. 导入方式不同：PySide6 vs PyQt6
2. 信号槽连接语法相似但有微小差异
3. PySide6使用Qt.AlignCenter而不是Qt.AlignmentFlag.AlignCenter
4. PySide6使用app.exec()而不是app.exec_()(在新版本中，PyQt6也可能使用app.exec())

## 可停靠窗口特性

- 支持拖拽
- 支持浮动
- 支持垂直/水平并列
- 支持窗口堆叠和标签化 