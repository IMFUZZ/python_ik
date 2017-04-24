import pygame

class MovementHandle:

	def __init__(self, x, y, length):
		self.x = x
		self.y = y
		self.length = length

	def move(self, x, y):
		self.x = x
		self.y = y

	def draw(self, surface):
		pygame.draw.line(surface, (0, 0, 0), (self.x, self.y), (self.x, self.y + self.length), 3)

	def getBottomPoint(self):
		return (self.x, self.y+self.length)