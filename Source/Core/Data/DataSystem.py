import os
import pprint
import configparser
import datetime
from enum import Enum
from typing import Dict
from Core.Root import PROJECT_ROOT

class ConfigFileType(Enum):
    MenuIni = "Menu.ini"
    ConsoleVariableIni = "ConsoleVariable.ini"
    LayoutIni = "Layout.ini"
    HookIni = "Hook.ini"
    MenuTreeIni = "MenuTree.ini"
    ModuleIni = "Module.ini"

class DataSystem:
    def __init__(self, config_folder_name: str = "Config"):
        """
        初始化配置系统，包括 Config 和 Logs 文件夹，并根据 ConsoleVariable.ini 配置决定是否创建日志文件。
        """
        self.config_folder_path = os.path.join(PROJECT_ROOT, config_folder_name)
        self.log_folder_path = os.path.join(PROJECT_ROOT, "Logs")
        self.file_map: Dict[ConfigFileType, str] = {}

        self._ensure_folder(self.config_folder_path)
        self._ensure_folder(self.log_folder_path)
        self._initialize_config_files()
        self._load_console_variables()

    def _ensure_folder(self, folder_path: str) -> None:
        """确保文件夹存在"""
        os.makedirs(folder_path, exist_ok=True)

    def _create_empty_file(self, path: str) -> None:
        """如果文件不存在则创建空文件"""
        if not os.path.exists(path):
            with open(path, "w", encoding="utf-8"):
                pass

    def _initialize_config_files(self) -> None:
        """创建并记录所有配置文件路径"""
        for config_type in ConfigFileType:
            path = os.path.join(self.config_folder_path, config_type.value)
            self.file_map[config_type] = path
            if config_type == ConfigFileType.ConsoleVariableIni:
                self._create_empty_file(path)

    def _load_console_variables(self) -> None:
        """从 ConsoleVariable.ini 读取日志配置，控制日志文件生成"""
        parser = configparser.ConfigParser()
        ini_path = self.file_map[ConfigFileType.ConsoleVariableIni]

        parser.read(ini_path, encoding="utf-8")
        startup = parser["Startup"] if "Startup" in parser else {}

        debug_enabled = startup.get("debug.enable", "true").lower() == "true"
        log_enabled = startup.get("log.enable", "true").lower() == "true"

        if debug_enabled:
            self.debug_log_path = os.path.join(self.log_folder_path, "Debug.log")
            self._create_empty_file(self.debug_log_path)
        else:
            self.debug_log_path = None

        if log_enabled:
            dt_str = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            self.log_path = os.path.join(self.log_folder_path, f"Log_{dt_str}.log")
            self._create_empty_file(self.log_path)
        else:
            self.log_path = None

    def GetFilePath(self, config_type: ConfigFileType) -> str:
        if config_type not in self.file_map:
            raise ValueError(f"{config_type.name} not initialized.")
        return self.file_map[config_type]

    def PrintAllFiles(self) -> None:
        pprint.pprint({k.name: v for k, v in self.file_map.items()})

    def GetAllFiles(self) -> Dict[ConfigFileType, str]:
        return self.file_map.copy()

    def Save_Plugin_Info(self, plugin_instances) -> None:
        ini = configparser.ConfigParser()
        for plugin in plugin_instances:
            section = plugin.info.get("name", plugin.__class__.__name__)
            ini[section] = {k: str(v) for k, v in plugin.info.items()}

        with open(self.GetFilePath(ConfigFileType.LayoutIni), "w", encoding="utf-8") as f:
            ini.write(f)

    def Save_Hook_List(self, hook_list) -> None:
        ini = configparser.ConfigParser()
        ini["Hooks"] = {f"hook_{i}": hook for i, hook in enumerate(hook_list)}

        with open(self.GetFilePath(ConfigFileType.HookIni), "w", encoding="utf-8") as f:
            ini.write(f)

    def GetLogFilePath(self, is_debug=False) -> str:
        return self.debug_log_path if is_debug else self.log_path

# 单例接口
_instance: DataSystem = None
def getsystem_data() -> DataSystem:
    global _instance
    if _instance is None:
        _instance = DataSystem()
    return _instance
