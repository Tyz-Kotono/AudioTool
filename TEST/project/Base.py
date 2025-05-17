from abc import ABC, abstractmethod


class Base(ABC):
    """抽象基类，所有子类必须实现run方法"""

    @abstractmethod
    def run(self):
        """子类必须实现的具体逻辑"""
        pass

    @classmethod
    def get_subclasses(cls):
        """获取所有直接子类"""
        return cls.__subclasses__()
