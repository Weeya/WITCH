import arcade
import arcade.key
from random import randint
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 620
SPEED = 5

class Wizard:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y

        self.delta_x = 0
    
    def move(self):
        self.x += self.delta_x
        if self.x < 0:
            self.x = self.world.width
        elif self.x > self.world.width:
            self.x = 0       
    
class Candy(arcade.Sprite):
    def reset_pos(self):
        self.center_y = randint(SCREEN_HEIGHT,1200)
        self.center_x = randint(5,SCREEN_WIDTH-5)
        #print(self.center_x)
    
    def update(self):
        self.center_y -= 2  #speed of candy
        if self.top < 0:
            self.reset_pos()

class Sweet(arcade.Sprite):
    def reset_pos(self):
        self.center_y = randint(SCREEN_HEIGHT,2000)
        self.center_x = randint(5,SCREEN_WIDTH-5)
    
    def update(self):
        self.center_y -= 4  #speed of sweet
        if self.top < 0:
            self.reset_pos()  

class Bomb(arcade.Sprite):
    def reset_pos(self):
        self.center_y = randint(SCREEN_HEIGHT,1000)
        self.center_x = randint(5,SCREEN_WIDTH-5)

    def update(self):
        self.center_y -= 3  #speed of bomb
        if self.top < 0:
            self.reset_pos()

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.status = 0
        self.wizard = Wizard(self, 250, 100)
        
        self.candy  = Candy        
        self.sweet = Sweet
        self.bomb = Bomb

    def update(self, delta):
        self.wizard.move()
    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.RIGHT:
            self.status = 2
            self.wizard.delta_x = SPEED
            
        elif key == arcade.key.LEFT:
            self.status = 1
            self.wizard.delta_x = -SPEED
    
    def on_key_release(self, key, key_modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.status = 0
            self.wizard.delta_x = 0
            
    
      
            
        