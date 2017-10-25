import arcade
from random import randint
from modelGame import World, Candy, Sweet, Bomb, Berry
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 620
Scaling = 0.4

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
        super().__init__(width, height,title = "Wizard Candy")
 
        self.background = None 
        self.background = arcade.load_texture('image/bg2.jpg')
        self.world = World(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.imagewiz = ['image/w3.png','image/left.png','image/right.png']
        self.wizard = ModelSprite(self.imagewiz[0],model=self.world.wizard)

        self.all_sprites_list = arcade.SpriteList()
        self.candy_list = arcade.SpriteList()
        self.sweet_list = arcade.SpriteList()
        self.bomb_list = arcade.SpriteList()
        self.berry_list = arcade.SpriteList()

        self.gameover = arcade.Sprite('image/gameover.png',0.8)
        self.gameover.set_position(SCREEN_WIDTH//2,SCREEN_HEIGHT//2)
        self.gameover_status = False
        
        for i in range(5):
            candy = Candy('image/candy.png',Scaling)
     
            self.all_sprites_list.append(candy)
            self.candy_list.append(candy)

        for i in range(1):
            sweet = Sweet('image/sweet.png',0.5)
    
            self.all_sprites_list.append(sweet)
            self.sweet_list.append(sweet)

        bomb = Bomb('image/bomb.png',0.05)

        self.all_sprites_list.append(bomb)
        self.bomb_list.append(bomb)

        berry = Berry('image/berry.png',0.5)
  
        self.all_sprites_list.append(berry)
        self.berry_list.append(berry)
    
        self.score = 0
    
    def update(self, delta):
        self.world.update(delta)
        self.wizard = ModelSprite(self.imagewiz[self.world.status],model=self.world.wizard)
        
        if not self.gameover_status :
            for candy in self.candy_list:
                if(candy.center_x-30<=self.world.wizard.x<=candy.center_x+30 and candy.center_y<=140):
                    
                    self.score += 1
                    candy.center_x = randint(SCREEN_HEIGHT,1200)
                    candy.center_y = randint(5,SCREEN_WIDTH-5)
      
            for sweet in self.sweet_list:
                if(sweet.center_x-30<=self.world.wizard.x<=sweet.center_x+30 and sweet.center_y<=140):
                    
                    self.score += 3
                    sweet.center_x = randint(SCREEN_HEIGHT,2000)
                    sweet.center_y = randint(5,SCREEN_WIDTH-5) 

            for berry in self.berry_list:
                if(berry.center_x-30<=self.world.wizard.x<=berry.center_x+30 and berry.center_y<=140):
                    Candy.Speed_Candy *= 2
                    Bomb.Speed_Bomb *= 1.5
                    self.score += 10
                    berry.center_x = randint(SCREEN_HEIGHT,2000)
                    berry.center_y = randint(5,SCREEN_WIDTH-5) 
            
            for bomb in self.bomb_list:
                if(bomb.center_x-30<=self.world.wizard.x<=bomb.center_x+30 and bomb.center_y<=140):
                    bomb.center_x = randint(SCREEN_HEIGHT,2000)
                    bomb.center_y = randint(5,SCREEN_WIDTH-5) 
                    self.gameover_status = True

            for sprite in self.all_sprites_list:
                sprite.update()

        self.Last_Score = self.score
    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.wizard.draw() 
        
        
        
        for sprite in self.all_sprites_list:
            sprite.draw()
        if self.gameover_status == False:
            output = "Score: {}".format(self.score)
            arcade.draw_text(output, 10, 20, arcade.color.WHITE, 16)

        elif self.gameover_status == True:
            self.gameover.draw()
            output = "Score: {}".format(self.Last_Score)
            arcade.draw_text(output, 10, 20, arcade.color.WHITE, 16)
            
    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key)
    def on_key_release(self, key, key_modifiers):
        self.world.on_key_release(key)

def main():
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()

if __name__ == '__main__':
    main()