import pygame
from board import Board
from robot import Robot

class Game:
    def __init__(self, w=600, h=600, nw=10, nh=10): # window width and height, width and height in number of tiles
        self.window = pygame.display.set_mode((w,h))
        self.clock = pygame.time.Clock()
        self.stopped = False

        self.board = Board(nw, nh)
        self.board.add_robot(Robot(1, 1))

        self.dx = w//nw
        self.dy = h//nh

        self.run()

    def get_rect(self, x, y):
        x_pix = x * self.dx
        y_pix = y * self.dy
        return (x_pix, y_pix, x_pix + self.dx, y_pix + self.dy)

    def draw(self):
        self.window.fill((255,255,255))
        for robot in self.board.robots:
            pygame.draw.rect(self.window, (0,0,0), self.get_rect(robot.x, robot.y))

    def run(self):
        while self.stopped == False:
            self.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    self.stopped = True

            pygame.display.update()
            self.clock.tick(60)

if __name__ == '__main__':
    Game()

    