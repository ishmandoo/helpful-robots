from enum import Enum

class Dir(Enum):
    N = 'N'
    S = 'S'
    E = 'E'
    W = 'W'

    def __str__(self):
        return str(self.value)

    def __mul__(self, other):
        if other == RelDir.F:
            return self
        if other == RelDir.R:
            return self.r()
        if other == Rot.CW:
            return self.cw()
        if other == Rot.CCW:
            return self.ccw()
    
    def __rmul__(self, other):
        return self.__mul__(other)

    def cw(self):
        if self == Dir.N:
            return Dir.E
        if self == Dir.S:
            return Dir.W
        if self == Dir.W:
            return Dir.N
        if self == Dir.E:
            return Dir.S

    def ccw(self):
        if self == Dir.N:
            return Dir.W
        if self == Dir.S:
            return Dir.E
        if self == Dir.W:
            return Dir.S
        if self == Dir.E:
            return Dir.N

    def r(self):
        if self == Dir.N:
            return Dir.S
        if self == Dir.S:
            return Dir.N
        if self == Dir.W:
            return Dir.E
        if self == Dir.E:
            return Dir.W


class Rot(Enum):
    CW = 'CW'
    CCW = 'CCW'

    def __str__(self):
        return str(self.value)

class RelDir(Enum):
    F = 'F'
    R = 'R'
    
    def __str__(self):
        return str(self.value)

class Const():
    pass