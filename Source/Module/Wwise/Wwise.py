from Module.Build import ModuleRules

class WwiseModule(ModuleRules):
    def __init__(self):
        super().__init__()
        self.info["name"] = "Wwise"

    def draw(self):
        print("Wwise drawing")

    def GetMenuLists(self):
        return {
            "hook": "Wwise",
            "Function": self.say_hello
        }

    def say_hello(self):
        print("Wwise Wappi Base")
