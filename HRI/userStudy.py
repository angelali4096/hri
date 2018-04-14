from maps import Map
from timeOptPlanner import TimeOptPlanner
from random import *
from node import Node
import math
from Tkinter import *
from basicAnimation import BasicAnimationRunner

class UserStudy():
    # Override these methods (or not)
    # def onMousePressed(self, event): pass
    # def onKeyPressed(self, event): pass
    # def onTimerFired(self): pass
    # def redrawAll(self): pass
    # def initAnimation(self): pass

    def __init__(self, Map):
        self.map = Map
        self.matrix = Map.matrix
        self.width = 300
        self.height = 300
        self.assistance_type = randint(1, 3)
        start_x = 1
        start_y = 10
        start_mode = 1
        start_id = start_y * self.map.cols + start_x
        goal_x = 27
        goal_y = 5
        goal_mode = 1
        goal_id = goal_y * self.map.cols + goal_x
        self.start_node = Node(start_id ,-1,False, 0, start_x, start_y, start_mode)
        self.goal_node = Node(goal_id, -1, False, float('inf'), goal_x, goal_y, goal_mode)
        self.robotPos = (start_x, start_y)
        self.map.initDiagMapMatrix()
        self.matrix = self.map.matrix 
        self.planner = TimeOptPlanner(self.goal_node, self.start_node, self.map, self.matrix)
        self.planner.dijkstra()
        self.mode_vals = self.planner.visited
        print self.planner.dist
    # Returns the node id given the coordinates and mode
    def get_node_id(self, x, y, mode):
        return (y * self.map.cols) + x + ((self.map.cols * self.map.rows) * mode)

    # Get the optimal/suboptimal mode when robot provides assistance
    # TODO: Implement suboptimal
    def get_assistance_mode(self, x, y, optimal):
        h_mode_val = self.mode_vals[x][y][0]
        v_mode_val = self.mode_vals[x][y][1]
        if h_mode_val.g < v_mode_val.g:
            return "horizontal"
        return "vertical"

    def moveRobot(self, xChange, yChange):
        (x, y) = self.robotPos
        newRobotPos = (x+xChange, y+yChange)
        if (newRobotPos[0] < self.planner.map.cols and newRobotPos[1] < self.planner.map.rows 
            and newRobotPos[0] >= 0 and newRobotPos[1] >= 0
            and self.planner.map.matrix[newRobotPos[1]][newRobotPos[0]] == 0):
                self.robotPos = newRobotPos
                print self.robotPos

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

    # 1 - Manual
    # 2 - Automatic
    # 3 - Forced
    # def assistance_type(self, type):
    #     if type == 3:

    # In general, you would probably not override this method (but you could)
    def run(self):
        def myBasicAnimation(app, canvas):
            self.app = app
            self.canvas = canvas
            self.initAnimation()
            while app.isRunning():
                (eventType, event) = app.getEvent()
                if (eventType == "mousePressed"): self.onMousePressed(event)
                elif (eventType == "keyPressed"): self.onKeyPressed(event)
                elif (eventType == "timerFired"): self.onTimerFired()
                self.redrawAll()
            print "Done!"
        BasicAnimationRunner(myBasicAnimation, width=self.width, height=self.height)

m = Map(2)
study = UserStudy(m)
m.run()

