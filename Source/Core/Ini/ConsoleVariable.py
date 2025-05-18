import configparser
import os

class ConsoleVariable:
    def __init__(self, filepath="Config/ConsoleVariable.ini"):
        self.filepath = filepath
        self.variables = {}
        self.load()

    def parse_value(self, value):
        value = value.strip().lower()
        if value in ['true', 'yes', 'on']:
            return True
        elif value in ['false', 'no', 'off']:
            return False
        try:
            if '.' in value:
                return float(value)
            return int(value)
        except ValueError:
            return value

    def load(self):
        if not os.path.exists(self.filepath):
            print(f"[ConsoleVariable] 配置文件未找到: {self.filepath}")
            return

        config = configparser.ConfigParser()
        config.read(self.filepath)

        if 'Startup' in config:
            for key, val in config['Startup'].items():
                self.variables[key.strip().lower()] = self.parse_value(val)

    def get(self, name, default=None):
        return self.variables.get(name.strip().lower(), default)

    def __contains__(self, name):
        return name.strip().lower() in self.variables

    def is_enabled(self, name):
        return bool(self.get(name, False))

# 单例接口
_instance = None
def get_global_cvars():
    global _instance
    if _instance is None:
        _instance = ConsoleVariable()
    return _instance
