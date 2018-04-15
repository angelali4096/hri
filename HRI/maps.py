"""
TO DO:
arrow on robot to indicate mode
goal square
"""

from Tkinter import *
from basicAnimationClass import BasicAnimationClass
from node import Node
from timeOptPlanner import TimeOptPlanner
from random import *

class Map(BasicAnimationClass):
    def __init__(self, mapID, assistanceType):
        self.cellSize = 30
        canvasWidth = self.cellSize * 34
        canvasHeight = self.cellSize * 20
        super(Map, self).__init__(canvasWidth, canvasHeight)
        self.mapID = mapID
        self.rows = 20
        self.cols = 34
        self.assistanceType = assistanceType # randomly assigns assistance type 
        self.mode = "vertical" # This is the mode the user is currently using
        self.zone = 1 # This is the optimal mode zone based on the optimality map

    def drawRobot(self):
        x = self.robotPos[0] * self.cellSize
        y = self.robotPos[1] * self.cellSize
        self.canvas.create_rectangle(x, y, x+self.cellSize, y+self.cellSize, fill = "blue")

    def getOptMode(self):
        if self.assistanceType == 1:
            return self.mode

        elif self.assistanceType == 2:
            if self.optMode[self.robotPos[1]][self.robotPos[0]] != self.zone:
                if self.zone == 0:
                    self.zone = 1
                    return "vertical"
                else:
                    self.zone = 0
                    return "horizontal"
            return self.mode

        elif self.assistanceType == 3:
            if self.optMode[self.robotPos[1]][self.robotPos[0]] == 0:
                return "horizontal"
            else:
                return "vertical"

    def moveRobot(self, xChange, yChange):
        (x, y) = self.robotPos
        newRobotPos = (x+xChange, y+yChange)
        if (newRobotPos[0] < self.cols and newRobotPos[1] < self.rows 
            and newRobotPos[0] >= 0 and newRobotPos[1] >= 0
            and self.matrix[newRobotPos[1]][newRobotPos[0]] == 0):
            self.robotPos = newRobotPos
            self.mode = self.getOptMode()

    def onKeyPressed(self, event):
        if event.keysym == "space":
            if self.mode == "vertical": 
                self.mode = "horizontal"
            else:
                self.mode = "vertical"
        if self.mode == "vertical":
            if event.keysym == "Up": self.moveRobot(0, -1)
            elif event.keysym == "Down": self.moveRobot(0, 1)
        elif self.mode == "horizontal":
            if event.keysym == "Up": self.moveRobot(1, 0)
            elif event.keysym == "Down": self.moveRobot(-1, 0)

        # only for testing
        # if event.keysym == "Up": self.moveRobot(0, -1)
        # if event.keysym == "Down": self.moveRobot(0, 1)
        # if event.keysym == "Right": self.moveRobot(1, 0)
        # if event.keysym == "Left": self.moveRobot(-1, 0)


    def generateTestMapMatrix(self, matrix):
        rowStart = self.rows/2 - 2
        colStart = self.cols/2 - 7

        for row in range(rowStart, rowStart+4):
            for col in range(colStart, colStart+14):
                matrix[row][col] = 1

        return matrix

    def generateDiagMapMatrix(self, matrix):
        startX = 12 
        startY = 2
        bigBlockY = 4
        bigBlockX = 6 * 2
    
        #top big block
        for row in range(startY, startY+bigBlockY):
            for col in range(startX, startX+bigBlockX):
                matrix[row][col] = 1

        #top diagonal blocks
        curX = startX + bigBlockX
        curY = startY + bigBlockY
        numLevels = (bigBlockX/2) - 1
        for i in xrange(numLevels):
            curX -= 1 * 2
            curY += 1
            for row in range(startY+bigBlockY, curY):
                for col in range(startX, curX):
                    matrix[row][col] = 1


        #bottom big block
        for row in range(self.rows-bigBlockY-startY, self.rows-startY):
            for col in range(startX, startX+bigBlockX):
                matrix[row][col] = 1
        
        #bottom diagonal blocks
        curX = startX
        curY = self.rows - bigBlockY - startY
        for i in xrange(numLevels):
            curX += 1 * 2
            curY -= 1
            for row in range(curY, self.rows-bigBlockY-startY):
                for col in range(curX,startX+bigBlockX):
                    matrix[row][col] = 1
                    
        return matrix

        
    def generateMatrix(self):
        matrix = []
        for row in range(self.rows): matrix += [[0] * self.cols]
        
        if self.mapID == 1:
            matrix = self.generateTestMapMatrix(matrix)
        if self.mapID == 2:
            matrix = self.generateDiagMapMatrix(matrix)
            self.gx = 28
            self.gy = 4

        return matrix

    #mapID = 0
    def drawBlankMap(self):
        self.canvas.create_rectangle(0, 0, self.width, self.height, fill="white")

    #mapID = 1
    def drawTestMap(self):
        self.canvas.create_rectangle(0, 0, self.width, self.height, fill="white")

        rowStart = self.rows/2 - 2
        colStart = self.cols/2 - 7

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

        #bottom big block
        self.canvas.create_rectangle(startX * self.cellSize, 
                 (self.rows - bigBlockY - startY) * self.cellSize,
                (startX + bigBlockX) * self.cellSize, 
                (self.rows - startY) * self.cellSize,
                 fill="black")
        
        #bottom diagonal blocks
        curX = startX
        curY = self.rows - bigBlockY - startY
        for i in xrange(numLevels):
            curX += 1 * 2
            curY -= 1
            self.canvas.create_rectangle(curX * self.cellSize, 
                curY * self.cellSize, (startX + bigBlockX) * self.cellSize, 
                (self.rows - bigBlockY - startY) * self.cellSize, fill="black")

    def drawGoal(self):
        x = self.gx * self.cellSize
        y = self.gy * self.cellSize
        self.canvas.create_rectangle(x, y, x+self.cellSize, y+self.cellSize, fill = "green")

    def goalReached(self):
        if self.gx == self.robotPos[0] and self.gy == self.robotPos[1]:
            self.isGoalReached = True
            self.canvas.delete(ALL)
            self.canvas.create_text(self.cellSize * (self.cols/2), self.cellSize * (self.rows/2 - 1), font="Times 40 bold",
            text="You have completed this map!")
            self.canvas.create_text(self.cellSize * (self.cols/2), self.cellSize * (self.rows/2 + 1), font="Times 40 bold",
            text="Please wait for the next map to load.")

    def redrawAll(self):
        self.canvas.delete(ALL)
        if self.mapID == 0: self.drawBlankMap()
        if self.mapID == 1: self.drawTestMap()
        if self.mapID == 2: self.drawDiagMap()
        
        self.drawGoal()
        self.drawRobot()

        self.goalReached()

    def initOptModeArray(self):
        self.optMode = [[5 for x in range(self.cols)] for y in range(self.rows)]
        # print (len(self.optMode), len(self.optMode[0]))
        for i in range(self.rows):
            for j in range(self.cols):
                if self.dist[i][j][0] < self.dist[i][j][1]:
                    self.optMode[i][j] = 0
                elif self.dist[i][j][0] > self.dist[i][j][1]:
                    self.optMode[i][j] = 1

        # for mrow in self.optMode:
        #     print mrow

    def initAnimation(self):
        rows = self.rows
        cols = self.cols
        self.isGoalReached = False
        self.matrix = self.generateMatrix()
        self.robotPos = (1, rows/2)
        self.planner = TimeOptPlanner(28, 4, self.rows, self.cols, self.matrix)
        self.planner.dijkstra()
        self.dist = self.planner.dist 
        self.initOptModeArray()
        self.app.setTimerDelay(500)

#map IDs range from 0 to 2
# mapObj = Map(2)
# mapObj.run()
