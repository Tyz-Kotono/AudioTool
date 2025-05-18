from pprint import pprint

from Core.PreBuild import PreBuildSystemModule
from Core.Collector  import collect_Modules
from Core.Ini.ConsoleVariable import get_global_cvars

from typing import List
from Core.Log import Log, Debug

class EngineInstance:
    def __init__(self):

        self.Modules = []
        self.PreBuild()
        self.BeginPlayEngine()


    def PreBuild(self):
        PreBuildSystemModule(self)  # 存储为实例变量

    def BeginPlayEngine(self):
        CollectModules(self)


        # self.WriteIni()

    def WriteIni(self):
        pprint(self.Modules)

        # ⬇️ 修复这里：先处理出钩子列表
        # hook_list = process_plugin_menus(self.Modules)
        # self.dataSystem.Save_Hook_List(hook_list)
#region Module

def CollectModules(Engine):
    for Module in collect_Modules():
        instance = Module()
        instance.Open()
        Engine.Modules.append(instance)
    Log.info(Engine.Modules)



#endregion


