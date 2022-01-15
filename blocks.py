from sprite import Sprite

class Question():

    def __init__(self, x, y):
        self.x = x
        self.y = y
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
       
    def update(self):
        pass

    def move(self, velocity: int):
        self.x += velocity


class Brick():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
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

    def update(self):
        pass

    def move(self, velocity: int):
        self.x += velocity



class Pipe:
    
    def __init__(self, x: int, y: int, current_phase: str):
        
        self.x = x
        self.y = y

        self.current_phase = current_phase
        
        if self.current_phase == "large":
            self.sprite = (0, 0, 200, 32, 56)
        if self.current_phase == "medium":
            self.sprite = (0, 32, 208, 32, 48)
        if self.current_phase == "small":
            self.sprite = (0, 64, 216, 32, 40)

        
    @property
    def w(self):
        return self.sprite[3]
    
    @property
    def h(self):
        return self.sprite[4]
    
    def update(self):
        pass

    def move(self, velocity: int):
        self.x += velocity

