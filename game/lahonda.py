#Le programme principal du jeu
from classes.map import Map
from classes.pawn import Pawn
from classes.cursor import Cursor

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
	pawn1.draw_pawn(screen, HEIGHT, WIDTH)

	tabPawn = [pawn1]

	map = Map(CELLWIDTH, CELLHEIGHT)

	cursor = Cursor()



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
					cursor.setPosCursor(mpos_x,mpos_y)
					cursor.isPlayer(tabPawn)
					cursor.displayCursorPos()


					

		pygame.display.flip()
	
	pygame.quit()

#Lancement du main
if __name__ == "__main__":
	main()
	#os.system("pause")