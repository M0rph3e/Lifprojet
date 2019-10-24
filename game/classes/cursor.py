#La classe cursor represente la case choisi par le jouer
import pygame
from .pawn import Pawn
from .map import Map

CELLWIDTH = 20
CELLHEIGHT = 20

class Cursor:
    #inititalisation
    def __init__(self):
        self.col = None
        self.row = None
        self.pawn = None
        self.wall = None

    def setPosCursor(self, mouseX, mouseY):
        colTest = mouseX // (CELLWIDTH) # which cell is the mouse clicking
        rowTest = mouseY // (CELLHEIGHT) # ^ same
        if rowTest >= 0 and colTest >= 0:
            try:
                self.col = colTest
                self.row = rowTest
                #map.grid[col][row] = 1
                
            except IndexError:
                pass
    
    def isPlayer(self, tabPlayer):
        for player in tabPlayer:
            if player.x == self.col and player.y == self.row:
                self.pawn = True
                print('\o/ Player \o/')
                break
            else:
                print('# No Player #')
        if self.pawn == None:
            self.pawn = False

    def isWall(self, map):
        if map.grid[self.col][self.row].get_traversable():
            self.wall=False
            print("|| Ground ||")
        else:
            self.wall=True 
            print('|| Wall ||')
            
    def displayCursorPos(self):
        print('ROW : ', self.row)
        print('COL : ', self.col)
    


        

    

    

    
