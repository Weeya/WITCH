import arcade
from random import randint
from modelGame import World
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 620
Scaling = 0.4
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
'''
class Snow:
    def __init__(self):
        self.x = 0
        self.y = 0
        
    def reset_pos(self):
        self.y = randint(SCREEN_HEIGHT, SCREEN_HEIGHT+100)
        self.x = randint(0,SCREEN_WIDTH)
''' 

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
 
        self.background = None 
        self.background = arcade.load_texture('image/bg2.jpg')
        self.world = World(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.imagewiz = ['image/w3.png','image/left.png','image/right.png']
        self.wizard = ModelSprite(self.imagewiz[0],model=self.world.wizard)
        
        self.all_sprites_list = None
        self.candy_list = None
        self.sweet_list = None
        self.bomb_list = None
        #self.snow_list = None
    
        self.score = 0
        
    def candy_falling(self):
        self.all_sprites_list = arcade.SpriteList()
        self.candy_list = arcade.SpriteList()
        self.sweet_list = arcade.SpriteList()
        self.bomb_list = arcade.SpriteList()

        for i in range(5):
            candy = Candy('image/candy.png',Scaling)
            candy.center_x = randint(10,SCREEN_WIDTH-10)
            candy.center_y = randint(1,SCREEN_HEIGHT)

            self.all_sprites_list.append(candy)
            self.candy_list.append(candy)
        
        for i in range(1):
            sweet = Sweet('image/sweet.png',0.5)
            sweet.center_x = randint(10,SCREEN_WIDTH-10)
            sweet.center_y = randint(600,SCREEN_HEIGHT)
    
            self.all_sprites_list.append(sweet)
            self.sweet_list.append(sweet)

        for i in range(1):
            bomb = Bomb('image/bomb.png',0.05)
            #bomb.center_x = randint(10,SCREEN_WIDTH-10)
            #bomb.center_y = randint(0,10)
    
            self.all_sprites_list.append(bomb)
            self.bomb_list.append(bomb)
    '''
    def start_falling(self):
        self.snow_list = []

        for i in range(50):
            snow = Snow()
            snow.x = randint(0,SCREEN_WIDTH)
            snow.y = randint(0,SCREEN_HEIGHT + 200)
            
            snow.size = randint(0,4)
            snow.speed = randint(20,40)

            self.snow_list.append(snow)
    '''
    def update(self, delta):
        self.world.update(delta)
        self.wizard = ModelSprite(self.imagewiz[self.world.status],model=self.world.wizard)
        self.all_sprites_list.update()
        '''
        if self.wizard.hit(self.candy,10):
            self.candy.random_location()
            self.score += 1
        '''
        if((Candy.center_x==self.world.wizard.x) and (Candy.center_y==self.world.wizard.y)):
            print(Candy.center_x)
        hit_list_candy = arcade.check_for_collision_with_list(self.wizard,self.candy_list)
        hit_list_sweet = arcade.check_for_collision_with_list(self.wizard,self.sweet_list)
        hit_list_bomb = arcade.check_for_collision_with_list(self.wizard,self.bomb_list)

        for candy in hit_list_candy:
            candy.reset_pos()
            self.score += 1
    
        for sweet in hit_list_sweet:
            sweet.reset_pos()
            self.score += 2
        
        for bomb in hit_list_bomb:
            bomb.reset_pos()
            print("in")
            if(self.score>=10):
                self.score -= 10
            elif(self.score-10<=0):
                self.score = 0

        '''
        for snow in self.snow_list:
            snow.y -= snow.speed * delta

            if snow.y < 0:
                snow.reset_pos()
        '''
        
    def on_draw(self):
        
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.wizard.draw() 
        
        self.all_sprites_list.draw()

        '''
        for snow in self.snow_list:
            arcade.draw_circle_filled(snow.x, snow.y,snow.size, arcade.color.WHITE)
        '''
        output = "Score: {}".format(self.score)
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 16)
        
    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)
    def on_key_release(self, key, key_modifiers):
        self.world.on_key_release(key, key_modifiers)

def main():
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    #window.start_falling()
    window.candy_falling()
    arcade.set_window(window)
    arcade.run()

if __name__ == '__main__':
    main()