from .Logger import BaseLogger

Log = BaseLogger(is_debug=False)    # 写入 Log 文件（带时间戳）
Debug = BaseLogger(is_debug=True) 