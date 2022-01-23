

import time
import pyxel
from fireball import Fireball
from collisions import Collisions
from sprite import Sprite
from debuggers import Debugger

class Mario():

    def __init__(self, x: int, y: int, velocity: int, map):
        
        self.x = x
        self.y = y
        self.vx = velocity
        self.vy = 0


        self.map = map
        self.collider = Collisions(self.map)

        
        self.phases = {
            
            "small_mario_right": (64, 64, 16, 16),
            "small_mario_run_right_1": (64, 32, 14, 16),
            "small_mario_run_right_2": (64, 0, 16, 16),
            "small_mario_run_right_3": (64, 48, 16, 16),
            "small_mario_jump_right": (64, 16, 16, 16),
            
            "small_mario_left": (80, 64, 16, 16),
            "small_mario_run_left_1": (80, 32, 14, 16),
            "small_mario_run_left_2": (80, 0, 16, 16),
            "small_mario_run_left_3": (80, 48, 16, 16),
            "small_mario_jump_left": (80, 16, 16, 16),
            
            "small_mario_die": (64, 80, 16, 16),

            "big_mario_right": (112, 0, 16, 32),
            "big_mario_run_right_1": (),
            "big_mario_run_right_2": (),
            "big_mario_run_right_3": (),
            "big_mario_jump_right": (),

            "big_mario_left": (96, 0, 16, 32),
            "big_mario_run_left_1": (),
            "big_mario_run_left_2": (),
            "big_mario_run_left_3": (),
            "big_mario_jump_left": (),
            
            "fire_mario_right": (144, 0, 16, 32),
            "fire_mario_run_right_1": (),
            "fire_mario_run_right_2": (),
            "fire_mario_run_right_3": (),
            "fire_mario_jump_right": (),

            "fire_mario_left": (128, 0, 16, 32),
            "fire_mario_run_left_1": (),
            "fire_mario_run_left_2": (),
            "fire_mario_run_left_3": (),
            "fire_mario_jump_left": (),
        
            "big_mario_duck": (),
            "fire_mario_duck": (),

            }
        
        
        self.sprites = Sprite(self.phases, "small_mario_right")

        self.debugger = Debugger(self)

        self.score = 0
        
        self.jump_speed = -8
        self.gravity = 0.4

        self.fireballs = []
        
        self.left_movement_counter = 1
        self.right_movement_counter = 1


    @property
    def w(self):
        return self.sprites.get_width()
    
    @property
    def h(self):
        return self.sprites.get_height()

    def move(self, velocity):
        self.x += velocity
        self.x = min(self.x, 238)
        self.x = max(self.x, 0)
        
    def entity_jump(self):
        self.vy = self.jump_speed

    def accelerate(self, gravity: int):
        self.vy += gravity
        self.y += self.vy      
        
    def move_x(self):
        
        if pyxel.btn(pyxel.KEY_RIGHT):
            if self.x < 230:
                self.running_animations(self.vx, \
                    ["small_mario_run_right_1", "small_mario_run_right_2", "small_mario_run_right_3"],\
                        ["big_mario_run_right_1", "big_mario_run_right_2", "big_mario_run_right_3"],\
                            ["fire_mario_run_right_1", "fire_mario_run_right_2", "fire_mario_run_right_3"])
            self.hit_wall_right()
                

            if self.x >= 230:
                self.running_animations(0, \
                    ["small_mario_run_right_1", "small_mario_run_right_2", "small_mario_run_right_3"],\
                        ["big_mario_run_right_1", "big_mario_run_right_2", "big_mario_run_right_3"],\
                            ["fire_mario_run_right_1", "fire_mario_run_right_2", "fire_mario_run_right_3"])     
                self.map.move(-3)
                for fireball in self.fireballs:
                    fireball.move(-3)

        elif pyxel.btn(pyxel.KEY_LEFT):
            self.running_animations(-self.vx, \
                ["small_mario_run_left_1", "small_mario_run_left_2", "small_mario_run_left_3"],\
                    ["big_mario_run_left_1", "big_mario_run_left_2", "big_mario_run_left_3"],\
                        ["fire_mario_run_left_1", "fire_mario_run_left_2", "fire_mario_run_left_3"])
            
            self.hit_wall_left()


        elif pyxel.btn(pyxel.KEY_DOWN):
            if self.is_big():
                self.sprites.set_current_phase("big_mario_duck")
            if self.is_fire():
                self.sprites.set_current_phase("fire_mario_duck")
    
    def move_y(self):
        if self.is_not_on_ground():
            self.accelerate(self.gravity)
            if self.is_small() and self.is_left():
                self.sprites.set_current_phase("small_mario_jump_left")
            if self.is_small() and self.is_right():
                self.sprites.set_current_phase("small_mario_jump_right")
            if not self.not_hit_head():
                mario_head = self.y
                self.vy = 0
                self.y = ((mario_head) - ((mario_head) % 16)) + self.h
            if not self.is_not_on_ground():
                if self.is_small() and self.is_left():
                    self.sprites.set_current_phase("small_mario_left")
                if self.is_small() and self.is_right():
                    self.sprites.set_current_phase("small_mario_right")    
        else:
            if self.is_small():
                mario_feet = self.y + 17
            if self.is_big() or self.is_fire():
                mario_feet = self.y + 33
            self.vy = 0
            self.y = ((mario_feet) - ((mario_feet) % 16)) - self.h
            if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_SPACE):
                self.entity_jump()
                
    def running_animations(self, velocity, small_phases: list, big_phases: list, fire_phases: list):
        
        if self.right_movement_counter == 1 or self.left_movement_counter == 1:
            self.move(velocity)
            if self.is_small():
                self.sprites.set_current_phase(small_phases[0])
            elif self.is_big():
                self.sprites.set_current_phase(big_phases[0])
            elif self.is_fire():
                self.sprites.set_current_phase(fire_phases[0])
        elif self.right_movement_counter == 5 or self.left_movement_counter == 5:
            self.move(velocity)
            if self.is_small():
                self.sprites.set_current_phase(small_phases[1])
            elif self.is_big():
                self.sprites.set_current_phase(big_phases[1])
            elif self.is_fire():
                self.sprites.set_current_phase(fire_phases[1])
        elif self.right_movement_counter == 10 or self.left_movement_counter == 10:
            self.move(velocity)
            if self.is_small():
                self.sprites.set_current_phase(small_phases[2])
            elif self.is_big():
                self.sprites.set_current_phase(big_phases[2])
            elif self.is_fire():
                self.sprites.set_current_phase(fire_phases[2])
        else:
            self.move(velocity)
            
        self.right_movement_counter += 1
        if self.right_movement_counter == 15:
            self.right_movement_counter = 1
        self.left_movement_counter += 1
        if self.left_movement_counter == 15:
            self.left_movement_counter = 1

    def is_not_on_ground(self):
        
        if self.is_small():
            left_foot = self.collider.get_tile_type_at(self.x, self.y + 17)
            right_foot = self.collider.get_tile_type_at(self.x + 10, self.y + 17)
        if self.is_big() or self.is_fire():
            left_foot = self.collider.get_tile_type_at(self.x, self.y + 33)
            right_foot = self.collider.get_tile_type_at(self.x + 14, self.y + 33)
        
        if self.collider.is_not_air_tile(left_foot, right_foot) and self.vy >= 0:
            return False
        else:
            return True

    def hit_wall_left(self):
        if self.is_small():
            left_bottom = self.collider.get_tile_type_at(self.x, self.y + 13)
            left_top = self.collider.get_tile_type_at(self.x, self.y)
        if self.is_big() or self.is_fire():
            left_bottom = self.collider.get_tile_type_at(self.x, self.y + 29)
            left_top = self.collider.get_tile_type_at(self.x, self.y)

        if self.collider.is_not_air_tile(left_bottom, left_top):
            self.x += 1
            self.hit_wall_left()
            
    def hit_wall_right(self):
        if self.is_small():
            right_bottom = self.collider.get_tile_type_at(self.x + 14, self.y + 13)
            right_top = self.collider.get_tile_type_at(self.x + 14, self.y)
        if self.is_big() or self.is_fire():
            right_bottom = self.collider.get_tile_type_at(self.x + 16, self.y + 29)
            right_top = self.collider.get_tile_type_at(self.x + 16, self.y)

        if self.collider.is_not_air_tile(right_bottom, right_top):
            self.x -= 1
            self.hit_wall_right()

    def not_hit_head(self):
        if self.is_small():
            right_head = self.collider.get_tile_type_at(self.x + 10, self.y)
            left_head = self.collider.get_tile_type_at(self.x, self.y)
        if self.is_big() or self.is_fire():
            right_head = self.collider.get_tile_type_at(self.x + 10, self.y)
            left_head = self.collider.get_tile_type_at(self.x, self.y)

        if self.collider.is_not_air_tile(right_head, left_head):
            return False
        else:
            return True

    def collide_above(self):
        mario_feet = self.y + self.h
        self.vy = 0
        self.y = ((mario_feet) - ((mario_feet) % 16)) - self.h
        if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_SPACE):
            self.entity_jump() 
        
    def collide_below(self, object):
        self.y = object.y + object.h
        self.vy = 0

    def collide_left(self):
        self.x += self.vx           
    
    def collide_right(self):
        self.x -= self.vx
                 
       
    def is_big(self):
        if self.sprites.current_phase in [ 
                self.phases['big_mario_left'],
                self.phases['big_mario_right'],                             
                self.phases['big_mario_run_right_1'],
                self.phases['big_mario_run_right_2'],
                self.phases['big_mario_run_right_3'], 
                self.phases['big_mario_run_left_1'],
                self.phases['big_mario_run_left_2'],
                self.phases['big_mario_run_left_3'],    
                self.phases['big_mario_jump_left'],
                self.phases['big_mario_jump_right'],
                self.phases['big_mario_duck']
            ]:
            return True
        
    def is_fire(self):
        if self.sprites.current_phase in [
                self.phases['fire_mario_left'],
                self.phases['fire_mario_right'],
                self.phases['fire_mario_run_right_1'],
                self.phases['fire_mario_run_right_2'],
                self.phases['fire_mario_run_right_3'],
                self.phases['fire_mario_run_left_1'],
                self.phases['fire_mario_run_left_2'],
                self.phases['fire_mario_run_left_3'],
                self.phases['fire_mario_jump_left'],
                self.phases['fire_mario_jump_right'],
                self.phases['fire_mario_duck']
            ]:
            return True
        
    def is_small(self):        
        if self.sprites.current_phase in [
                self.phases['small_mario_left'],
                self.phases['small_mario_right'],
                self.phases['small_mario_run_right_1'],
                self.phases['small_mario_run_right_2'],
                self.phases['small_mario_run_right_3'],
                self.phases['small_mario_run_left_1'],
                self.phases['small_mario_run_left_2'],
                self.phases['small_mario_run_left_3'],
                self.phases['small_mario_jump_left'],
                self.phases['small_mario_jump_right']
            ]:
            return True

    def is_left(self):
        if self.sprites.current_phase in [
                self.phases['small_mario_left'],
                self.phases['big_mario_left'],
                self.phases['fire_mario_left'],
                self.phases['small_mario_run_left_1'],
                self.phases['small_mario_run_left_2'],
                self.phases['small_mario_run_left_3'],
                self.phases['small_mario_jump_left'],
                self.phases['big_mario_run_left_1'],
                self.phases['big_mario_run_left_2'],
                self.phases['big_mario_run_left_3'],
                self.phases['big_mario_jump_left'],
                self.phases['fire_mario_run_left_1'],
                self.phases['fire_mario_run_left_2'],
                self.phases['fire_mario_run_left_3'],
                self.phases['fire_mario_jump_left'],
            ]:
            return True
    
    def is_right(self):
        if self.sprites.current_phase in [
                self.phases['small_mario_right'],
                self.phases['big_mario_right'],
                self.phases['fire_mario_right'],
                self.phases['small_mario_run_right_1'],
                self.phases['small_mario_run_right_2'],
                self.phases['small_mario_run_right_3'],
                self.phases['small_mario_jump_right'],
                self.phases['big_mario_run_right_1'],
                self.phases['big_mario_run_right_2'],
                self.phases['big_mario_run_right_3'],
                self.phases['big_mario_jump_right'],
                self.phases['fire_mario_run_right_1'],
                self.phases['fire_mario_run_right_2'],
                self.phases['fire_mario_run_right_3'],
                self.phases['fire_mario_jump_right'],
            ]:
            return True
        
    def mario_shoot(self):

        if pyxel.btnp(pyxel.KEY_F):
            self.fireballs.append(Fireball(self.map))
            for fireball in self.fireballs:
                fireball.fire(self.x, self.y)
        for fireball in self.fireballs:
            fireball.update_pve()

        
    def update(self):
    
        self.move_x()
        self.move_y()
        self.mario_shoot()
        self.debugger.update()
        self.map.collision_handler(self)
        
        print(f"{self.x}, {self.y}")
      
    def draw(self):
            
        self.sprites.draw(self.x, self.y)

        self.debugger.draw()
            
        for fireball in self.fireballs:
            fireball.sprites.draw(fireball.x, fireball.y)
            
            