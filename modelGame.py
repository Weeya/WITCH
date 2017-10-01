class Wizard:
    WAIT = 0.5
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y

        self.wait_time = 0
    def update(self, delta):
        self.wait_time += delta

        if self.wait_time < Wizard.WAIT:
            return
        
        if self.x >= self.world.width:
            self.x = 0
        elif self.x <= 0:
            self.x = width
        self.x += 3

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.wizard = Wizard(self, 250, 130)

    def update(self, delta):
        self.wizard.update(delta)
