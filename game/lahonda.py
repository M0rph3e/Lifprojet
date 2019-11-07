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
	pawn1 = Pawn(18,10,10,1)

	tabPawn = [pawn1]

	player=None

	map = Map(CELLWIDTH, CELLHEIGHT)

	cursorMain = Cursor()


	done = False
	#Boucle principale de jeu
	while not done:

		map.draw_grid(screen)
		
		#Ceci permet de limiter le FPS dans jeu
		clock.tick(FPS)
		map.draw_grid(screen)
		pawn1.draw_pawn(screen, 20, 20)
		

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
						#player=cursorMain.pawn
					if cursorMain.isGround(map) and not cursorMain.isPlayer(tabPawn):
						cursorMain=cursorMain
						if cursorMain.pawn!=None:
							while cursorMain.pawn.x != cursorMain.col or cursorMain.pawn.y != cursorMain.row:
								cursorMain.pawn.move(cursorMain.col,cursorMain.row)
								map.draw_grid(screen)
								cursorMain.pawn.draw_pawn(screen, 20, 20)
								time.sleep(0.5)
								pygame.display.flip()
							cursorMain.pawn=None
							
							#cursor1.displayCursorPos()
					print('')


					

		pygame.display.flip()
	
	pygame.quit()

#Lancement du main
if __name__ == "__main__":
	main()
	#os.system("pause")