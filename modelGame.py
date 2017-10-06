import arcade.key
D_UP = 1
D_RIGHT = 2
D_DOWN = 3
D_LEFT = 4
 
DIR_OFFSET = { D_UP: (0,1),
               D_RIGHT: (1,0),
               D_DOWN: (0,-1),
               D_LEFT: (-1,0) }
'''
class Model:
    def __init__(self, world, x, y, angle):
        self.world = world
        self.x = x
        self.y = y
        self.angle = 0
'''
class Wizard:
    WAIT = 0
    step = 6
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y

        self.wait_time = 0

        self.direction = D_RIGHT 
    def update(self, delta):
        self.wait_time += delta

        if self.wait_time < Wizard.WAIT:
            return
        
        self.x = (self.x + 5*DIR_OFFSET[self.direction][0])%self.world.width 
       
        '''
        if self.x >= self.world.width:
            self.x = 0
        elif self.x <= 0:
            self.x = width
        self.x += self.step
        '''
        self.wait_time = 0


class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.wizard = Wizard(self, 250, 130)
        #self.candy = Candy(self, 250, 300)

    def update(self, delta):
        self.wizard.update(delta)

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.RIGHT:
            self.wizard.direction = D_RIGHT
        elif key == arcade.key.LEFT:
            self.wizard.direction = D_LEFT
        elif key == arcade.key.UP:
            self.wizard.direction = D_UP #break!!
            #self.snake.direction = D_DOWN