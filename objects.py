import pygame

class Obj:
    def __init__(self, pos):        
        self.pos = pos
        self.level = None
        self.alive = True
        self.holdable = False
        self.pushable = False
        self.blocks = False
        self.var_name = None
        self.image = None
        self.goal = False

    
    def front_pos(self):
        return self.pos + self.dir

    def die(self):
        self.alive = False

    def is_blocking(self):
        return self.blocks

    def get_image(self):
        return self.image

    def move(self, pos):
        del self.level.objects[self.pos]
        self.level.objects[pos] = self
        self.pos = pos
        print(self.pos, pos)

    def action(self):
        if self.goal:
            self.level.win()


class Wall(Obj):
    def __init__(self, pos):
        Obj.__init__(self, pos)
        self.image = pygame.transform.scale(pygame.image.load("assets/wall.png").convert_alpha(), (60, 60))
        self.blocks = True

class CondWall(Obj):
    def __init__(self, pos, var_name):
        Obj.__init__(self, pos)
        self.image_block = pygame.transform.scale(pygame.image.load("assets/wall.png").convert_alpha(), (60, 60))
        self.image_no_block = pygame.transform.scale(pygame.image.load("assets/wall_down.png").convert_alpha(), (60, 60))
        self.var_name = var_name
    
    def is_blocking(self):
        if self.var_name in self.level.vars:
            return self.level.vars[self.var_name].value
        else:
            raise ValueError('variable not found')
    
    def get_image(self):
        if self.var_name in self.level.vars:
            if self.level.vars[self.var_name].value:
                return self.image_block
            else:
                return self.image_no_block
        else:
            raise ValueError('variable not found')


class Goal(Obj):
    def __init__(self, pos):
        Obj.__init__(self, pos)
        self.image = pygame.transform.scale(pygame.image.load("assets/flag.png").convert_alpha(), (60, 60))
        self.goal = True
        self.blocks = True

class Bomb(Obj):
    def __init__(self, pos):
        Obj.__init__(self, pos)
        self.image = pygame.transform.scale(pygame.image.load("assets/bomb.jpg").convert_alpha(), (60, 60))

class HoldBox(Obj):
    def __init__(self, pos):
        Obj.__init__(self, pos)
        self.image = pygame.transform.scale(pygame.image.load("assets/box.png").convert_alpha(), (60, 60))
        self.holdable = True

class Box(Obj):
    def __init__(self, pos):
        Obj.__init__(self, pos)
        self.image = pygame.transform.scale(pygame.image.load("assets/box.png").convert_alpha(), (60, 60))
        self.pushable = True

class Switch(Obj):
    def __init__(self, pos, var_name):
        Obj.__init__(self, pos)
        self.image_off = pygame.transform.scale(pygame.image.load("assets/switch_off.png").convert_alpha(), (60, 60))
        self.image_on = pygame.transform.scale(pygame.image.load("assets/switch_on.png").convert_alpha(), (60, 60))
        self.var_name = var_name
        self.blocks = True
    
    def action(self):
        if self.var_name in self.level.vars:
            self.level.vars[self.var_name].toggle()
        else:
            raise ValueError('variable not found')

    def get_image(self):
        if self.var_name in self.level.vars:
            if self.level.vars[self.var_name].value:
                return self.image_on
            else:
                return self.image_off
        else:
            raise ValueError('variable not found')


