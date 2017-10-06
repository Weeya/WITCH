import arcade
import math
from random import randint
from modelGame import World
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 620
Scaling = 0.4
class Candy(arcade.Sprite):
    def reset_pos(self):
        self.center_y = randint(700,1000)
        self.center_x = randint(0,SCREEN_WIDTH)
        #self.center_y = randint(SCREEN_HEIGHT + 10,SCREEN_HEIGHT + 100)
        #self.center_x = randint(0,SCREEN_WIDTH)
    
    def update(self):
        
        self.center_y -= 2  #speed of candy
        if self.top < 0:
            self.reset_pos()  

class Snow:
    def __init__(self):
        self.x = 0
        self.y = 0
        
    def reset_pos(self):
        self.y = randint(SCREEN_HEIGHT, SCREEN_HEIGHT+100)
        self.x = randint(0,SCREEN_WIDTH)
        
class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)
 
        super().__init__(*args, **kwargs)
 
    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)
 
    def draw(self):
        self.sync_with_model()
        super().draw()

class GameWindow(arcade.Window):
    def __init__(self,width,height):
        super().__init__(width, height)
 
        arcade.set_background_color(arcade.color.BLACK)
        self.world = World(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.wizard = ModelSprite('image/w3.png',model=self.world.wizard)

        self.all_sprites_list = None
        self.candy_list = None
        self.snow_list = None
    
    def candy_falling(self):
        self.all_sprites_list = arcade.SpriteList()
        self.candy_list = arcade.SpriteList()

        for i in range(15):
            candy = Candy('image/candy.png',Scaling)
            candy.center_x = randint(0,SCREEN_WIDTH)
            candy.center_y = randint(100,SCREEN_HEIGHT)
    
            self.all_sprites_list.append(candy)
            self.candy_list.append(candy)

    def start_falling(self):
        self.snow_list = []

        for i in range(50):
            snow = Snow()
            snow.x = randint(0,SCREEN_WIDTH)
            snow.y = randint(0,SCREEN_HEIGHT + 200)
            
            snow.size = randint(0,4)
            snow.speed = randint(20,40)

            self.snow_list.append(snow)

    def update(self, delta):
        self.world.update(delta)
        self.all_sprites_list.update()
        for snow in self.snow_list:
            snow.y -= snow.speed * delta

            if snow.y < 0:
                snow.reset_pos()

    def on_draw(self):
        arcade.start_render()
        self.wizard.draw() 
        self.all_sprites_list.draw()
        for snow in self.snow_list:
            arcade.draw_circle_filled(snow.x, snow.y,snow.size, arcade.color.WHITE)
        
        #output = "Score: {}".format(self.score)
        #arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)
        
    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)

def main():
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.start_falling()
    window.candy_falling()
    arcade.set_window(window)
    arcade.run()

if __name__ == '__main__':
    main()