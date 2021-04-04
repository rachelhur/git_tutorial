class Divide:
    """This is my branch. I will add a divide class"""
    def __init__(self, a:int, b:int):
        self.a = a
        self.b = b
    def __divide__(self, a:int, b:int):
        return self.a / self.b
