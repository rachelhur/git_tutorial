class Add:
    def __init__(self, a:int, b:int):
        self.a = a
        self.b = b
    def __add__(self, a: int, b:int):
        return self.a + self.b
