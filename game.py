import pygame
from board import Board
from robot import Robot, NormalRobot
import command
from util import Dir, RelDir, Rot

class Game:
    FONTSIZE = 30
    def __init__(self, w=900, h=600, nw=10, nh=10): # window width and height, width and height in number of tiles
        self.window = pygame.display.set_mode((w,h))
        self.clock = pygame.time.Clock()
        self.stopped = False

        self.board = Board(nw, nh)
        self.board.add_robot(NormalRobot(1, 1))

        self.dx = h//nw
        self.dy = h//nh

        pygame.font.init()
        self.font = pygame.font.SysFont('Comic Sans MS', Game.FONTSIZE)
        
        self.commands = []
        self.command_index = 0

        self.run()

    def get_rect(self, x, y):
        x_pix = x * self.dx
        y_pix = y * self.dy
        return (x_pix, y_pix, self.dx, self.dy)

    def draw(self):
        self.window.fill((255,255,255))
        for robot in self.board.robots:
            pygame.draw.rect(self.window, (0,0,0), self.get_rect(robot.x, robot.y))

        y = 0
        for i, command in enumerate(self.commands):
            text = str(command)
            text_surface = self.font.render(text, True, (0, 0, 0))
            self.window.blit(text_surface, dest=(620,y))

            if i == self.command_index:
                marker = ">"
                text_surface = self.font.render(marker, True, (0, 0, 0))
                self.window.blit(text_surface, dest=(600,y))

            y += Game.FONTSIZE

    def run(self):
        while self.stopped == False:
            self.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.stopped = True

                    if event.key == pygame.K_UP:
                        self.commands.append(command.Move(Dir.N))
                    if event.key == pygame.K_DOWN:
                        self.commands.append(command.Move(Dir.S))
                    if event.key == pygame.K_RIGHT:
                        self.commands.append(command.Move(Dir.E))
                    if event.key == pygame.K_LEFT:
                        self.commands.append(command.Move(Dir.W))

                        
                    if event.key == pygame.K_w:
                        self.commands.append(command.RelMove(RelDir.F))
                    if event.key == pygame.K_s:
                        self.commands.append(command.RelMove(RelDir.R))
                    if event.key == pygame.K_a:
                        self.commands.append(command.Rot(Rot.CCW))
                    if event.key == pygame.K_d:
                        self.commands.append(command.Rot(Rot.CW))


                    if event.key == pygame.K_SPACE:
                        if self.command_index < len(self.commands):
                            self.board.run_command(self.commands[self.command_index])
                            self.command_index += 1
                        else:
                            self.stopped = True
                    

            pygame.display.update()
            self.clock.tick(60)

if __name__ == '__main__':
    g = Game()
    