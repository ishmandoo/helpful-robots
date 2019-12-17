import pygame

class Obj:
    def __init__(self, x, y):        
        self.x = x
        self.y = y
        self.alive = True
    
    def die(self):
        self.alive = False

class Wall(Obj):
    def __init__(self, x, y):
        Obj.__init__(self, x, y)
        self.image = pygame.transform.scale(pygame.image.load("assets/wall.png").convert_alpha(), (60, 60))

class Goal(Obj):
    def __init__(self, x, y):
        Obj.__init__(self, x, y)
        self.image = pygame.transform.scale(pygame.image.load("assets/flag.png").convert_alpha(), (60, 60))

class Bomb(Obj):
    def __init__(self, x, y):
        Obj.__init__(self, x, y)
        self.image = pygame.transform.scale(pygame.image.load("assets/bomb.jpg").convert_alpha(), (60, 60))