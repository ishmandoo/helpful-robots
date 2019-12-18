from level import Level
from robot import Robot, NormalRobot, RelativeRobot, TestRobot
from util import Dir, RelDir, Rot, Command
from objects import Wall, Goal, Bomb, Box, Switch, CondWall

def build():
        level = Level("Level 1", 10, 10)

        #level.add_robot(NormalRobot((1, 1), Dir.S))
        level.add_robot(TestRobot((3, 2), Dir.W))

        level.add_object(Wall((0,2)))

        for i in range(9):
            level.add_object(Wall((i,1)))

        for i in range(6):
            level.add_object(Wall((i,3)))
        
        for i in range(3,9):
            level.add_object(Wall((8,i)))

        for i in range(3,9):
            level.add_object(Wall((6,i)))
        
        for i in range(1,9):
            level.add_object(Wall((9,i)))
        
        level.add_var('door')
        level.add_object(Switch((8,2), 'door'))

        level.add_object(CondWall((7,5), 'door'))

        level.add_object(Goal((7,7)))
        level.add_object(Wall((7,8)))
        return level