import command
from util import Dir, RelDir, Rot
import pygame

class Robot:
    def __init__(self, x, y, dir=-Dir.N):
        self.x = x
        self.y = y
        self.dir = dir

    def run_command(self, com):
        pass

    def normal_move(self, dir):
        if dir == Dir.W:
            self.x -= 1
        if dir == Dir.E:
            self.x += 1
        if dir == Dir.N:
            self.y -= 1
        if dir == Dir.S:
            self.y += 1


class NormalRobot(Robot):
    def __init__(self, x, y):
        Robot.__init__(self, x, y)
        self.image = pygame.transform.scale(pygame.image.load("assets/robot.png").convert_alpha(), (60, 60))

    def run_command(self, com):

        if isinstance(com, command.Move):
            self.normal_move(com.dir)
            self.dir = com.dir

        if isinstance(com, command.RelMove):
            print(self.dir * com.dir)
            self.normal_move(self.dir * com.dir)

        if isinstance(com, command.Rot):
            self.dir *= com.dir
