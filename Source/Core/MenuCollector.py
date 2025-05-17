# Core/MenuCollector.py
from typing import List

def process_plugin_menus(plugin_instances: List[object]):
    hook_entries = []

    for plugin in plugin_instances:
        if hasattr(plugin, "GetMenuLists"):
            menu_data = plugin.GetMenuLists()
            hook = menu_data.get("hook")
            func = menu_data.get("Function")

            print(f"Hook: {hook}")
            if callable(func):
                func()

            hook_entries.append(hook)

    return hook_entries  # 返回给 Config 用于写入 Hook.ini
