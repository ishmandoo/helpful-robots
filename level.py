from objects import Wall, Goal, Bomb
from variable import Variable
import copy

class Level:
    def __init__(self, name, w, h):
        self.name = name
        self.robots = []
        self.objects = {}
        self.vars = {}
        self.w = w
        self.h = h
        self.complete = False


    def win(self):
        self.complete = True
    
    def add_robot(self, robot):
        robot.level = self
        self.robots.append(robot)

    def add_object(self, obj):
        obj.level = self
        self.objects[obj.pos] = obj

    def add_var(self, name):
        self.vars[name] = Variable(name)

    def is_blocked(self, pos):
        if pos in self.objects:
            obj = self.objects[pos]
            return obj.is_blocking()
        return False

    def is_pushable(self, pos):
        if pos in self.objects:
            obj = self.objects[pos]
            return obj.pushable
        return False

    def object_at(self, pos):
        if pos in self.objects:
            print("no obj")
            obj = self.objects[pos]
            return obj
        return None
                    

    def run_command(self, com):
        for robot in self.robots:
            robot.run_command(com, self)
            '''
            if (robot.x, robot.y) in self.objects:
                obj = self.objects[(robot.x, robot.y)]
                if isinstance(obj, Wall):
                    robot.reset_to_last()
                elif isinstance(obj, Bomb):
                    robot.die()
                    obj.die()
            '''
