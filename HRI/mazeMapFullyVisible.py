from Tkinter import *
from basicAnimationClass import BasicAnimationClass
from timeOptPlanner import TimeOptPlanner
from random import *
from time import *
import yaml

class MazeMapFullyVisible(BasicAnimationClass):
    def __init__(self, userID, assistanceType, lastMap):
        self.lastMap = lastMap
        self.rows = 37
        self.cols = 58
        self.gx = 47
        self.gy = 16
        self.cellSize = 15
        canvasWidth = self.cellSize * self.cols
        canvasHeight = self.cellSize * self.rows
        super(MazeMapFullyVisible, self).__init__(canvasWidth, canvasHeight)
        self.assistanceType = assistanceType #randint(1,3) # randomly assigns assistance type
        self.mode = "vertical" # This is the mode the user is currently using
        self.zone = 1 # This is the optimal mode zone based on the optimality map
        self.moveNum = 0
        self.userID = userID
        self.mapID = 1
        self.dataFile = "test_" + str(self.userID) + "_" + str(self.assistanceType) + "_" + str(self.mapID) + ".yml"

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

    def drawRobot(self):
        x = self.robotPos[0] * self.cellSize
        y = self.robotPos[1] * self.cellSize
        self.canvas.create_rectangle(x, y, x+self.cellSize, y+self.cellSize, fill="blue")

        if self.mode == "vertical":
            self.canvas.create_rectangle((x+self.cellSize/2)-2, y+2, (x+self.cellSize/2)+2, y+self.cellSize-2, fill="yellow")
        if self.mode == "horizontal":
            self.canvas.create_rectangle(x+2, (y+self.cellSize/2)-2, x+self.cellSize-2, (y+self.cellSize/2)+2, fill="yellow")

    def drawGoal(self):
        x = self.gx * self.cellSize
        y = self.gy * self.cellSize
        self.canvas.create_rectangle(x, y, x+self.cellSize, y+self.cellSize, fill="green")

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

        if self.zone == 0:
            zonestr = "vertical"
        else:
            zonestr = "horizontal"

        key = "move" + str(self.moveNum)
        info = "general info"
        filename = "test/" + self.dataFile
        with open(filename, 'a') as yaml_file:
            if (self.moveNum == 0):
                info = {info : {"assistance_type" : self.assistanceType, \
                               "user_id" : self.userID,\
                               "map_id" : self.mapID}}
                yaml.dump(info, yaml_file, default_flow_style=False)
            data = {key: {"x" : str(self.robotPos[0]), \
                          "y": str(self.robotPos[1]), \
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

            if (x > self.cellSize*(self.cols/2-6) and y > self.cellSize*(self.rows/2 + 6.5) and
                x < self.cellSize*(self.cols/2+6) and y < self.cellSize*(self.rows/2+9.5)):
                self.continueClicked = True

    def generateMatrix(self):
        matrix = []
        for row in range(self.rows): matrix += [[0] * self.cols]

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
        self.canvas.create_rectangle(0, 0, self.cols*self.cellSize, self.rows*self.cellSize, fill="white")
        for row in range(self.rows):
            for col in range(self.cols):
                if self.matrix[row][col] == 1:
                    self.canvas.create_rectangle(col*self.cellSize, row*self.cellSize,
                        (col+1)*self.cellSize, (row+1)*self.cellSize, fill="black")

    def goalReached(self):
        if self.gx == self.robotPos[0] and self.gy == self.robotPos[1]:
            self.isGoalReached = True
            self.canvas.delete(ALL)
            if self.lastMap == False:
                self.canvas.create_text(self.cellSize * (self.cols/2), self.cellSize * (self.rows/2 - 8), font="Times 30 bold",
                text="You have completed this map!")
                self.canvas.create_text(self.cellSize * (self.cols/2), self.cellSize * (self.rows/2 - 4), font="Times 30 bold",
                text="Before clicking continue, please fill out")
                self.canvas.create_text(self.cellSize * (self.cols/2), self.cellSize * (self.rows/2 ), font="Times 30 bold",
                text=" the survey in the other tab using the")
                self.canvas.create_text(self.cellSize * (self.cols/2), self.cellSize * (self.rows/2 + 4), font="Times 30 bold",
                text = "following version ID <" + self.versionID + "> and user ID <" + str(self.userID) + ">.")
                self.canvas.create_rectangle(self.cellSize*(self.cols/2-6), self.cellSize*(self.rows/2 + 6.5),
                                            self.cellSize*(self.cols/2+6), self.cellSize*(self.rows/2+9.5), fill="green")
                self.canvas.create_text(self.cellSize * (self.cols/2), self.cellSize * (self.rows/2 +8), font="Times 30 bold",
                text="Continue")
            else:
                self.canvas.create_text(self.cellSize * (self.cols/2), self.cellSize * (self.rows/2 - 1), font="Times 30 bold",
                text="You have completed the study.")
                self.canvas.create_text(self.cellSize * (self.cols/2), self.cellSize * (self.rows/2 + 1), font="Times 30 bold",
                text="Thank you for participating!")

    def redrawAll(self):
        self.canvas.delete(ALL)
        self.drawMap()
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

    def setVersionID(self):
        num = ""
        if self.assistanceType == 1:
            num = "574"
        elif self.assistanceType == 2:
            num = "483"
        else:
            num = "216"
        return num


    def initAnimation(self):
        self.matrix = self.generateMatrix()
        self.robotPos = (1, 4)
        self.versionID = self.setVersionID()
        self.planner = TimeOptPlanner(self.gx, self.gy, self.rows, self.cols, self.matrix)
        self.planner.dijkstra()
        self.dist = self.planner.dist
        self.initOptModeArray()
        self.continueClicked = False
        self.isGoalReached = False
        self.app.setTimerDelay(500)

# mapObj = MazeMapFullyVisible(1, 2, False)
# mapObj.run()
