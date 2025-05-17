import importlib
import inspect
from pathlib import Path
import sys
from .Base import Base


def discover_subclasses():
    """发现所有继承自Base的子类"""
    subclasses = []
    base_dir = Path(__file__).parent

    # 遍历所有子目录
    for child in base_dir.iterdir():
        if child.is_dir() and not child.name.startswith('_'):
            module_name = f"{child.name}.Base"

            try:
                # 动态导入模块
                module = importlib.import_module(module_name)

                # 检查模块中的所有类
                for name, obj in inspect.getmembers(module, inspect.isclass):
                    if issubclass(obj, Base) and obj is not Base:
                        subclasses.append(obj)

            except ImportError as e:
                print(f"Warning: Could not import {module_name}: {e}")

    return subclasses


if __name__ == "__main__":
    # 示例用法
    all_subclasses = discover_subclasses()
    print(f"Found {len(all_subclasses)} subclasses:")

    for i, subclass in enumerate(all_subclasses, 1):
        print(f"{i}. {subclass.__name__} from {subclass.__module__}")

        # 实例化并运行
        instance = subclass()
        instance.run()