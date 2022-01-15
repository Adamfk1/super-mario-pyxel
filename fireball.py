import pyxel
from sprite import Sprite
from collisions import Collisions

class Fireball:
    def __init__(self, map):
        self.x = -10
        self.y = 0
        self.vx = 0
        self.vy = 0
        self.GRAVITY = 0.25
        self.B_SPD_X = 1.8
        self.B_SPD_Y = 1.5
        
        self.map = map
        self.collider = Collisions(map)
        
        self.phases = {"phase_one": (0, 144, 8, 8), "phase_two": (0, 152, 8, 8),\
            "phase_three": (8, 144, 8, 8), "phase_four": (8, 152, 8, 8),\
                "explode_one": (16, 144, 16, 16), "explode_two": (32, 144, 16, 16),\
                    "explode_three": (48, 144, 16, 16)}
        
        self.sprites = Sprite(self.phases, "phase_one")
        
    @property
    def w(self):
        return self.sprites.get_width()
    
    @property
    def h(self):
        return self.sprites.get_height() 
    
    def fire(self, x, y):
        self.x = x
        self.y = y
        self.vx = self.B_SPD_X
        self.vy = -self.B_SPD_Y
        

    def update_pve(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += self.GRAVITY
        self.sprites.set_current_phase("explode_one")

            
    def update_nve(self):
        self.x -= self.vx
        self.y += self.vy
        self.vy += self.GRAVITY
        self.sprites.set_current_phase("explode_three")


    def is_not_on_ground(self):
        
        left_foot = self.collider.get_tile_type_at(self.x, self.y + 15)

        if left_foot != (0, 0) and self.vy >= 0:
            return False
        else:
            return True
    
    def move(self, velocity):
        self.x += velocity

    def draw(self, mario):
        self.sprites.draw(mario.x, mario.y)



