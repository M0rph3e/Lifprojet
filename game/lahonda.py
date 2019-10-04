#Le programme principal du jeu
from classes.map import Map
import pygame
import time
import os

WIDTH = 500
HEIGHT = 500
CELLWIDTH = 20
CELLHEIGHT = 20


#Variables globales
FPS = 60

def main():
	pygame.init()
	
	pygame.display.set_caption("Lahonda")

	screen = pygame.display.set_mode((HEIGHT, WIDTH))

	clock = pygame.time.Clock()

	map = Map(CELLWIDTH, CELLHEIGHT)

	

	done = False
	#Boucle principale de jeu
	while not done:

		map.draw_grid(screen)
		
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
					col = mpos_x // (CELLWIDTH) # which cell is the mouse clicking
					row = mpos_y // (CELLHEIGHT) # ^ same
					map.grid[row][col] = 1
					print ("row : ",row) 
					print ("col : ",col)

		pygame.display.flip()
	
	pygame.quit()

#Lancement du main
if __name__ == "__main__":
	main()
	#os.system("pause")