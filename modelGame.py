import arcade.key
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
    
class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.status = 0
        self.wizard = Wizard(self, 250, 100)
        
    
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
            
    
      
            
        