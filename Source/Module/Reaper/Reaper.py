from Module.Build import ModuleRules

class PluginB(ModuleRules):
    def __init__(self):
        super().__init__()
        self.info["name"] = "Reaper"

    def draw(self):
        print("Reaper drawing")

    def GetMenuLists(self):
        return {
            "hook": "Reaper",
            "Function": self.say_hello
        }

    def say_hello(self):
        print("Hello from Reaper")
