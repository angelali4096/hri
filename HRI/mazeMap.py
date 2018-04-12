"""
TO DO:
arrow on robot to indicate mode
goal square
"""

from Tkinter import *
from basicAnimationClass import BasicAnimationClass

class MazeMap(BasicAnimationClass):
	def __init__(self):
		self.cellSize = 30
		canvasWidth = self.cellSize * 20
		canvasHeight = self.cellSize * 20
		super(MazeMap, self).__init__(canvasWidth, canvasHeight)
		self.canvasRows = 20
		self.canvasCols = 20

	def drawRobot(self):
		x = self.robotCanvasPos[0] * self.cellSize
		y = self.robotCanvasPos[1] * self.cellSize
		self.canvas.create_rectangle(x, y, x+self.cellSize, y+self.cellSize, fill="blue")

	def moveRobot(self, xChange, yChange):
		(x, y) = self.robotMatrixPos
		newRobotPos = (x+xChange, y+yChange)
		if (newRobotPos[0] < self.matrixCols and newRobotPos[1] < self.matrixRows 
			and newRobotPos[0] >= 0 and newRobotPos[1] >= 0
			and self.matrix[newRobotPos[1]][newRobotPos[0]] == 0):
			
			if newRobotPos[0] < 3:
				self.xOffsetCanvas = 0
			elif newRobotPos[0] < 40:
				self.xOffsetCanvas = newRobotPos[0]-2
			else:
				self.xOffsetCanvas = 38

			if newRobotPos[1] < 5:
				self.yOffsetCanvas = 0
			elif newRobotPos[1] < 21:
				self.yOffsetCanvas = newRobotPos[1]-4
			else:
				self.yOffsetCanvas = 17

			self.robotCanvasPos = (newRobotPos[0]-self.xOffsetCanvas, newRobotPos[1]-self.yOffsetCanvas)
			self.robotMatrixPos = newRobotPos

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

		# only for testing
		# if event.keysym == "Up": self.moveRobot(0, -1)
		# if event.keysym == "Down": self.moveRobot(0, 1)
		# if event.keysym == "Right": self.moveRobot(1, 0)
		# if event.keysym == "Left": self.moveRobot(-1, 0)
		
	def generateMatrix(self):
		matrix = []
		for row in range(self.matrixRows): matrix += [[0] * self.matrixCols]

		#horizontal lines
		for row in range(0,2):
			for col in range(0,58):
				matrix[row][col]=1
		for row in range(7,9):
			for col in range(7,16):
				matrix[row][col]=1
			for col in range(28,37):
				matrix[row][col]=1
			for col in range(49,57):
				matrix[row][col]=1
		for row in range(14,16):
			for col in range(7,30):
				matrix[row][col]=1
			for col in range(35,44):
				matrix[row][col]=1
		for row in range(21,23):
			for col in range(0,9):
				matrix[row][col]=1
			for col in range(21,30):
				matrix[row][col]=1
			for col in range(42,51):
				matrix[row][col]=1
		for row in range(28,30):
			for col in range(7,23):
				matrix[row][col]=1
			for col in range(35,44):
				matrix[row][col]=1
		for row in range(35,37):
			for col in range(0,58):
				matrix[row][col]=1

		#vertical lines
		for col in range(0,2):
			for row in range(7,37):
				matrix[row][col]=1
		for col in range(7,9):
			for row in range(7,16):
				matrix[row][col]=1
		for col in range(14,16):
			for row in range(14,23):
				matrix[row][col]=1
		for col in range(21,23):
			for row in range(0,16):
				matrix[row][col]=1
			for row in range(21,30):
				matrix[row][col]=1
		for col in range(28,30):
			for row in range(14,23):
				matrix[row][col]=1
			for row in range(28,37):
				matrix[row][col]=1
		for col in range(35,37):
			for row in range(7,16):
				matrix[row][col]=1
			for row in range(21,30):
				matrix[row][col]=1
		for col in range(42,44):
			for row in range(0,9):
				matrix[row][col]=1
			for row in range(14,23):
				matrix[row][col]=1
			for row in range(28,37):
				matrix[row][col]=1
		for col in range(49,51):
			for row in range(7,16):
				matrix[row][col]=1
			for row in range(21,30):
				matrix[row][col]=1
		for col in range(56,58):
			for row in range(0,30):
				matrix[row][col]=1

		return matrix

	def drawMap(self):
		xOff = self.xOffsetCanvas
		yOff = self.yOffsetCanvas
		self.canvas.create_rectangle(0, 0, self.canvasCols*self.cellSize, self.canvasRows*self.cellSize, fill="white")
		for row in range(yOff, yOff+self.canvasRows):
			for col in range(xOff, xOff+self.canvasCols):
				if self.matrix[row][col] == 1: 
					self.canvas.create_rectangle((col-xOff)*self.cellSize, (row-yOff)*self.cellSize, 
						(col-xOff+1)*self.cellSize, (row-yOff+1)*self.cellSize, fill="black")

	def redrawAll(self):
		self.canvas.delete(ALL)
		self.drawMap()
		self.drawRobot()

	def initAnimation(self):
		self.matrixRows = 37
		self.matrixCols = 58
		self.xOffsetCanvas = 0
		self.yOffsetCanvas = 0
		self.matrix = self.generateMatrix()
		self.robotMatrixPos = (1, 4)
		self.robotCanvasPos = (1, 4)
		self.mode = "vertical"
		self.app.setTimerDelay(500)
		
mapObj = MazeMap()
mapObj.run()