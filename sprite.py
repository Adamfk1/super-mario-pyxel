import pyxel

class Sprite():
    def __init__(self, phases: {str: (int, int, int, int)}, initial_phase_name):
        self.phases = phases
        self.current_phase = self.phases[initial_phase_name]

    def set_current_phase(self, phase_name):
        self.current_phase = self.phases[phase_name]

    def get_width(self):
        return self.current_phase[2]

    def get_height(self):
        return self.current_phase[3]

    def draw(self, x, y):
        pyxel.blt(x,y,0, *self.current_phase, 12)
        

