
class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def get_x(self):
        return self.x
    
    @property
    def get_y(self):
        return self.y
    
    @property
    def get_vx(self):
        return self.vx
    
    @property
    def get_vy(self):
        return self.vy