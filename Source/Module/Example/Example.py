from Module.Build import ModuleRules

class PluginB(ModuleRules):
    def __init__(self):
        super().__init__()
        self.info["name"] = "Example"

    def Open(self):
        print("Example drawing")

    def GetMenuLists(self):
        return {
            "hook": "Example",
            "Function": self.say_hello
        }

    def say_hello(self):
        print("Hello from Example")
