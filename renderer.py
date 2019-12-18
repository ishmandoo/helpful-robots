import pygame
import time

class Renderer:
    FONTSIZE = 30
    def __init__(self, level, window):
        self.level = level
        self.window = window

        w, h = window.get_size()

        self.dx = h//level.w
        self.dy = h//level.h

        self.font = pygame.font.SysFont('Comic Sans MS', Renderer.FONTSIZE)

    def show_title(self):
        self.window.fill((255,255,255))
        font = pygame.font.SysFont('Comic Sans MS', Renderer.FONTSIZE * 2)
        text = font.render(self.level.name, True, (0, 0, 0))
        self.window.blit(text, (0,0))    
        
        pygame.display.update()
        time.sleep(1)
        #pygame.time.delay(1000)

    def get_rect(self, pos):
        x_pix, y_pix = self.get_coords(pos)
        return (x_pix, y_pix, self.dx, self.dy)

    def get_coords(self, pos):
        x_pix = pos[0] * self.dx
        y_pix = pos[1] * self.dy
        return (x_pix, y_pix)

    def draw(self, commands, command_index):
        self.window.fill((255,255,255))

        for obj in self.level.objects.values():
            if obj.alive:
                self.window.blit(obj.get_image(), self.get_coords(obj.pos))
            
        for robot in self.level.robots:
            if robot.alive:
                #pygame.draw.rect(self.window, (0,0,0), self.get_rect(robot.x, robot.y))
                self.window.blit(pygame.transform.rotate(robot.image, (-robot.dir).angle()), self.get_coords(robot.pos))

        y = 0
        for i, command in enumerate(commands):
            text = str(command)
            text_surface = self.font.render(text, True, (0, 0, 0))
            self.window.blit(text_surface, dest=(620,y))

            if i == command_index:
                marker = ">"
                text_surface = self.font.render(marker, True, (0, 0, 0))
                self.window.blit(text_surface, dest=(600,y))

            y += Renderer.FONTSIZE
        
        
        pygame.display.update()