#La classe Pawn AI represente les personnages controllables par l'AI
import pygame
import time
from .colors import *
from classes.ground import Ground
from classes.wall import Wall
from threading import Thread
from classes.pawn import Pawn
import random
import sys
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

    def move(self, screen, grid_in, tabPawn):
        dist_min = sys.maxsize
        posmin = self.get_position()
        for i in tabPawn:
            distance = self.get_distance(i.x,i.y)
            if distance < dist_min:
                dist_min=distance
                posmin = i.get_position()
        
             
        print("Position initiale :", (self.x,self.y))
        print("Position finale :", posmin[0]," , ", posmin[1])


        Pawn.move(self, posmin[0]-1,posmin[1], screen, grid_in)

        self.canMove=0
    
