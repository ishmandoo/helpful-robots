from util import Dir

class Command:
    def __init__(self):
        pass

class Move(Command):
    def __init__(self, dir):
        self.dir = dir
    
    def __repr__(self):
        return "move " + str(self.dir)

class RelMove(Command):
    def __init__(self, dir):
        self.dir = dir
    
    def __repr__(self):
        return "relative move " + str(self.dir)


class Rot(Command):
    def __init__(self, dir):
        self.dir = dir
    
    def __repr__(self):
        return "rotation " + str(self.dir)