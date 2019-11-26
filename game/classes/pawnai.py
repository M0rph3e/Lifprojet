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
    def __init__(self, x, y, hp, att, defense, team):
        self.x = x
        self.y = y
        self.defense=defense
        self.att=att
        self.hp = hp 
        self.move_range = 5
        self.attack_range = 1
        self.team = team
        self.canMove=DISTANCE_DEPL_MAX
        self.canAttack=True

    def choseTarget(self, tabPawn):
        priority = [0,0,0]

        for i in tabPawn:         
            priority[tabPawn.index(i)] -= self.get_distance(i.x,i.y) #priorite en fonction de distance
            priority[tabPawn.index(i)] -= i.hp
            priority[tabPawn.index(i)] += self._difference_attaque(i.att, i.defense)
        
        print(priority)
        return tabPawn[priority.index(max(priority))]

    def move(self, screen, grid_in, target):
        dist_min = sys.maxsize
        distance = self.get_distance(target.x,target.y)
        if distance < dist_min:
            dist_min=distance
            posmin = target.get_position()
        
             
        print("Position initiale :", (self.x,self.y))
        print("Position finale :", posmin[0]," , ", posmin[1])


        Pawn.move(self, posmin[0]-1,posmin[1], screen, grid_in)

        self.canMove=0
    
