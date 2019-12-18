from objects import Wall, Goal, Bomb

class Board:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.robots = []
        self.objects = {}
    
    def add_robot(self, robot):
        self.robots.append(robot)

    def add_object(self, obj):
        self.objects[(obj.x, obj.y)] = obj

    def run_command(self, com):
        for robot in self.robots:
            robot.run_command(com)
            if (robot.x, robot.y) in self.objects:
                obj = self.objects[(robot.x, robot.y)]
                if isinstance(obj, Wall):
                    robot.reset_to_last()
                elif isinstance(obj, Bomb):
                    robot.die()
                    obj.die()
