from Module.Build import ModuleRules
from .WwiseCore import main

class WwiseModule(ModuleRules):
    def __init__(self):
        super().__init__()
        self.info["name"] = "Wwise"

    def Open(self):
        main()

    def GetMenuLists(self):
        return {
            "hook": "Wwise",
            "Function": self.say_hello
        }

    def say_hello(self):
        print("Wwise Wappi Base")
