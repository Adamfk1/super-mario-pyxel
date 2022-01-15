# The Goomba class which inherits from the enemy class has everything there is to handle in
# The Goomba uses the collisions class.



from collisions import Collisions
import pyxel
import random


class Goomba():
    

    def __init__(self, x, y, alive, map):
        self.__x = x
        self.__y = y
        self.__vx = 1
        self.map = map
        
        self.collisions = Collisions(map)
        self.w = 16
        self.h = 16
        self.sprite = (0, 32, 48, self.w, self.h)
        self.count_lives = 1
        self.alive = alive
        self.hit_left = False
        self.hit_right = False
        
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    def update(self):
        self.movement()
        
    def move(self, velocity: int): 
       self.__x += velocity
    
    def movement(self):
        self.hit_wall_right()
        self.hit_wall_left()
        if self.hit_left:
            self.__vx *= -1

        if self.hit_right: 
            self.__vx *= -1
        
        self.__x += self.__vx
        

       
    def hit_wall_left(self):
        left = self.collisions.get_tile_type_at(self.x, self.y + 1)


        if left != 0:
            self.hit_left = True
            self.hit_right = False
        else:
            self.hit_left = False
            
       
    def hit_wall_right(self):
        right = self.collisions.get_tile_type_at(self.x + 16, self.y + 1)

        if right != 0:
            self.hit_right = True
            self.hit_left = False
        else:
            self.hit_right = False
            
