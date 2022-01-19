from sprite import Sprite

class Block():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self):
        pass

    def move(self, velocity: int):
        self.x += velocity

class Question(Block):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.phases = {
            "question_block": (16, 0, 16, 16),
            "solid_block": (16, 16, 16, 16),
            
            }
        
        self.sprites = Sprite(self.phases, "question_block")


    @property
    def w(self):
        return self.sprites.get_width()
    
    @property
    def h(self):
        return self.sprites.get_height()


class Brick(Block):
    
    def __init__(self, x, y):
        super().__init__(x, y)
        self.phases = {
            "brick_block": (0, 16, 16, 16),
            
            }
        
        self.sprites = Sprite(self.phases, "brick_block")

    @property
    def w(self):
        return self.sprites.get_width()
    
    @property
    def h(self):
        return self.sprites.get_height()


