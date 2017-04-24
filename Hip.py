import pygame, Leg, MovementHandle

class Hip:

	def __init__(self, x, y):
		self.originalX = x
		self.originalY = y
		self.x = x
		self.y = y
		self.legA = Leg.Leg(301, x, y, x+75, y+300)
		self.legB = Leg.Leg(301, x, y, x-75, y+300)
		self.mHandle = MovementHandle.MovementHandle(self.x, self.y, 300)
		self.crouched = False

	def update(self):
		self.legA.update()
		self.legB.update()

		self.mHandle
		footATargetFromHandle = self.legA.footTargetFromHandle(self.mHandle.x, self.mHandle.y)
		footBTargetFromHandle = self.legB.footTargetFromHandle(self.mHandle.x, self.mHandle.y)
		point = self.mHandle.getBottomPoint()
		if abs(footATargetFromHandle[0]) > 335:
			self.legA.liftFoot()
			self.legA.orientFoot(point[0], point[1])
		if abs(footBTargetFromHandle[0]) > 335:
			self.legB.liftFoot()
			self.legB.orientFoot(point[0], point[1])

	def getPoints(self):
		points = []
		points += self.legA.getPoints()
		points += self.legB.getPoints()
		return points

	def draw(self, surface):
		points = self.legA.getPoints()
		for x in range(0, len(points)-1):
			pygame.draw.line(surface, (255, 0, 0), (points[x][0], points[x][1]), (points[x+1][0], points[x+1][1]), 3)
		points = self.legB.getPoints()
		for x in range(0, len(points)-1):
			pygame.draw.line(surface, (255, 0, 0), (points[x][0], points[x][1]), (points[x+1][0], points[x+1][1]), 3)
		self.mHandle.draw(surface)

	def moveFeetTargets(self, valPerFrame):
		self.legA.moveTargetX(valPerFrame)
		self.legB.moveTargetX(valPerFrame)

	def crouch(self, crouched):
		if crouched:
			self.y = self.originalX/2
		else:
			self.y = self.originalX*2