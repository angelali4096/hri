"""
TO DO:
arrow on robot to indicate mode
maze map
randomize map choices
"""

from Tkinter import *
from basicAnimationClass import BasicAnimationClass

class Map(BasicAnimationClass):
	def __init__(self, mapID):
		self.cellSize = 30
		canvasWidth = self.cellSize * 34
		canvasHeight = self.cellSize * 20
		super(Map, self).__init__(canvasWidth, canvasHeight)
		self.mapID = mapID
		self.rows = 20
		self.cols = 34

	def drawRobot(self):
		x = self.robotPos[0] * self.cellSize
		y = self.robotPos[1] * self.cellSize
		self.canvas.create_rectangle(x, y, x+self.cellSize, y+self.cellSize, fill = "blue")



	def moveRobot(self, xChange, yChange):
		(x, y) = self.robotPos
		newRobotPos = (x+xChange, y+yChange)
		if (newRobotPos[0] < self.cols and newRobotPos[1] < self.rows 
			and newRobotPos[0] >= 0 and newRobotPos[1] >= 0
			and self.matrix[newRobotPos[1]][newRobotPos[0]] == 0):
			self.robotPos = newRobotPos

	def onKeyPressed(self, event):
		if event.keysym == "space":
			if self.mode == "vertical": 
				self.mode = "horizontal"
			else:
				self.mode = "vertical"
		if self.mode == "vertical":
			if event.keysym == "Up": self.moveRobot(0, -1)
			if event.keysym == "Down": self.moveRobot(0, 1)
		if self.mode == "horizontal":
			if event.keysym == "Up": self.moveRobot(1, 0)
			if event.keysym == "Down": self.moveRobot(-1, 0)

		#only for testing
		# if event.keysym == "Up": self.moveRobot(0, -1)
		# if event.keysym == "Down": self.moveRobot(0, 1)
		# if event.keysym == "Right": self.moveRobot(1, 0)
		# if event.keysym == "Left": self.moveRobot(-1, 0)

		
	#mapID = 0
	def drawBlankMap(self):
		self.canvas.create_rectangle(0, 0, self.width, self.height, fill="white")

	#mapID = 1
	def drawTestMap(self):
		self.canvas.create_rectangle(0, 0, self.width, self.height, fill="white")

		rowStart = self.rows/2 - 2
		colStart = self.cols/2 - 7

		#create matrix
		for row in range(rowStart, rowStart+4):
			for col in range(colStart, colStart+14):
				self.matrix[row][col] = 1
		print(self.matrix)


		x = colStart*self.cellSize
		y = rowStart*self.cellSize

		rectWidth = 14 * self.cellSize 
		rectHeight = 4 * self.cellSize

		self.canvas.create_rectangle(x, y, x+rectWidth, y+rectHeight, fill="black")

	#mapID = 2
	def drawDiagMap(self):
		self.canvas.create_rectangle(0, 0, self.width, self.height, fill="white")

		startX = 12 
		startY = 2
		bigBlockY = 4
		bigBlockX = 6 * 2
	
		#top big block
		self.canvas.create_rectangle(startX * self.cellSize, startY * self.cellSize, 
				(startX + bigBlockX) * self.cellSize,
				(startY + bigBlockY) * self.cellSize, fill="black")
		#top big block matrix
		for row in range(startY, startY+bigBlockY):
			for col in range(startX, startX+bigBlockX):
				self.matrix[row][col] = 1

		#top diagonal blocks
		curX = startX + bigBlockX
		curY = startY + bigBlockY
		numLevels = (bigBlockX/2) - 1
		for i in xrange(numLevels):
			curX -= 1 * 2
			curY += 1
			self.canvas.create_rectangle(startX * self.cellSize, 
				(bigBlockY + startY) * self.cellSize, 
				curX * self.cellSize, curY * self.cellSize, fill="black")
			#matrix for top diagonal blocks
			for row in range(startY+bigBlockY, curY):
				for col in range(startX, curX):
					self.matrix[row][col] = 1

		#bottom big block
		self.canvas.create_rectangle(startX * self.cellSize, 
				 (self.rows - bigBlockY - startY) * self.cellSize,
				(startX + bigBlockX) * self.cellSize, 
				(self.rows - startY) * self.cellSize,
				 fill="black")
		#bottom big block matrix
		for row in range(self.rows-bigBlockY-startY, self.rows-startY):
			for col in range(startX, startX+bigBlockX):
				self.matrix[row][col] = 1
		
		#bottom diagonal blocks
		curX = startX
		curY = self.rows - bigBlockY - startY
		for i in xrange(numLevels):
			curX += 1 * 2
			curY -= 1
			self.canvas.create_rectangle(curX * self.cellSize, 
				curY * self.cellSize, (startX + bigBlockX) * self.cellSize, 
				(self.rows - bigBlockY - startY) * self.cellSize, fill="black")
			#matrix for bottom diangonal blocks
			for row in range(curY, self.rows-bigBlockY-startY):
				for col in range(curX,startX+bigBlockX):
					self.matrix[row][col] = 1


	#mapID = 3
	def drawMazeMap(self):
		self.canvas.create_rectangle(0, 0, self.width, self.height, fill="white")

	def redrawAll(self):
		self.canvas.delete(ALL)
		if self.mapID == 0: self.drawBlankMap()
		if self.mapID == 1: self.drawTestMap()
		if self.mapID == 2: self.drawDiagMap()
		if self.mapID == 3: self.drawMazeMap()
		self.drawRobot()

	def initAnimation(self):
		rows = self.rows
		cols = self.cols
		self.matrix = []
		for row in range(rows): self.matrix += [[0] * cols]
		self.robotPos = (1, rows/2)
		self.mode = "vertical"
		self.app.setTimerDelay(500)
		
mapObj = Map(2)
mapObj.run()
