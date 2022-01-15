import pyxel

class Collisions:
    

    def __init__(self, map):
        self.map = map

    def get_tile_type_at(self, screen_x, screen_y):
        return pyxel.tilemap(1).pget((screen_x - self.map.x) // 8, (screen_y // 8) + 66)

    def is_not_air_tile(self, tile_one: tuple, tile_two: tuple):
        if tile_one != (0, 0) or tile_two != (0, 0):
            return True
        else:
            return False
        
    def is_colliding(self, player, object):
                
        player_right = player.x + player.w
        player_top = player.y + player.h
        player_left = player.x
        player_bottom = player.y
        
        object_right = object.x + object.w
        object_top = object.y + object.h
        object_left = object.x
        object_bottom = object.y
        
        left_line = player_right - object_left
        above_line = player_top - object_bottom
        below_line = object_top - player_bottom
        right_line = object_right - player_left
        
        
        if min(left_line, right_line, below_line, above_line) >= 0:
            

            if above_line < (left_line and right_line and below_line):
                return (True, "up")
            elif below_line < (left_line and right_line and above_line):
                return (True, "down")
            elif right_line < (above_line and left_line and below_line):
                return (True, "left")             
            elif left_line < (above_line and right_line and below_line):
                return (True, "right")             
          

