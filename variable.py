class Variable:
    def __init__(self, name):
        self.value = True
        self.name = name
    def toggle(self):
        print("toggle")
        self.value = not self.value