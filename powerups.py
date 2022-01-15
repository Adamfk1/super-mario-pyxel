
class PowerUps:
    def __init__(self, x: int, y: int, w: int, h: int, type: str):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.type = type
        
    @property
    def sprite(self):
        if self.type == 'red_mushroom':
            return (0, 0, 88, self.w, self.h)
        elif self.type == 'flower':
            return (0, 16, 88, self.w, self.h)
        elif self.type == 'star':
            return (0, 32, 88, self.w, self.h)
        elif self.type == 'green_mushroom':
            return (0, 32, 40, self.w, self.h)
        elif self.type == None:
            pass

    def draw(self):
        pass
    
    def move(self, velocity):
        self.x += velocity        