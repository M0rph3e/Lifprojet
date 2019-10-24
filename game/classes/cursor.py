#La classe cursor represente la case choisi par le jouer
import pygame
from .pawn import Pawn

CELLWIDTH = 20
CELLHEIGHT = 20

class Cursor:
    #inititalisation
    def __init__(self):
        self.col = None
        self.row = None
        self.pawn = None

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
                print('# Player #')
                break
            else:
                print('# Empty tile #')
        if self.pawn == None:
            self.pawn = False

    def displayCursorPos(self):
        print('ROW : ', self.row)
        print('COL : ', self.col)
    


        

    

    

    
