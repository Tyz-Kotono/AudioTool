#Source\Core\PreBuild\PreBuildSystem.py

class PreBuildSystemModule:
    def __init__(self, engine):  # 接收 Engine 实例
        self.engine = engine     # 存储依赖
        self.PreBuild()



    def PreBuild(self):
        print("PreBuild executed")
