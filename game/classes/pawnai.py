#La classe Pawn AI represente les personnages controllables par l'AI
import pygame
import time
from .colors import *
from classes.ground import Ground
from classes.wall import Wall
from threading import Thread
from classes.pawn import Pawn
from classes.pawn import astar

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

    def choseTarget(self, tabPawn, tabEnemy, grid):
        if tabPawn != []:
            priority = []
            groupePote = []

            
            
            for i in range(0, len(tabPawn)):
                priority.append(0)


            #print(self.get_position())
            for i in tabPawn:
                degatsGroupe = self._difference_attaque(self.att, i.defense)

                pos_i = self.getClosestAdjacent(i.get_position(),grid)
                path=astar(grid, self.get_position(), pos_i)
                
                #print(path)
                
                if(path != None):
                    priority[tabPawn.index(i)] -= len(path) * 0.5 #priorite en fonction de distance
                else:
                    priority[tabPawn.index(i)] -= 0
                
                priority[tabPawn.index(i)] -= i.hp * 2

                if(self._difference_attaque(self.att, i.defense)<8):
                    for j in tabEnemy:
                        if(self.get_position() != j.get_position()):

                            pos_j = self.getClosestAdjacent(j.get_position(),grid)
                            pote_proche = astar(grid, self.get_position(), pos_j)

                            if(len(pote_proche)<=7):
                                groupePote.append(j)

                    for pote in groupePote:
                        degatsGroupe += self._difference_attaque(pote.att, i.defense)
                    if degatsGroupe >= i.hp:
                        priority[tabPawn.index(i)] += 10
            
            
            if priority != []:
                target = tabPawn[priority.index(max(priority))]
                
                if self._difference_attaque(self.att, target.defense) < self._difference_attaque(target.att, self.defense):
                    fuite = Pawn(20-target.x, 20-target.y, 0, 0, 0, UNIT)
                
                    return fuite
                else:
                    return target
        else: 
            return self
        

    def attackTarget(self, target, tabPawn, lamapa):
        if Pawn.get_adjacent(self,target):
            if Pawn.attack(self, target) == True:
                for i in tabPawn:
                    if(lamapa.grid[target.x][target.y] == i):
                        lamapa.grid[i.x][i.y] = lamapa.g
                        tabPawn.remove(i)
                        


    def move(self, screen, grid_in, target):
        dist_min = sys.maxsize
        distance = self.get_distance(target.x,target.y)
        if distance < dist_min:
            dist_min=distance
            posmin = target.get_position()
        
             
        #print("Position initiale :", (self.x,self.y))
        #print("Position finale :", posmin[0]," , ", posmin[1])
        
        
        Pawn.move(self, posmin[0],posmin[1], screen, grid_in)

        self.canMove=0
    
