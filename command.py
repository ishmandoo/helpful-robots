class Command:
    def __init__(self):
        pass

class Move(Command):
    def __init__(self, dir):
        super.__init__()
        self.dir = dir