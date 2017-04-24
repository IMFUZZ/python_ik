import pygame, IK

class Leg:

	def __init__(self, length, rootX, rootY, footX, footY):
		self.length = int(length/2)
		self.rootX = rootX
		self.rootY = rootY
		self.kneeX = 0
		self.kneeY = 0
		self.footX = footX
		self.footY = footY
		self.targetX = footX
		self.targetY = footY
		self.lift = 8
	
	def orientFoot(self, x, y):
		self.targetX = x
		self.targetY = y

	def liftFoot(self):
		self.lift = 0

	def update(self):
		if self.lift <= 8:
			self.lift += 1
			self.footY -= 5
		diffX = int(self.targetX - self.footX)
		diffY = int(self.targetY - self.footY)
		if diffX != 0:
			self.footX += diffX/200
		if diffY != 0:
			self.footY += diffY/200

	def draw(self, surface):
		points = self.getPoints()
		for x in range(0, len(points)-1):
			pygame.draw.line(surface, (255, 0, 0), (points[x][0], points[x][1]), (points[x+1][0], points[x+1][1]), 3)

	def getPoints(self):
		targetX = self.footX - self.rootX
		targetY = self.footY - self.rootY
		return [(self.rootX, self.rootY)] + IK.getIKPositions((self.rootX, self.rootY), (targetX, targetY), self.length, self.length)

	def footTargetFromHandle(self, x, y):
		return (x-self.targetX, y-self.targetY)

	def moveTargetX(self, valPerFrame):
		self.targetX += valPerFrame;