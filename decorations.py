import pyxel
from sprite import Sprite

class Cloud:
    
    def __init__(self):
        
        self.__cloud = [(-10, 40), (80, 25), (40, 60)]

    @property
    def cloud(self):
        return self.__cloud
    
    def draw(self):
    
        # Draw Clouds
        offset = (pyxel.frame_count // 8) % 160
        for i in range(3):
            for x, y in self.__cloud:
                pyxel.blt(x + i * 180 - offset, y, 0, 0, 176, 48, 24, 12)
                

class Bush:
    
    def __init__(self):
            
        self.__bush = [[30, 224],[720, 224]]

        
    @property
    def bush(self):
        return self.__bush

    def draw(self):

        for bush in self.__bush:
            pyxel.blt(bush[0], bush[1], 0, 48, 184, 48, 16, 12)

    def move(self, velocity):
        for bush in self.__bush:
                bush[0] += velocity

