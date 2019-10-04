#La classe Pawn represente les personnages controllables par le jouer ou par l'AI
import pygame
class Pawn:
	def __init__(self, x, y):
		self.x = x
		self.y = y

		self.hp = 3

		self.move_range = 5
		self.attack_range = 1
	
	def move(self, x2, y2):
		self.x = x2
		self.y = y2

	def draw_pawn(self, screen, height, width):
		color = (0, 255, 0)		
		pygame.draw.rect(screen, color, (self.x * height, self.y * width, width, height))	