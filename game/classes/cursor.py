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
        self.enemy = None
        #self.wall = None

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

    def displayCursorState(self):
        if self.wall:
            print('|| Wall ||')
        elif self.pawn==None:
            print("|| Ground ||")
        if self.pawn != None:
            print('# Player #')
        if self.enemy != None:
            print('# Enemy #')




    def displayCursorPos(self):
        print('ROW : ', self.row)
        print('COL : ', self.col)
        print('')

    


        

    

    

    
