# Config/config.py
import os
import configparser

def save_plugin_info(plugin_instances, output_path):
    ini = configparser.ConfigParser()
    for plugin in plugin_instances:
        section = plugin.info.get("name", plugin.__class__.__name__)
        ini[section] = {k: str(v) for k, v in plugin.info.items()}

    with open(output_path, "w", encoding="utf-8") as f:
        ini.write(f)
    print(f"Plugin layout written to: {output_path}")


def save_hook_list(hook_list, output_path):
    ini = configparser.ConfigParser()
    ini["Hooks"] = {f"hook_{i}": hook for i, hook in enumerate(hook_list)}

    with open(output_path, "w", encoding="utf-8") as f:
        ini.write(f)
    print(f"Hook list written to: {output_path}")
