import os
import sys
import importlib.util
import inspect


# 自动定位Source为根目录
def find_source_root():
    """向上递归查找直到找到Source目录"""
    current = os.path.dirname(os.path.abspath(__file__))
    while True:
        if os.path.basename(current) == "Source":
            return current
        parent = os.path.dirname(current)
        if parent == current:  # 到达文件系统根目录
            raise RuntimeError("Source directory not found in parent paths")
        current = parent

# 设置项目根目录
PROJECT_ROOT = find_source_root()
sys.path.insert(0, PROJECT_ROOT)