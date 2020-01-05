#La classe Map represente le terrain
import pygame
from .pawn import Pawn
from .wall import Wall
from .ground import Ground
class Map:
	#inititalisation
	def __init__(self, height, width):
		self.height = height
		self.width = width
		self.size = 20
		self.w = Wall()
		self.g = Ground()
		#le terrain est stocké dans une liste avec 1 - mur, 0 - sol
		
		self.grid = [[self.w, self.w, self.w, self.w, self.w, self.w, self.w, self.w, self.w, self.w, self.w, self.w, self.w, self.w, self.w, self.w, self.w, self.w, self.w, self.w],
					 [self.w, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.w],
					 [self.w, self.g, self.g, self.g, self.g, self.w, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.w, self.g, self.g, self.w],
					 [self.w, self.g, self.g, self.g, self.g, self.w, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.w, self.g, self.g, self.w],
					 [self.w, self.w, self.w, self.w, self.w, self.w, self.g, self.g, self.w, self.w, self.g, self.g, self.g, self.g, self.g, self.g, self.w, self.g, self.g, self.w],
					 [self.w, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.w, self.w, self.g, self.g, self.g, self.g, self.g, self.g, self.w, self.g, self.g, self.w],
					 [self.w, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.w, self.w, self.g, self.g, self.g, self.g, self.g, self.g, self.w, self.g, self.g, self.w],
					 [self.w, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.w, self.w, self.g, self.g, self.g, self.g, self.g, self.g, self.w, self.g, self.g, self.w],
					 [self.w, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.w, self.g, self.g, self.w],
					 [self.w, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.w, self.g, self.g, self.w],
					 [self.w, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.w, self.w, self.w, self.w],
					 [self.w, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.w, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.w],
					 [self.w, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.w, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.w],
					 [self.w, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.w, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.w],
					 [self.w, self.w, self.w, self.w, self.w, self.w, self.w, self.w, self.g, self.g, self.g, self.w, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.w],
					 [self.w, self.g, self.g, self.g, self.g, self.g, self.g, self.w, self.g, self.g, self.g, self.w, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.w],
					 [self.w, self.g, self.g, self.g, self.g, self.g, self.g, self.w, self.g, self.g, self.g, self.w, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.w],
					 [self.w, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.w, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.w],
					 [self.w, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.w, self.g, self.g, self.g, self.g, self.g, self.g, self.g, self.w],
					 [self.w, self.w, self.w, self.w, self.w, self.w, self.w, self.w, self.w, self.w, self.w, self.w, self.w, self.w, self.w ,self.w, self.w, self.w, self.w, self.w]]

	def draw_grid(self, screen):
		for row in range(self.size):
			for column in range(self.size):
				if self.grid[column][row] == self.w:
					self.w.draw(screen,row,column,self.height,self.width)
				if self.grid[column][row] == self.g:
					self.g.draw(screen,row,column,self.height,self.width)
				if isinstance(self.grid[column][row], Pawn):
					self.grid[column][row].draw_pawn(screen, self.height, self.width)
					
	def add_pawn(self, pawn):
		self.grid[pawn.x][pawn.y] = pawn

	def afficher(self):
		for row in range(self.size):
			for column in range(self.size):
				if(isinstance(self.grid[column][row], Ground)):
					print("[ ]",  end = "")
				if(isinstance(self.grid[column][row], Wall)):
					print("[/]",  end = "")
				if(isinstance(self.grid[column][row], Pawn)):
					print("[P]",  end = "")
			print("\n")	