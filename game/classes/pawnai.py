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
    def __init__(self, x, y, hp, att, defense, team,type):
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
        self.fuite = False
        self.type=type

    def move(self, x2, y2,screen,grid_in):
        Pawn.move(self, x2, y2,screen,grid_in)
        self.canMove=0

    def choseTarget(self, tabPawn, tabEnemy, grid):
        if tabPawn != []:
            priority = []
            groupePote = []

            
            
            for i in range(0, len(tabPawn)):
                priority.append(0)


            #print(self.get_position())
            for i in tabPawn:
                degatsGroupe = self._difference_attaque(self.att, i.defense)

                path=astar(grid, self.get_position(), i.get_position(), True)
                
                #print(path)
                
                if(path != None):
                    priority[tabPawn.index(i)] -= len(path) * 0.5 #priorite en fonction de distance
                else:
                    priority[tabPawn.index(i)] -= 0
                
                priority[tabPawn.index(i)] -= i.hp * 2

                if(self._difference_attaque(self.att, i.defense)<8):
                    for j in tabEnemy:
                        if(self.get_position() != j.get_position()):

                            pote_proche = astar(grid, j.get_position(), i.get_position(), True)

                            if pote_proche != None:
                                if(len(pote_proche)<=7):
                                    groupePote.append(j)

                    for pote in groupePote:
                        degatsGroupe += self._difference_attaque(pote.att, i.defense)
                        
                    if degatsGroupe >= i.hp:
                        priority[tabPawn.index(i)] += 10
            
            if priority != []:
                target = tabPawn[priority.index(max(priority))]

                if self._difference_attaque(self.att, target.defense) < self._difference_attaque(target.att, self.defense):
                    posMoy = getPositionMoy(tabPawn)
                    posFuite = getFarthestCorner(posMoy[0], posMoy[1], grid)
                    self.fuite = True
                    print("posMoy : ",posMoy)
                    return posFuite
                else:
                    return (target.x, target.y)
        else: 
            return self
        

    def attackTarget(self, target, tabPawn, lamapa):
        if Pawn.get_adjacent(self,target):
            if Pawn.attack(self, target) == True:
                for i in tabPawn:
                    if(lamapa.grid[target.x][target.y] == i):
                        lamapa.grid[i.x][i.y] = lamapa.g
                        tabPawn.remove(i)
                        

def get_distance(x, y, x2, y2): 
    diff_x = abs(x - x2)
    diff_y = abs(y - y2)
    return diff_x + diff_y

def getFarthestCorner(x, y, grid):
        topLeft=(1,1)
        topRight=(1,18)
        bottomLeft=(18,1)
        bottomRight=(18,18)

        options = []
        

        tL = get_distance(x, y, topLeft[0],topLeft[1])
        tR = get_distance(x, y, topRight[0],topRight[1])
        bL = get_distance(x, y, bottomLeft[0],bottomLeft[1])
        bR = get_distance(x, y, bottomRight[0],bottomRight[1])

        options.append((tL,topLeft))
        options.append((tR,topRight))
        options.append((bL,bottomLeft))
        options.append((bR,bottomRight))

        options.sort(key=lambda x: x[0])
        options.reverse()

        for pos in options:
             if (not isinstance(grid[pos[1][0]][pos[1][1]], Wall)): 
                 pos_fin =  pos[1]
                 return pos_fin
    
