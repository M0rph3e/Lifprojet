#La classe Pawn represente les personnages controllables par le jouer ou par l'AI
import pygame
from .colors import * 
class Pawn:
	def __init__(self, x, y, att, defense):
		self.x = x
		self.y = y
		self.defense=defense
		self.att=att
		self.hp = 20 #j'ai changé
		self.move_range = 5
		self.attack_range = 1
	
	def move(self, x2, y2):
		self.x = x2
		self.y = y2

	def draw_pawn(self, screen, height, width):	
		pygame.draw.rect(screen, UNIT, (self.x * height, self.y * width, width, height))

	def _get_position(self):
		return (self.x,self.y)

	def attack(self, pion):
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

	#Cette méthode permet de faire la différence entre l'attaque de l'attaquant et la défense de celui qui est attaqué,
	# elle permet de traité le cas ou défense>attaque qui renverra 0 au lieu d'un nb négatif (rajoutant des pv)
	def _difference_attaque(self, attaque, defense):
		diff=(attaque-defense)
		print("Difference",diff)
		if diff > 0:
			return diff
		else:
			return 0

	 


	
		
		



		

	
	
		