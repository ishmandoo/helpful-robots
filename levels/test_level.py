from level import Level
from robot import Robot, NormalRobot, RelativeRobot, TestRobot
from util import Dir, RelDir, Rot, Command
from objects import Wall, Goal, Bomb, Box, Switch, CondWall

def build():
        level = Level("Test Level", 10, 10)

        #level.add_robot(NormalRobot((1, 1), Dir.S))
        level.add_robot(TestRobot((3, 2), Dir.W))

        level.add_object(Wall((3,3)))
        level.add_object(Goal((5,3)))
        level.add_object(Bomb((4,4)))
        level.add_object(Box((3,4)))
        level.add_object(Box((3,4)))

        level.add_object(Switch((5,5), 'test'))
        level.add_object(CondWall((6,6), 'test'))
        level.add_var('test')

        return level