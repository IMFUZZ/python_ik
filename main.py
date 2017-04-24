import sys, pygame, math
import Hip
pygame.init()

def main():
	size = width, height = 800, 600
	centerWidth, centerHeight = width/2, height/2-100
	screen = pygame.display.set_mode(size)
	hip = Hip.Hip(centerWidth, centerHeight)
	pressedKey = None
	while 1:
		screen.fill((255, 255, 255))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				pressedKey = event.key
				if event.key == pygame.K_ESCAPE:
					sys.exit()
			else:
				pressedKey = None
			if pygame.mouse.get_pressed()[0]:
				hip.legA.orientFoot(mousePos[0], mousePos[1])
			if pygame.mouse.get_pressed()[1]:
				print("button2")
			if pygame.mouse.get_pressed()[2]:
				hip.legB.orientFoot(mousePos[0], mousePos[1])

		if pressedKey == pygame.K_RIGHT:
			hip.mHandle.move(hip.x+175, hip.y)
			hip.moveFeetTargets(-0.4)
		if pressedKey == pygame.K_LEFT:
			hip.mHandle.move(hip.x-175, hip.y)
			hip.moveFeetTargets(0.4)
		if pressedKey != pygame.K_LEFT and pressedKey != pygame.K_RIGHT:
			hip.mHandle.move(hip.x, hip.y)

		if pressedKey == pygame.K_DOWN:
			hip.crouch(True)
		if pressedKey == pygame.K_UP:
			hip.crouch(False)

		mousePos = pygame.mouse.get_pos()
		hip.update()
		hip.draw(screen)

		pygame.display.flip()

if __name__ == "__main__":
	main()