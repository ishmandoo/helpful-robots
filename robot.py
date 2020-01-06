#import command
from util import Dir, RelDir, Rot, Command
import pygame
from objects import Obj

class Robot(Obj):
    def __init__(self, pos, dir):
        print("init Robot")
        super().__init__(pos)
        self.dir = dir
        self.holder = False
        self.held_obj = None

    def reset_to_last(self):
        self.pos, self.dir = self.last_state
    
    def front_pos(self):
        return self.pos + self.dir

    def run_command(self, com, level):
        self.last_state = self.pos, self.dir
        
        if self.held_obj:
            self.held_obj.move(self.front_pos())

        if com == Command.A:
            print("action")
            obj_front = self.level.object_at(self.front_pos())
            if obj_front:
                obj_front.action()
    
    def cardinal_move(self, dir):
        new_pos = self.pos + dir
        if not self.level.is_blocked(new_pos):
            if self.held_obj:
                if not self.level.is_blocked(new_pos + dir):
                    self.pos = new_pos
            else:
                self.pos = new_pos

        obj_front = self.level.object_at(self.front_pos())
        if obj_front:
            pass
            # TODO: pushing objects
            #obj_front.cardinal_move(dir)

    def relative_move(self, dir):
        self.cardinal_move(self.dir * dir)

    def rotate(self, dir):
        new_dir = self.dir * dir
        if self.held_obj:
            if not self.level.is_blocked(self.pos + new_dir):
                self.dir = new_dir
        else:
            self.dir = new_dir

class HoldingRobot(Robot):
    def __init__(self, pos, dir):
        print("init Robot")
        super().__init__(pos, dir)
        self.image = pygame.transform.scale(pygame.image.load("assets/robot.png").convert_alpha(), (60, 60))
        self.holder = True

    def run_command(self, com, level):
        if com == Command.A:
            print("action")
            if self.held_obj:
                self.held_obj = None
                print("obj put down")
            else:
                obj_front = self.level.object_at(self.front_pos())
                print(obj_front)
                if obj_front:
                    if obj_front.holdable:
                        self.held_obj = obj_front
                        print("obj picked up")
        
        super().run_command(com, level) # call the parent class run_command

class NormalRobot(Robot):
    def __init__(self, pos, dir):
        print("init NormalRobot")
        super().__init__(pos, dir)
        self.image = pygame.transform.scale(pygame.image.load("assets/robot.png").convert_alpha(), (60, 60))

    def run_command(self, com, level):

        new_dir = None
        if com == Command.U:
            new_dir = Dir.N
        if com == Command.D:
            new_dir = Dir.S
        if com == Command.L:
            new_dir = Dir.W
        if com == Command.R:
            new_dir = Dir.E

        if new_dir:
            self.cardinal_move(new_dir)
            self.dir = new_dir
        
        super().run_command(com, level) # call the parent class run_command

class TestRobot(NormalRobot, HoldingRobot):
    def __init__(self, pos, dir):
        print("init TestRobot")
        super().__init__(pos, dir)

class RelativeRobot(Robot):
    def __init__(self, pos, dir):
        print("init RelativeRobot")
        super().__init__(pos, dir)
        self.image = pygame.transform.scale(pygame.image.load("assets/robot.png").convert_alpha(), (60, 60))
        self.holder = True

    def run_command(self, com, level):
        super().run_command(com, level) # call the parent class run_command

        if com == Command.U:
            self.relative_move(RelDir.F)
        if com == Command.D:
            self.relative_move(RelDir.R)
        if com == Command.L:
            self.rotate(Rot.CCW)
        if com == Command.R:
            self.rotate(Rot.CW)

