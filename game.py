import pygame
pygame.font.init()
import time

from renderer import Renderer
from level import Level
from robot import Robot, NormalRobot, RelativeRobot, TestRobot
from util import Dir, RelDir, Rot, Command
from objects import Wall, Goal, Bomb, Box, Switch, CondWall
from levels import test_level, level_1, level_2

class Game:
    def __init__(self, w=900, h=600): # window width and height, width and height in number of tiles
        self.window = pygame.display.set_mode((w,h))
        self.clock = pygame.time.Clock()
        self.stopped = False
        self.levels = [
            level_1,
            level_2,
            test_level
            ]
        
        self.current_level = None
        self.current_level_builder = None

        for level in self.levels:
            self.current_level_builder = level
            self.start_level(level)
    
    def start_level(self, level, title=True):
        self.commands = []
        self.command_index = 0

        self.current_level = level.build()
        self.renderer = Renderer(self.current_level, self.window)
        
        if title:
            self.renderer.show_title()
        self.run()

    def run(self):
        while self.stopped == False:
            self.renderer.draw(self.commands, self.command_index)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()

                    if event.key == pygame.K_UP:
                        self.commands.append(Command.U)
                    if event.key == pygame.K_DOWN:
                        self.commands.append(Command.D)
                    if event.key == pygame.K_LEFT:
                        self.commands.append(Command.L)
                    if event.key == pygame.K_RIGHT:
                        self.commands.append(Command.R)
                    if event.key == pygame.K_SPACE:
                        self.commands.append(Command.A)
                        
                    if event.key == pygame.K_w:
                        self.current_level.run_command(Command.U)
                    if event.key == pygame.K_s:
                        self.current_level.run_command(Command.D)
                    if event.key == pygame.K_a:
                        self.current_level.run_command(Command.L)
                    if event.key == pygame.K_d:
                        self.current_level.run_command(Command.R)
                    if event.key == pygame.K_e:
                        self.current_level.run_command(Command.A)

                    if event.key == pygame.K_BACKSPACE:
                        self.commands = self.commands[:-1]


                    if event.key == pygame.K_RETURN:
                        for i, command in enumerate(self.commands):
                            self.current_level.run_command(command)
                            self.renderer.draw(self.commands, i)

                            pygame.time.delay(200)
                        if not self.current_level.complete:
                            self.start_level(self.current_level_builder, title=False)
                    
            if self.current_level.complete:
                return

            pygame.display.update()
            self.clock.tick(60)

if __name__ == '__main__':
    g = Game()
    