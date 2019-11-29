#Le programme principal du jeu
from classes.map import Map
from classes.pawn import Pawn
from classes.pawnai import PawnAI
from classes.cursor import Cursor
from classes.colors import *
from classes.ground import Ground  

import pygame
import time
import os
import sys

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

	pawn1 = Pawn(18, 16, 20, 5, 3, UNIT)
	pawn2 = Pawn(16, 16, 20, 5, 3, UNIT)
	pawn3 = Pawn(16, 18, 20, 5, 3, UNIT)
		

	enemy1 = PawnAI(5, 3, 15, 10, 5, ENEMY)
	enemy2 = PawnAI(5, 5, 15, 10, 5, ENEMY)
	enemy3 = PawnAI(7, 5, 15, 10, 5, ENEMY)

	tabPawn = [pawn1,pawn2,pawn3]
	tabEnemy = [enemy1, enemy2, enemy3]

	la_mapa = Map(CELLWIDTH, CELLHEIGHT)

	cursorMain = Cursor()
	
	done = False

	tour = 1
	#Boucle principale de jeu
	while not done:
		
		#Ceci permet de limiter le FPS dans jeu
		clock.tick(FPS)
		###### TOUR JOUEUR ######
		if tour == 1:
			print('Au tour du Joueur')

			for i in tabPawn:
				i.canMove=7
				i.canAttack=True

			while tour == 1:

				

				screen.fill(BLACK)

				if(tabPawn == [] or tabEnemy == []):
					done = True
					break

				for i in tabPawn:
					la_mapa.add_pawn(i)
		
				for i in tabEnemy:
					la_mapa.add_pawn(i)

				la_mapa.draw_grid(screen)

				#Gestion des evenements
				for event in pygame.event.get():
						if (event.type == pygame.QUIT):
							pygame.quit()
							sys.exit()

						if (event.type == pygame.KEYDOWN):
							if event.key == pygame.K_ESCAPE:
								pygame.quit()
								sys.exit()
							if event.key == pygame.K_p:
								tour = 2
							if event.key == pygame.K_d:
								la_mapa.afficher()

						if (event.type == pygame.MOUSEBUTTONDOWN):
							# get the position of the mouse
							mpos_x, mpos_y = event.pos
							cursorMain.setPosCursor(mpos_x,mpos_y)
							if(isinstance(la_mapa.grid[cursorMain.col][cursorMain.row], Ground)):
								if cursorMain.pawn!=None:
									la_mapa.grid[cursorMain.pawn.x][cursorMain.pawn.y] = la_mapa.g
									cursorMain.pawn.move(cursorMain.col, cursorMain.row, screen,la_mapa.grid)

							if(isinstance(la_mapa.grid[cursorMain.col][cursorMain.row], Pawn)):
								if(la_mapa.grid[cursorMain.col][cursorMain.row].team == UNIT):
									print('PLAYER SELECTED')
									for i in tabPawn:
										if(la_mapa.grid[cursorMain.col][cursorMain.row] == i):
											cursorMain.pawn = i
									#for i in range (cursorMain.col-7,cursorMain.col+7):
									#	for j in range (cursorMain.row-7,cursorMain.row+7):
									#		diff_x = abs(cursorMain.col - i)
									#		diff_y = abs(cursorMain.row - j)
									#		if diff_x + diff_y <=5:
									#			pygame.draw.rect(screen, RED, (i * la_mapa.width, j * la_mapa.height, la_mapa.width, la_mapa.height)) 								

								if(la_mapa.grid[cursorMain.col][cursorMain.row].team == ENEMY):
									print("ENEMY SELECTED")
									if cursorMain.pawn!=None:
										for i in tabEnemy:
											if(la_mapa.grid[cursorMain.col][cursorMain.row] == i):
												if(cursorMain.pawn.attack(i)):
													la_mapa.grid[i.x][i.y] = la_mapa.g
													tabEnemy.remove(i)

									
									
							cursorMain.displayCursorPos()

				if all(pawn.canMove == 0 for pawn in tabPawn) and all(pawn.canAttack == False for pawn in tabPawn):
					
					tour=2
					print('fin du tour')
		
				pygame.display.flip()
		

		###### TOUR IA ######
		if tour == 2:
			print("Au tour de l'IA")
			for i in tabEnemy:
				i.canMove=7
				i.canAttack=True

			

			

			while tour == 2:
				screen.fill(BLACK)
		
				for i in tabPawn:
					la_mapa.add_pawn(i)
		
				for i in tabEnemy:
					la_mapa.add_pawn(i)

				la_mapa.draw_grid(screen)

				

				#permet de faire bouger les pions ennemis 
				for j in tabEnemy:
					la_mapa.grid[j.x][j.y] = la_mapa.g
					j.move(screen, la_mapa.grid, j.choseTarget(tabPawn, tabEnemy, la_mapa.grid))
					j.attackTarget(j.choseTarget(tabPawn, tabEnemy, la_mapa.grid), tabPawn, la_mapa)
					
					la_mapa.add_pawn(j)
					
					
					
					


				for event in pygame.event.get():

						if (event.type == pygame.KEYDOWN):
							if event.key == pygame.K_p:
								tour = 1
				###### DEPLACEMENT ET ATTAQUE IA ######

				if all(enemy.canMove == 0 for enemy in tabEnemy):
					tour=1

				if(tabPawn == [] or tabEnemy == []):
					done = True
					break
					

	print('FIN DE LA PARTIE')				

	pygame.quit()

#Lancement du main
if __name__ == "__main__":
	main()
	#os.system("pause")