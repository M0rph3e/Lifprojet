#La classe Map represente le terrain
import pygame
class Map:
	#inititalisation
	def __init__(self, height, width, size):
		self.height = height
		self.width = width
		self.size = size-1
		#le terrain est stocké dans une liste avec 1 - mur, 0 - sol
		
		self.grid = [[1, 1, 1, 1, 1],
					 [1, 0, 0, 0, 1],
					 [1, 0, 0, 0, 1],
					 [1, 0, 0, 0, 1],
					 [1, 1, 1, 1, 1]]

	def draw_grid(self, screen):
		for row in range(self.size):
			for column in range(self.size):
				if self.grid[row][column] == 1:
					color = (255, 255, 255)
					pygame.draw.rect(screen, color, (column, row, self.width/self.size, self.height/self.size),self.size)
				if self.grid[row][column] == 0:
					color = (0, 0, 0)		
					pygame.draw.rect(screen, color, (column, row, self.width/self.size, self.height/self.size),self.size)


"""
	#remplissage de la liste
	def fill_grid(self):
		for row in range(size):
			self.grid.append([])
			for column in range(size):
					self.grid[row][column].append(0)
"""