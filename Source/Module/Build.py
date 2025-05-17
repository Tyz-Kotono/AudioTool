# Module/base.py
from abc import ABC, abstractmethod

class ModuleRules(ABC):
    def __init__(self):
        self.info = {}  # 每个插件自己的信息字典

    @abstractmethod
    def draw(self):
        pass
