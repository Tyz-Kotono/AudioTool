class A:
    def __init__(self):
        self.name = "A"
    
    def get_name(self):
        return self.name


class B(A):
    def __init__(self):
        super().__init__()
        self.name = "B"


class C(A):
    def __init__(self):
        super().__init__()
        self.name = "C"


class D(A):
    def __init__(self):
        super().__init__()
        self.name = "D"


class E(B):
    def __init__(self):
        super().__init__()
        self.name = "E"


class F(B):
    def __init__(self):
        super().__init__()
        self.name = "F" 