#La classe Pawn AI represente les personnages controllables par l'AI
import pygame
import time
from .colors import *
from classes.ground import Ground
from classes.wall import Wall
from threading import Thread
from classes.pawn import Pawn
import random
DISTANCE_DEPL_MAX=7


class PawnAI(Pawn):
    def __init__(self, x, y, att, defense, team):
        self.x = x
        self.y = y
        self.defense=defense
        self.att=att
        self.hp = 20 
        self.move_range = 5
        self.attack_range = 1
        self.team = team
        self.canMove=DISTANCE_DEPL_MAX
        self.canAttack=True

    def move(self, screen, grid_in):
        new_x = random.randrange(self.x-self.canMove,self.x+self.canMove+1,1)
        max = abs(new_x-self.x)
        new_y = random.randrange(self.x-self.canMove+max,self.x+self.canMove-max+1,1)
        pos_ini = (self.x,self.y)
        pos_fin = (new_x,new_y)
        print("Position initiale :", pos_ini)
        print("Position finale :", pos_fin)
        Pawn.move(self, new_x,new_y, screen, grid_in)
        self.canMove=0


