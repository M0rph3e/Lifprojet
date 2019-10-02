#Le programme principal du jeu

import pygame
import time

#Variables globales
FPS = 60

def main():
	pygame.init()
	screen = pygame.display.set_mode((400,300))

	clock = pygame.time.Clock()

	done = False
	#Boucle principale de jeu
	while not done:
		#Ceci permet de limiter le FPS dans jeu
		clock.tick(FPS)

		#Gestion des evenements
		for event in pygame.event.get():
				if (event.type == pygame.QUIT):
						done = True

				if (event.type == pygame.KEYDOWN):
					if event.key == pygame.K_ESCAPE:
						done = True


		pygame.display.flip()
		

#Lancement du main
if __name__ == "__main__":
	main()
	pygame.quit()