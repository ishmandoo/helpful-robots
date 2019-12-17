import command
from util import Dir, RelDir, Rot
import pygame

class Robot:
    def __init__(self, x, y, dir):
        self.x = x
        self.y = y
        self.dir = dir
        self.last_state = None # x, y, dir
        self.alive = True
        self.holder = False
        self.held = None
    
    def die(self):
        self.alive = False

    def reset_to_last(self):
        self.x, self.y, self.dir = self.last_state

    def run_command(self, com):
        self.last_state = self.x, self.y, self.dir

    def cardinal_move(self, dir):
        self.x, self.y = (self.x, self.y) + dir

    def relative_move(self, dir):
        self.cardinal_move(self.dir * dir)

    def rotate(self, dir):
        self.dir *= dir


class NormalRobot(Robot):
    def __init__(self, x, y, dir):
        Robot.__init__(self, x, y, dir)
        self.image = pygame.transform.scale(pygame.image.load("assets/robot.png").convert_alpha(), (60, 60))
        self.holder = True

    def run_command(self, com):
        Robot.run_command(self, com) # call the parent class run_command
        if isinstance(com, command.Move): # if this is a cardinal direction move (N,S,E,W)
            self.cardinal_move(com.dir) # move in the direction of the command
            self.dir = com.dir # rotate the robot to face this direction

        if isinstance(com, command.RelMove): # if it is a relative move (F,R)
            self.relative_move(com.dir)

        if isinstance(com, command.Rot): # if this is a rotation
            self.rotate(com.dir)

