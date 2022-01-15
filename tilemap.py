import pyxel
import random
from goomba import Goomba
from koopa import Koopa
from blocks import Question, Brick, Pipe
from collisions import Collisions
from powerups import PowerUps
from decorations import Cloud, Bush

class Map:
    
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.sprite = (1, 0, 528, 2000, 400)
        self.h = self.sprite[4]
        self.w = self.sprite[3]
        self.collider = Collisions(self)
        
        self.clouds = Cloud()
        self.bushes = Bush() 
        
        self.power_ups = []
        self.question_blocks = self.create_question_blocks()
        

    def collision_handler(self, mario):
        power_ups = ("star", "flower","red_mushroom","red_mushroom", None, None, None, None, None, None)
        
        self.question_collision(mario, power_ups)
        
        self.power_up_collision(mario)
    
         
    def question_collision(self, mario, power_ups):
        for question in self.question_blocks:
            if self.collider.is_colliding(mario, question) == (True, "down"):
                mario.collide_below(question)
                if question.sprites.current_phase == question.phases['question_block']:
                    question.sprites.set_current_phase("solid_block")
                    self.power_ups.append(PowerUps(question.x, question.y - 16 , 16, 16, random.choice(power_ups)))
                
            if self.collider.is_colliding(mario, question) == (True, "up"):
                mario.collide_above()
            if self.collider.is_colliding(mario, question) == (True, "left"):
                mario.collide_left()
            if self.collider.is_colliding(mario, question) == (True, "right"):
                mario.collide_right()
    

    
    def power_up_collision(self, mario):
        for power_up in self.power_ups:
            if self.collider.is_colliding(mario, power_up):
                self.is_mushroom(mario, power_up)
                self.is_flower(mario, power_up)
                self.is_coin()
                self.is_star(mario, power_up)
                self.power_ups.remove(power_up)
                
    def is_mushroom(self,mario, power_up):
        if power_up.type == "mushroom" and mario.is_small():
            if mario.is_left():
                mario.sprites.set_current_phase("big_mario_left")
            if mario.is_right():
                mario.sprites.set_current_phase("big_mario_right")

    
    def is_flower(self, mario, power_up):
        if power_up.type == "flower" and mario.is_big():
            if mario.is_left():
                mario.sprites.set_current_phase("fire_mario_left")
            if mario.is_right():
                mario.sprites.set_current_phase("fire_mario_right")

    def is_coin(self):
        # Make coin appear, animate, dissapear and add to score
        pass
    
    def is_star(self, mario, power_up):
        if power_up.type == "star":
            pass
            
    def create_question_blocks(self):
        question_blocks = [Question(176, 160), Question(224, 160), Question(240,160), Question(120, 192)]
        return question_blocks
    

    def move(self, velocity: int): 
        self.x += velocity
        self.bushes.move(velocity)
        
        for question in self.question_blocks:
            question.move(velocity)
            
        for power_up in self.power_ups:
            power_up.move(velocity)
            


    def update(self):
        pass
                  
    def draw(self):
            
        pyxel.bltm(self.x, 0, self.sprite[0], self.sprite[1], self.sprite[2], self.sprite[3], self.sprite[4])

        self.clouds.draw()    
        self.bushes.draw()
                
        for question in self.question_blocks:
            question.sprites.draw(question.x, question.y)
            for power_up in self.power_ups:
                if power_up.type is not None:
                    pyxel.blt(power_up.x, power_up.y, power_up.sprite[0], power_up.sprite[1], power_up.sprite[2], power_up.sprite[3],power_up.sprite[4], 12)
        
    