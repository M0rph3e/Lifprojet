#Classe modelisant un mur pour la map.
#Cette classe hérite de l'interface tile
import pygame
from .colors import * 
class Wall:
    def __init__(self):
        pass

    def draw(self,screen,x,y,height,width):
        pygame.draw.rect(screen, WALL, (y * width, x * height, width, height))

    def get_traversable(self):
        return False
