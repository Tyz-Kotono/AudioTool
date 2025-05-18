import os
import sys
import importlib.util
import inspect
from Core.Root import PROJECT_ROOT  # 明确导入需要的变量
from Module.Build import ModuleRules


def load_modules_from_folder(folder_path, package_root=None):
    """从指定文件夹加载模块

    Args:
        folder_path: 要扫描的文件夹绝对路径
        package_root: 包根路径（用于生成模块名），如果为None则自动从PROJECT_ROOT计算
    """
    plugin_classes = []

    # 计算模块的基础包名（如果未指定）
    if package_root is None:
        package_root = os.path.relpath(folder_path, PROJECT_ROOT).replace(os.sep, ".")

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".py") and not file.startswith("__"):
                full_path = os.path.join(root, file)

                # 生成模块名（基于包根路径）
                rel_path = os.path.relpath(full_path, folder_path)
                module_name = f"{package_root}.{rel_path[:-3].replace(os.sep, '.')}"

                try:
                    spec = importlib.util.spec_from_file_location(module_name, full_path)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)

                    for name, obj in inspect.getmembers(module, inspect.isclass):
                        if (issubclass(obj, ModuleRules)
                                and obj is not ModuleRules
                                and obj.__module__ == module_name):
                            plugin_classes.append(obj)
                except Exception as e:
                    print(f"[Error] Failed to load {file}: {str(e)}")

    return plugin_classes


def collect_Modules():
    """收集所有插件模块"""
    module_folder = os.path.join(PROJECT_ROOT, "Module")
    return load_modules_from_folder(module_folder, "Module")


if __name__ == "__main__":
    Modules = collect_Modules()

    for cls in Modules:
        try:
            instance = cls()
            print(f"Loaded plugin: {cls.__name__}")
            print("Info:", instance.info)
            instance.Open()
        except Exception as e:
            print(f"[Error] Failed to initialize {cls.__name__}: {str(e)}")