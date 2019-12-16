import command
from util import Dir

class Robot:
    def __init__(self, x, y, dir=Dir.U):
        self.x = x
        self.y = y

    def run_command(self, com):
        pass

    def normal_move(self, dir):
        if dir == Dir.L:
            self.x -= 1
        if dir == Dir.R:
            self.x += 1
        if dir == Dir.U:
            self.y -= 1
        if dir == Dir.D:
            self.y += 1


class NormalRobot(Robot):
    def __init__(self, x, y):
        Robot.__init__(self, x, y)

    def run_command(self, com):
        print(com)
        if isinstance(com, command.Move):
            self.normal_move(com.dir)
