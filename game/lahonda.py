#Le programme principal du jeu
from classes.map import Map
from classes.pawn import Pawn
from classes.cursor import Cursor
from classes.colors import *
from classes.ground import Ground  

import pygame
import time
import os

WIDTH = 400 
HEIGHT = 400
CELLWIDTH = 20
CELLHEIGHT = 20


#Variables globales
FPS = 60

def main():
	pygame.init()
	
	pygame.display.set_caption("Lahonda")

	screen = pygame.display.set_mode((HEIGHT, WIDTH))

	clock = pygame.time.Clock()
	pawn1 = Pawn(18,10,10,1,UNIT)
	pawn2 = Pawn(10,5,10,1,UNIT)
	pawn3 = Pawn(10,7,10,1,ENEMY)

	tabPawn = [pawn1,pawn2,pawn3]

	map = Map(CELLWIDTH, CELLHEIGHT)

	cursorMain = Cursor()
	
	map.add_pawn(pawn1)
	map.add_pawn(pawn2)
	map.add_pawn(pawn3)

	done = False
	#Boucle principale de jeu
	while not done:
		screen.fill(BLACK)
		map.draw_grid(screen)

		map.add_pawn(pawn1)
		map.add_pawn(pawn2)
		map.add_pawn(pawn3)
		#Ceci permet de limiter le FPS dans jeu
		clock.tick(FPS)

		#Gestion des evenements
		for event in pygame.event.get():
				if (event.type == pygame.QUIT):
						done = True

				if (event.type == pygame.KEYDOWN):
					if event.key == pygame.K_ESCAPE:
						done = True

				if (event.type == pygame.MOUSEBUTTONDOWN):
					# get the position of the mouse
					mpos_x, mpos_y = event.pos
					
					cursorMain.setPosCursor(mpos_x,mpos_y)

					if(isinstance(map.grid[cursorMain.col][cursorMain.row], Pawn)):			
						print('PLAYER SELECTED')
						cursorMain.pawn = map.grid[cursorMain.col][cursorMain.row]
							
					if(isinstance(map.grid[cursorMain.col][cursorMain.row], Ground)):
						if cursorMain.pawn!=None:
							print("Je suis la")
							
							map.grid[cursorMain.pawn.x][cursorMain.pawn.y] = map.g
							
							cursorMain.pawn.move(cursorMain.col, cursorMain.row, screen)
							
					
						


					

		pygame.display.flip()
	
	pygame.quit()

#Lancement du main
if __name__ == "__main__":
	main()
	#os.system("pause")