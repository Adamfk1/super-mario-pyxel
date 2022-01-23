import pyxel

class Debugger:
    
    def __init__(self, player):
        self.player = player
    
    def debug_transform(self):
        if pyxel.btnp(pyxel.KEY_B):
            self.player.y -= 8
            self.player.sprites.set_current_phase("big_mario_left")
        if pyxel.btnp(pyxel.KEY_V):
            self.player.y -= 8
            self.player.sprites.set_current_phase("fire_mario_left")
        if pyxel.btnp(pyxel.KEY_S):
            self.player.sprites.set_current_phase("small_mario_left")
            
    def debug_draw(self):
        
        if pyxel.btn(pyxel.KEY_1):
            pyxel.rectb(self.player.x, self.player.y, self.player.w, self.player.h, 0)   
                 
        if pyxel.btn(pyxel.KEY_2):
            if self.player.is_small():
                pyxel.circb(self.player.x, self.player.y + 17, 2, 0)
                pyxel.circb(self.player.x + 10, self.player.y + 17, 2, 0)
            elif self.player.is_big() or self.player.is_fire():
                pyxel.circb(self.player.x, self.player.y + 33, 2, 0)
                pyxel.circb(self.player.x + 16, self.player.y + 33, 2, 0)
                
        if pyxel.btn(pyxel.KEY_3):
            if self.player.is_small():
                pyxel.circb(self.player.x, self.player.y, 2, 0)
                pyxel.circb(self.player.x + 10, self.player.y, 2, 0)
            if self.player.is_big() or self.player.is_fire():
                pyxel.circb(self.player.x, self.player.y, 2, 0)
                pyxel.circb(self.player.x + 16, self.player.y, 2, 0)
                
        if pyxel.btn(pyxel.KEY_4):
            if self.player.is_small():
                pyxel.circb(self.player.x + 14, self.player.y + 13, 2, 0)
                pyxel.circb(self.player.x + 14, self.player.y, 2, 0)
            elif self.player.is_big() or self.player.is_fire():
                pyxel.circb(self.player.x + 16, self.player.y + 32, 2, 0)
                pyxel.circb(self.player.x + 16, self.player.y, 2, 0)
                
        if pyxel.btn(pyxel.KEY_5):
            if self.player.is_small():
                pyxel.circb(self.player.x, self.player.y + 13, 2, 0)
                pyxel.circb(self.player.x, self.player.y, 2, 0)
            elif self.player.is_big() or self.player.is_fire():
                pyxel.circb(self.player.x, self.player.y + 32, 2, 0)
                pyxel.circb(self.player.x, self.player.y, 2, 0)

    def update(self):
        self.debug_transform()
              
    def draw(self):
        self.debug_draw()