from Tkinter import *
from basicAnimationClass import BasicAnimationClass
from timeOptPlanner import TimeOptPlanner
from random import *
from time import *
import yaml

class MazeMapPartiallyVisible(BasicAnimationClass):
    def __init__(self, userID, assistanceType, lastMap):
        self.lastMap = lastMap
        self.cellSize = 30
        canvasWidth = self.cellSize * 20
        canvasHeight = self.cellSize * 20
        super(MazeMapPartiallyVisible, self).__init__(canvasWidth, canvasHeight)
        self.canvasRows = 20
        self.canvasCols = 20
        self.assistanceType = assistanceType #randint(1,3) # randomly assigns assistance type
        self.mode = "vertical" # This is the mode the user is currently using
        self.zone = 1 # This is the optimal mode zone based on the optimality map
        self.moveNum = 0
        self.userID = userID
        self.mapID = 2
        self.dataFile = "test_" + str(self.userID) + "_" + str(self.assistanceType) + "_" + str(self.mapID) + ".yml"

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

        if self.mode == "vertical":
            self.canvas.create_rectangle((x+self.cellSize/2)-2, y+5, (x+self.cellSize/2)+2, y+self.cellSize-5, fill="yellow")
        if self.mode == "horizontal":
            self.canvas.create_rectangle(x+5, (y+self.cellSize/2)-2, x+self.cellSize-5, (y+self.cellSize/2)+2, fill="yellow")

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

        if self.zone == 0:
            zonestr = "vertical"
        else:
            zonestr = "horizontal"

        key = "move" + str(self.moveNum)
        info = "general info"
        filename = "test/" + self.dataFile
        with open(filename, 'a') as yaml_file:
            if (self.moveNum == 0):
                info = {info : {"assistance type" : self.assistanceType, \
                                "user id" : self.userID,\
                                "map id" : self.mapID}}
                yaml.dump(info, yaml_file, default_flow_style=False)
            data = {key: {"x" : str(self.robotMatrixPos[0]), \
                          "y": str(self.robotMatrixPos[1]), \
                          "zone": zonestr, \
                          "mode": self.mode, \
                          "time": str(time()), \
                          "keypress": event.keysym}}
            yaml.dump(data, yaml_file, default_flow_style=False)

        self.moveNum += 1
        # only for testing
        # if event.keysym == "Up": self.moveRobot(0, -1)
        # if event.keysym == "Down": self.moveRobot(0, 1)
        # if event.keysym == "Right": self.moveRobot(1, 0)
        # if event.keysym == "Left": self.moveRobot(-1, 0)

    def onMousePressed(self, event):
        if self.isGoalReached:
            x = event.x
            y = event.y

            if (x > self.cellSize*(self.canvasCols/2-3) and y > self.cellSize*(self.canvasRows/2 + 3.25) and
                x < self.cellSize*(self.canvasCols/2+3) and y < self.cellSize*(self.canvasRows/2+4.75)):
                self.continueClicked = True

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
            for row in range(7,37):
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
            self.canvas.delete(ALL)
            if self.lastMap == False:
                self.canvas.create_text(self.cellSize * (self.canvasCols/2), self.cellSize * (self.canvasRows/2 - 4), font="Times 20 bold",
                text="You have completed this map!")
                self.canvas.create_text(self.cellSize * (self.canvasCols/2), self.cellSize * (self.canvasRows/2 - 2), font="Times 20 bold",
                text="Before clicking continue, please fill out")
                self.canvas.create_text(self.cellSize * (self.canvasCols/2), self.cellSize * (self.canvasRows/2 ), font="Times 20 bold",
                text=" the survey in the other tab using the")
                self.canvas.create_text(self.cellSize * (self.canvasCols/2), self.cellSize * (self.canvasRows/2 + 2), font="Times 20 bold",
                text = "following version ID <" + self.versionID + "> and user ID <" + str(self.userID) + ">.")
                self.canvas.create_rectangle(self.cellSize*(self.canvasCols/2-3), self.cellSize*(self.canvasRows/2 + 3.25),
                                            self.cellSize*(self.canvasCols/2+3), self.cellSize*(self.canvasRows/2+4.75), fill="green")
                self.canvas.create_text(self.cellSize * (self.canvasCols/2), self.cellSize * (self.canvasRows/2 +4), font="Times 20 bold",
                text="Continue")
            else:
                self.canvas.create_text(self.cellSize * (self.canvasCols/2), self.cellSize * (self.canvasRows/2 - 1), font="Times 20 bold",
                text="You have completed the study.")
                self.canvas.create_text(self.cellSize * (self.canvasCols/2), self.cellSize * (self.canvasRows/2 + 1), font="Times 20 bold",
                text="Thank you for participating!")

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

    def setVersionID(self):
        num = ""
        if self.assistanceType == 1:
            num = "102"
        elif self.assistanceType == 2:
            num = "281"
        else:
            num = "819"
        return num


    def initAnimation(self):
        self.matrixRows = 37
        self.matrixCols = 58
        self.xOffsetCanvas = 0
        self.yOffsetCanvas = 0
        self.matrix = self.generateMatrix()
        self.robotMatrixPos = (1, 4)
        self.robotCanvasPos = (1, 4)
        self.versionID = self.setVersionID()
        self.planner = TimeOptPlanner(55, 3, self.matrixRows, self.matrixCols, self.matrix)
        self.planner.dijkstra()
        self.dist = self.planner.dist
        self.initOptModeArray()
        self.continueClicked = False
        self.isGoalReached = False
        self.app.setTimerDelay(500)

# mapObj = MazeMapPartiallyVisible(1, 1, False)
# mapObj.run()
