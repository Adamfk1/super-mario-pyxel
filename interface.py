from mario import Mario
from tilemap import Map
from tilemap import Map
import pyxel


# The interface is where all code comes together and is drawn on the screen
class Interface:

    def __init__(self, w: int, h: int):
        self.width = w
        self.height = h

        self.death_counter = 0
        self.game_attempt = 0

        self.reset_game = False

        self.map = Map(0, 200)

    
        self.mario = Mario(20, 1, 3, self.map)


    def update(self):
        self.mario.update()
        self.map.update()


    def draw(self):
        pyxel.cls(0)

        self.map.draw()
        self.mario.draw()


        pyxel.mouse(True)

        
