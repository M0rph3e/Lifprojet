#La classe Map represente le terrain
import pygame
class Map:
	#inititalisation
	def __init__(self, height, width, size):
		self.height = height
		self.width = width
		self.size = size
		#le terrain est stocké dans une liste avec 1 - mur, 0 - sol
		self.grid = []
	
	#remplissage de la liste
	def fill_grid(self):
		for row in range(size):
			self.grid.append([])
			for column in range(size):
				if(row == (0 or 9) or column == (0 or 9))
					self.grid[row].append(1)
				else
					self.grid[row].append(0)

	#
	def draw_grid(self, screen):
		for row in range(size):
			for column in range(size):
				if grid[row][column] == 1:
					color = (255, 255, 255)
					pygame.draw.rect(screen, color, (column, row, width/size, height/size))
				else
					color = (0, 0, 0)
					pygame.draw.rect(screen, color, (column, row, width/size, height/size))
