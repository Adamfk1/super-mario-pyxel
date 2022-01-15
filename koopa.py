# The Koopa class which inherits from the enemy class has everything there is to handle in
# The Koopa uses the collisions class.


from collisions import Collisions
import random
import pyxel


class Koopa():

    def __init__(self, x, y, alive, map, left, right):
        self.__x = x
        self.y = y
        self.__vx = 1
        self.map = map
        self.count_lives = 3
        self.collisions = Collisions(map)
        self.w = 16
        self.h = 24
        self.sprite = (0, 48, 32, self.w, self.h)


        self.hit_left = False
        self.hit_right = False

    @property
    def x(self):
        return self.__x

    def update(self):
        self.movement()

    def move(self, velocity: int):
        self.__x += velocity

    def movement(self):
        self.hit_wall_right()
        self.hit_wall_left()
        if self.hit_left:
            self.sprite = (0, 48, 32, self.w, self.h)
            self.__vx *= -1

        if self.hit_right:
            self.sprite = (0, 48, 32, -self.w, self.h)
            self.__vx *= -1

        if not self.sprite[2] == 120:
            self.__x += self.__vx

    def hit_wall_left(self):
        left = self.collisions.get_tile_type_at(self.x, self.y + 6)

        if left != 0:
            self.hit_left = True
            self.hit_right = False
        else:
            self.hit_left = False
            
    def hit_wall_right(self):
        right = self.collisions.get_tile_type_at(self.x + 16, self.y + 6)

        if right != 0:
            self.hit_right = True
            self.hit_left = False
        else:
            self.hit_right = False
