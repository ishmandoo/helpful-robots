class Board:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.robots = []
    
    def add_robot(self, robot):
        self.robots.append(robot)

    def run_command(self, com):
        for robot in self.robots:
            robot.run_command(com)


if __name__  == '__main__':
    print(Board().board)