import math

def lastBoneAngle(targetX, targetY, d1, d2):
	numerator = (targetX**2)+(targetY**2)-(d1**2)-(d2**2)
	denominator = (2*d1*d2)
	cosAngle = numerator/denominator
	if (cosAngle > 1 or cosAngle < -1):
		cosAngle = 1
	return math.acos(cosAngle) 

def secondaryAngle(angle, targetX, targetY, d1, d2):
	triAdjacent = (d1+(d2*math.cos(angle)))
	triOpposite = (d2*(math.sin(angle)))
	return math.atan2((targetY*triAdjacent - targetX*triOpposite), (targetX*triAdjacent + targetY*triOpposite))

def getIKPositions(origin, target, d1, d2):
	originX = origin[0]
	originY = origin[1]
	targetX = target[0]
	targetY = target[1]
	endAngle = lastBoneAngle(targetX, targetY, d1, d2)
	rootAngle = secondaryAngle(endAngle, targetX, targetY, d1, d2)
	endAngle += rootAngle
	rootX = originX + math.cos(rootAngle)*d2
	rootY = originY + math.sin(rootAngle)*d2
	endX = rootX + math.cos(endAngle)*d1
	endY = rootY + math.sin(endAngle)*d1
	return [(rootX, rootY), (endX, endY)]
