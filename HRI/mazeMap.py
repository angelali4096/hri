"""
TO DO:
arrow on robot to indicate mode
goal square
"""

from Tkinter import *
from basicAnimationClass import BasicAnimationClass
from timeOptPlanner import TimeOptPlanner
from random import *

class MazeMap(BasicAnimationClass):
    def __init__(self):
        self.cellSize = 30
        canvasWidth = self.cellSize * 20
        canvasHeight = self.cellSize * 20
        super(MazeMap, self).__init__(canvasWidth, canvasHeight)
        self.canvasRows = 20
        self.canvasCols = 20
        self.assistanceType = 2 #randint(1,3) # randomly assigns assistance type 
        self.mode = "vertical" # This is the mode the user is currently using
        self.zone = 1 # This is the optimal mode zone based on the optimality map

    def getOptMode(self):
        if self.assistanceType == 1:
            return self.mode

        elif self.assistanceType == 2:
            if self.optMode[self.robotMatrixPos[1]][self.robotMatrixPos[0]] != self.zone:
                if self.zone == 0:
                    self.zone = 1
                    return "vertical"
                else:
                    self.zone = 0
                    return "horizontal"
            return self.mode

        elif self.assistanceType == 3:
            if self.optMode[self.robotMatrixPos[1]][self.robotMatrixPos[0]] == 0:
                return "horizontal"
            else:
                return "vertical"

    def drawRobot(self):
        x = self.robotCanvasPos[0] * self.cellSize
        y = self.robotCanvasPos[1] * self.cellSize
        self.canvas.create_rectangle(x, y, x+self.cellSize, y+self.cellSize, fill="blue")

    def drawGoal(self):
        x = (55 - self.xOffsetCanvas) * self.cellSize
        y = (3 - self.yOffsetCanvas) * self.cellSize
        self.canvas.create_rectangle(x, y, x+self.cellSize, y+self.cellSize, fill="green")

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
        
    def generateMatrix(self):
        self.gx = 55
        self.gy = 3

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

    def goalReached(self):
        if self.gx == self.robotMatrixPos[0] and self.gy == self.robotMatrixPos[1]:
            self.isGoalReached = True

    def redrawAll(self):
        self.canvas.delete(ALL)
        self.drawMap()
        self.drawGoal()
        self.drawRobot()

        self.goalReached()

    def initOptModeArray(self):
        self.optMode = [[5 for x in range(self.matrixCols)] for y in range(self.matrixRows)]
        # print (len(self.optMode), len(self.optMode[0]))
        for i in range(self.matrixRows):
            for j in range(self.matrixCols):
                if self.dist[i][j][0] < self.dist[i][j][1]:
                    self.optMode[i][j] = 0
                elif self.dist[i][j][0] > self.dist[i][j][1]:
                    self.optMode[i][j] = 1

        # for mrow in self.optMode:
        #     print mrow

    def initAnimation(self):
        self.matrixRows = 37
        self.matrixCols = 58
        self.xOffsetCanvas = 0
        self.yOffsetCanvas = 0
        self.matrix = self.generateMatrix()
        self.robotMatrixPos = (1, 4)
        self.robotCanvasPos = (1, 4)
        self.planner = TimeOptPlanner(55, 3, self.matrixRows, self.matrixCols, self.matrix)
        self.planner.dijkstra()
        self.dist = self.planner.dist 
        self.initOptModeArray()
        self.isGoalReached = False
        self.app.setTimerDelay(500)
        
# mapObj = MazeMap()
# mapObj.run()