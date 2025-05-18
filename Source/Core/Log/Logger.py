import os
import datetime
from Core.Data import getsystem_data

class LogLevel:
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"

# Markdown 风格颜色
LOG_COLORS = {
    LogLevel.DEBUG: "**🟦 DEBUG**",
    LogLevel.INFO: "**🟩 INFO**",
    LogLevel.WARNING: "**🟨 WARNING**",
    LogLevel.ERROR: "**🟥 ERROR**"
}

class BaseLogger:
    def __init__(self, is_debug=False):
        self.is_debug = is_debug
        self.log_file_path = getsystem_data().GetLogFilePath(is_debug=self.is_debug)
        self.enabled = self.log_file_path is not None

    def log(self, level: str, message: str):
        if not self.enabled:
            return

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        level_tag = LOG_COLORS.get(level, level)
        formatted = f"[{timestamp}] {level_tag}: {message}"

        # 控制台输出
        print(formatted)

        # 写入日志文件
        with open(self.log_file_path, "a", encoding="utf-8") as f:
            f.write(formatted + "\n")

    def debug(self, msg): self.log(LogLevel.DEBUG, msg)
    def info(self, msg): self.log(LogLevel.INFO, msg)
    def warning(self, msg): self.log(LogLevel.WARNING, msg)
    def error(self, msg): self.log(LogLevel.ERROR, msg)

# 两种日志实例
Log = BaseLogger(is_debug=False)
Debug = BaseLogger(is_debug=True)
