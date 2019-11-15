#La classe Pawn represente les personnages controllables par le jouer ou par l'AI
import pygame
import time
from .colors import *

DISTANCE_DEPL_MAX=7

class Pawn:
	def __init__(self, x, y, att, defense, team):
		self.x = x
		self.y = y
		self.defense=defense
		self.att=att
		self.hp = 20 #j'ai changé
		self.move_range = 5
		self.attack_range = 1
		self.team = team
	
	def move(self, x2, y2,screen):
		if self.get_distance(x2,y2) <= DISTANCE_DEPL_MAX:
			while self.x != x2 or self.y != y2:
				self.remove_pawn(screen, 20, 20)
				if self.x < x2:
					self.x += 1
				elif self.x > x2:
					self.x -= 1
				if self.y < y2:
					self.y += 1
				elif self.y > y2:
					self.y -= 1
				self.draw_pawn(screen, 20, 20)
				time.sleep(0.5)
				pygame.display.flip()
		else:
			print ('Vous ne pouvez pas aller ici')
		

	def draw_pawn(self, screen, height, width):	
		self.rect = pygame.draw.rect(screen, self.team, (self.x * height, self.y * width, width, height))
	
	def remove_pawn(self, screen, height, width):
		pygame.draw.rect(screen, BLACK, (self.x * height, self.y * width, width, height))	
		pygame.draw.rect(screen, GROUND, (self.x * height, self.y * width, width, height),1)

	def get_position(self):
		return (self.x,self.y)

	def attack(self, pion):
		if(self.get_adjacent(pion) and (self.team != pion.team)):	
			print("Oponent HP", pion.hp)
			pion.hp -= self._difference_attaque(self.att,pion.defense)
			print("After attack", pion.hp)
			if pion.hp<=0:
				del pion
				print("Il est mort")
			else:
				print("Current HP", self.hp)
				self.hp -= self._difference_attaque(pion.att,self.defense)
				print("After attack", self.hp)
				if self.hp <= 0:
					del self
					print("Vous êtes pas doués")
		else:
			print("Il est loin pour attaquer, pelo")

	def get_adjacent(self,pion): #verifie qu'un pion est adjacent à un autre
		diff_x = abs(self.x - pion.x)
		diff_y = abs(self.y - pion.y)
		if(diff_x == 0 and diff_y == 1) or (diff_x == 1 and diff_y == 0):
			return True
		else:
			return False

	def get_distance(self,x2,y2): #verifie qu'un pion est adjacent à un autre
		diff_x = abs(self.x - x2)
		diff_y = abs(self.y - y2)
		return diff_x + diff_y
		

	#Cette méthode permet de faire la différence entre l'attaque de l'attaquant et la défense de celui qui est attaqué,
	# elle permet de traité le cas ou défense>attaque qui renverra 0 au lieu d'un nb négatif (rajoutant des pv)
	def _difference_attaque(self, attaque, defense):
		diff=(attaque-defense)
		print("Difference",diff)
		if diff > 0:
			return diff
		else:
			return 0

	 


	
		
		



		

	
	
		