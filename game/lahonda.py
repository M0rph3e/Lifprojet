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

	pawn1 = Pawn(18,18,10,1,UNIT)
	pawn2 = Pawn(18,16,10,1,UNIT)
	pawn3 = Pawn(16,18,10,1,UNIT)
		

	enemy1 = Pawn(5,1,10,1,ENEMY)
	enemy2 = Pawn(5,3,10,1,ENEMY)
	enemy3 = Pawn(7,1,10,1,ENEMY)

	tabPawn = [pawn1,pawn2,pawn3, enemy1, enemy2, enemy3]

	la_mapa = Map(CELLWIDTH, CELLHEIGHT)

	cursorMain = Cursor()
	
	done = False
	#Boucle principale de jeu
	while not done:
		screen.fill(BLACK)
		
		for i in tabPawn:
			la_mapa.add_pawn(i)
		
		la_mapa.draw_grid(screen)
		
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

					if(isinstance(la_mapa.grid[cursorMain.col][cursorMain.row], Pawn)):
						if(la_mapa.grid[cursorMain.col][cursorMain.row].team == UNIT):
							print('PLAYER SELECTED')
							cursorMain.pawn = la_mapa.grid[cursorMain.col][cursorMain.row]
						if(la_mapa.grid[cursorMain.col][cursorMain.row].team == ENEMY):
							print("ENEMY SELECTED")
							cursorMain.enemy = la_mapa.grid[cursorMain.col][cursorMain.row]
							cursorMain.pawn.attack(cursorMain.enemy)
							
					if(isinstance(la_mapa.grid[cursorMain.col][cursorMain.row], Ground)):
						if cursorMain.pawn!=None:
							print("Je suis la")
							
							la_mapa.grid[cursorMain.pawn.x][cursorMain.pawn.y] = la_mapa.g
							
							cursorMain.pawn.move(cursorMain.col, cursorMain.row, screen)



					

		pygame.display.flip()
	
	pygame.quit()

#Lancement du main
if __name__ == "__main__":
	main()
	#os.system("pause")