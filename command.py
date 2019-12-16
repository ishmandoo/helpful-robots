from util import Dir

class Command:
    def __init__(self):
        pass

class Move(Command):
    def __init__(self, dir):
        self.dir = dir
    
    def __repr__(self):
        if self.dir == Dir.U:
            return "U"
        if self.dir == Dir.D:
            return "D"
        if self.dir == Dir.L:
            return "L"
        if self.dir == Dir.R:
            return "R"