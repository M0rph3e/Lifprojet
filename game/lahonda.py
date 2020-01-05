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
HEIGHT = 800
CELLWIDTH = 20
CELLHEIGHT = 20


#Variables globales
FPS = 60

def menu():
	done = False
	game_on = False
	while(not done):

		screen = pygame.display.set_mode((HEIGHT, WIDTH))
		font1 = pygame.font.SysFont("comicsansms", 50)
		font2 = pygame.font.SysFont("comicsansms", 25)

		hello = font1.render("Lahonda", True, (255, 0, 0))
		enter = font2.render("Press Enter to Start", True, (255, 0, 0))
		screen.blit(hello, (WIDTH*0.50, HEIGHT*0.20))
		screen.blit(enter, (WIDTH*0.45, HEIGHT*0.40)) 

		for event in pygame.event.get():
			if (event.type == pygame.QUIT):
				done = True
								
			if (event.type == pygame.KEYDOWN):
				if event.key == pygame.K_ESCAPE:
					done = True

				if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
					game_on = True
					done = True

		pygame.display.flip()
	
	if(game_on == True):
		game()

def lose():
	done = False
	game_on = False
	while(not done):

		screen = pygame.display.set_mode((HEIGHT, WIDTH))
		font1 = pygame.font.SysFont("comicsansms", 50)
		font2 = pygame.font.SysFont("comicsansms", 25)

		hello = font1.render("Loser", True, (255, 0, 0))
		enter = font2.render("Press Enter to Restart", True, (255, 0, 0))
		screen.blit(hello, (WIDTH*0.50, HEIGHT*0.20))
		screen.blit(enter, (WIDTH*0.45, HEIGHT*0.40))

		for event in pygame.event.get():
			if (event.type == pygame.QUIT):
				done = True
								
			if (event.type == pygame.KEYDOWN):
				if event.key == pygame.K_ESCAPE:
					done = True

				if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
					game_on = True
					done = True

		pygame.display.flip()
	
	if(game_on == True):
		game()

def win():
	done = False
	game_on = False
	while(not done):

		screen = pygame.display.set_mode((HEIGHT, WIDTH))
		font1 = pygame.font.SysFont("comicsansms", 50)
		font2 = pygame.font.SysFont("comicsansms", 25)

		hello = font1.render("Nice", True, (255, 0, 0))
		enter = font2.render("Press Enter to Restart", True, (255, 0, 0))
		screen.blit(hello, (WIDTH*0.50, HEIGHT*0.20))
		screen.blit(enter, (WIDTH*0.45, HEIGHT*0.40)) 

		for event in pygame.event.get():
			if (event.type == pygame.QUIT):
				done = True
								
			if (event.type == pygame.KEYDOWN):
				if event.key == pygame.K_ESCAPE:
					done = True

				if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
					game_on = True
					done = True

		pygame.display.flip()
	
	if(game_on == True):
		game()

def game():
	
	pygame.display.set_caption("Lahonda")

	screen = pygame.display.set_mode((HEIGHT, WIDTH))

	clock = pygame.time.Clock()

	pawn1 = Pawn(18, 16, 20, 11, 8, UNIT,HACHE)
	pawn2 = Pawn(16, 16, 20, 11, 8, UNIT,EPEE)
	pawn3 = Pawn(16, 18, 20, 11, 8, UNIT,LANCE)
		

	enemy1 = PawnAI(5, 3, 15, 11, 8, ENEMY,HACHE)
	enemy2 = PawnAI(5, 5, 15, 11, 8, ENEMY,EPEE)
	enemy3 = PawnAI(7, 5, 15, 11, 8, ENEMY,LANCE)

	tabPawn = [pawn1,pawn2,pawn3]
	tabEnemy = [enemy1, enemy2, enemy3]




	

	la_mapa = Map(CELLWIDTH, CELLHEIGHT)


	cursorMain = Cursor()
	
	done = False
	el_wino = False
	la_luso = False
	tour = 1
	#Boucle principale de jeu
	while not done:
		screen.fill(BLACK)
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
				
				if(done==True):
					break

				for i in tabPawn:
					la_mapa.add_pawn(i)
		
				for i in tabEnemy:
					la_mapa.add_pawn(i)

				#if(tabEnemy == []):	
				#	el_wino = True
				#	break
				
				#if(tabPawn == []):
				#	la_luso = True
				#	break				

				la_mapa.draw_grid(screen)
				#font1 = pygame.font.SysFont("comicsansms", 25)
				#title = font1.render("Lahonda", True, (255, 0, 0))
				#screen.blit(title, (WIDTH*1.1, HEIGHT*0.01))

				for i in range(0, len(tabPawn)):
					
					font1 = pygame.font.SysFont("comicsansms", 30)
					players_2 = font1.render("Players", True, (255, 0, 0))
					screen.blit(players_2, (WIDTH*1.025, HEIGHT*0.040))

					text = "P{} - Type :{} - hp: {} att: {} def: {} move:{}".format(i+1,tabPawn[i].get_type(),tabPawn[i].hp,tabPawn[i].att,tabPawn[i].defense,tabPawn[i].canMove)
					font2 = pygame.font.SysFont("comicsansms", 15)
					players = font2.render(text, True, (255, 0, 0))
					screen.blit(players, (WIDTH*1.025, HEIGHT*0.1 + HEIGHT*0.035*i))

				for i in range(0, len(tabEnemy)):
					font1 = pygame.font.SysFont("comicsansms", 30)
					enemies = font1.render("AI Players", True, (255, 0, 0))
					screen.blit(enemies, (WIDTH*1.025, HEIGHT*0.235))
					
					text = "AI{} - Type :{} - hp: {} att: {} def: {} move:{}".format(i+1,tabEnemy[i].get_type(),tabEnemy[i].hp,tabEnemy[i].att,tabEnemy[i].defense,tabEnemy[i].canMove)
					font2 = pygame.font.SysFont("comicsansms", 15)
					players = font2.render(text, True, (255, 0, 0))
					screen.blit(players, (WIDTH*1.025, HEIGHT*0.30 + HEIGHT*0.035*i))

				

				#Gestion des evenements
				for event in pygame.event.get():
						if (event.type == pygame.QUIT):
							done = True
							

						if (event.type == pygame.KEYDOWN):
							if event.key == pygame.K_ESCAPE:
								done = True
								
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
											i.afficherStats()								

								if(la_mapa.grid[cursorMain.col][cursorMain.row].team == ENEMY):
									print("ENEMY SELECTED")
									if cursorMain.pawn!=None:
										for i in tabEnemy:
											if(la_mapa.grid[cursorMain.col][cursorMain.row] == i):
												i.afficherStats()
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

			if(done==True):
				break

			for i in tabEnemy:
				i.canMove=7
				i.canAttack=True
				i.fuite = False

			if(tabEnemy == []):	
				el_wino = True
				break
			
			if(tabPawn == []):
				la_luso = True
				break
			

			while tour == 2:
				screen.fill(BLACK)
				
				for i in tabPawn:
					la_mapa.add_pawn(i)
		
				for i in tabEnemy:
					la_mapa.add_pawn(i)

				la_mapa.draw_grid(screen)

				for i in range(0, len(tabPawn)):
					font1 = pygame.font.SysFont("comicsansms", 30)
					players_2 = font1.render("Players", True, (255, 0, 0))
					screen.blit(players_2, (WIDTH*1.025, HEIGHT*0.040))

					text = "P{} - hp: {} att: {} def: {} move:{}".format(i+1,tabPawn[i].hp,tabPawn[i].att,tabPawn[i].defense,tabPawn[i].canMove)
					font2 = pygame.font.SysFont("comicsansms", 15)
					players = font2.render(text, True, (255, 0, 0))
					screen.blit(players, (WIDTH*1.025, HEIGHT*0.1 + HEIGHT*0.035*i))

				for i in range(0, len(tabEnemy)):
					font1 = pygame.font.SysFont("comicsansms", 30)
					enemies = font1.render("AI Players", True, (255, 0, 0))
					screen.blit(enemies, (WIDTH*1.025, HEIGHT*0.235))

					text = "AI{} - hp: {} att: {} def: {} move:{}".format(i+1,tabEnemy[i].hp,tabEnemy[i].att,tabEnemy[i].defense,tabEnemy[i].canMove)
					font2 = pygame.font.SysFont("comicsansms", 15)
					players = font2.render(text, True, (255, 0, 0))
					screen.blit(players, (WIDTH*1.025, HEIGHT*0.30 + HEIGHT*0.035*i))			

				#permet de faire bouger les pions ennemis 
				for j in tabEnemy:
					pawnTarget = None
					la_mapa.grid[j.x][j.y] = la_mapa.g
					target = j.choseTarget(tabPawn, tabEnemy, la_mapa.grid)
					for p in tabPawn:
						if la_mapa.grid[target[0]][target[1]]==p:
							pawnTarget = p
					j.move(target[0], target[1], screen, la_mapa.grid)
					if not j.fuite:
						j.attackTarget(pawnTarget, tabPawn, la_mapa)
					la_mapa.add_pawn(j)
					
					
		
					


				#for event in pygame.event.get():

				#		if (event.type == pygame.KEYDOWN):
				#			if event.key == pygame.K_p:
				#				tour = 1
				###### DEPLACEMENT ET ATTAQUE IA ######

				if all(enemy.canMove == 0 for enemy in tabEnemy):
					tour=1
	
	print('FIN DE LA PARTIE')

	if(el_wino == True):
		win()
	if(la_luso == True):
		lose()


def main():

	pygame.init()
	print("1")
	menu()

	print("2")

	pygame.quit()

#Lancement du main
if __name__ == "__main__":
	main()
	#os.system("pause")