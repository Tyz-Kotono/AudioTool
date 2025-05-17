# Core/coll.py
import os
import sys
import importlib.util
import inspect

# 添加项目根目录到 sys.path（便于跨文件夹 import）
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

from Module.Build import ModuleRules


def load_modules_from_folder(folder_path, package_root):
    plugin_classes = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".py") and not file.startswith("__"):
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, PROJECT_ROOT)
                module_name = rel_path[:-3].replace(os.sep, ".")  # 去掉 .py，转为模块路径

                # 动态加载模块
                spec = importlib.util.spec_from_file_location(module_name, full_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                # 查找 ModuleRules 子类
                for name, obj in inspect.getmembers(module, inspect.isclass):
                    if issubclass(obj, ModuleRules) and obj is not ModuleRules:
                        plugin_classes.append(obj)

    return plugin_classes



def collect_plugins():
    plugin_classes = []
    module_folder = os.path.join(PROJECT_ROOT, "Module")

    for root, dirs, files in os.walk(module_folder):
        for file in files:
            if file.endswith(".py") and not file.startswith("__"):
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, PROJECT_ROOT)
                module_name = rel_path[:-3].replace(os.sep, ".")

                spec = importlib.util.spec_from_file_location(module_name, full_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                for name, obj in inspect.getmembers(module, inspect.isclass):
                    if issubclass(obj, ModuleRules) and obj is not ModuleRules:
                        plugin_classes.append(obj)

    return plugin_classes



if __name__ == "__main__":
    module_folder = os.path.join(PROJECT_ROOT, "Module")
    plugins = load_modules_from_folder(module_folder, "Module")

    for cls in plugins:
        instance = cls()
        print(f"Loaded plugin: {cls.__name__}")
        print("Info:", instance.info)
        instance.draw()
