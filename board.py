class Board:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.robots = []
    
    def add_robot(self, robot):
        self.robots.append(robot)


if __name__  == '__main__':
    print(Board().board)