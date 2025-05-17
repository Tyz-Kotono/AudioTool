# main.py
import os
from Core.coll import collect_plugins
from Core.MenuCollector import process_plugin_menus
from Config.config import save_plugin_info, save_hook_list

def main():
    plugins = []
    for cls in collect_plugins():
        instance = cls()
        instance.draw()
        plugins.append(instance)

    ini_dir = os.path.join(os.path.dirname(__file__), "Config")
    os.makedirs(ini_dir, exist_ok=True)

    save_plugin_info(plugins, os.path.join(ini_dir, "Layout.ini"))

    hook_list = process_plugin_menus(plugins)
    save_hook_list(hook_list, os.path.join(ini_dir, "Hook.ini"))

if __name__ == "__main__":
    main()
