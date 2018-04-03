"""
TO DO:
diag map
correct redrawall
on key pressed to move robot
don't let robot hit obstacles
arrow on robot to indicate mode

LATER TO DO:
maze map
randomize map
"""

from Tkinter import *
from eventBasedAnimationClass import EventBasedAnimationClass

class Map(EventBasedAnimationClass):

	def __init__(self, mapID):
		self.cellSize = 30
		canvasWidth = self.cellSize * 34
		canvasHeight = self.cellSize * 20
		super(Map, self).__init__(canvasWidth, canvasHeight)
		
		self.rows = canvasHeight / self.cellSize
		self.cols = canvasWidth / self.cellSize
		self.mapID = mapID
		#create blank obstacle matrix in terms of "cells"
		self.matrix = []
		for row in range(self.rows): self.matrix += [[0] * self.cols]
		self.robotPos = (1, self.rows/2)

	def initAnimation(self):
		field = []
		rows = self.rows
		cols = self.cols
		self.redrawAll()
		# self.app.setTimerDelay(1000)
		# self.currentAction = 0


	def drawRobot(self):
		x = self.robotPos[0] * self.cellSize
		y = self.robotPos[1] * self.cellSize
		self.canvas.create_rectangle(x, y, x+self.cellSize, y+self.cellSize, fill = "blue")

	# def onKeyPressed(self, event):
	# 	break

	#mapID = 0
	def drawBlankMap(self):
		self.canvas.create_rectangle(0, 0, self.width, self.height, fill="white")

	#mapID = 1
	def drawTestMap(self):
		self.canvas.create_rectangle(0, 0, self.width, self.height, fill="white")
		rectWidth = 14 * self.cellSize 
		rectHeight = 4 * self.cellSize
		x = (self.width / 2) - (rectWidth / 2)
		y = (self.height / 2) - (rectHeight / 2)

		self.canvas.create_rectangle(x, y, x + rectWidth, y + rectHeight, fill="black") #annieblack

		#update matrix
		rowStart = x/self.cellSize
		colStart = y/self.cellSize
		rowEnd = rowStart + rectHeight/self.cellSize
		colEnd = colStart + rectWidth/self.cellSize

		for row in range(rowStart, rowEnd):
			for col in range(colStart, colEnd):
				self.matrix[row][col] = 1
		print(self.matrix)


	#mapID = 2
	def drawDiagMap(self):
		self.canvas.create_rectangle(0, 0, self.width, self.height, fill="white")
		
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

Map(1).run()