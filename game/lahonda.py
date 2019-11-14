#Le programme principal du jeu
from classes.map import Map
from classes.pawn import Pawn
from classes.cursor import Cursor
from classes.colors import * 

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

	player=None

	map = Map(CELLWIDTH, CELLHEIGHT)

	cursorMain = Cursor()
	cursorCase = Cursor()

	

	done = False
	#Boucle principale de jeu
	while not done:
		screen.fill(BLACK)
		map.draw_grid(screen)
		
		#Ceci permet de limiter le FPS dans jeu
		clock.tick(FPS)
		map.draw_grid(screen)
		for i in tabPawn:
			i.draw_pawn(screen, 20, 20)
		

		#Gestion des evenements
		for event in pygame.event.get():
				if (event.type == pygame.QUIT):
						done = True

				if (event.type == pygame.KEYDOWN):
					if event.key == pygame.K_ESCAPE:
						done = True

				if (event.type == pygame.KEYDOWN):
					if event.key == pygame.K_f:
						pawn1.move(pawn1.x-1,pawn1.y)


				if (event.type == pygame.MOUSEBUTTONDOWN):
					# get the position of the mouse
					mpos_x, mpos_y = event.pos
					cursorMain.setPosCursor(mpos_x,mpos_y)
					if cursorMain.isPlayer(tabPawn):
						print('PLAYER SELECTED')
						#cursorPlayer=cursorMain
						
					if cursorMain.isGround(map) and not cursorMain.isPlayer(tabPawn):
						cursorCase=cursorMain
						if cursorMain.pawn!=None:
							cursorMain.pawn.move(cursorCase.col,cursorCase.row,screen)
							cursorMain.pawn=None
						
						if cursorMain.enemy!=None:
							cursorMain.enemy.move(cursorCase.col,cursorCase.row,screen)
							cursorMain.enemy=None
					
					if not cursorMain.isGround(map) and cursorMain.isPlayer(tabPawn):
						cursorCase=cursorMain
						if cursorMain.pawn!=None and cursorMain.enemy!=None:
							print("Je suis la")
							cursorMain.pawn.attack(cursorMain.enemy)
							cursorMain.pawn=None
							cursorMain.enemy=None
					
					print('')


					

		pygame.display.flip()
	
	pygame.quit()

#Lancement du main
if __name__ == "__main__":
	main()
	#os.system("pause")