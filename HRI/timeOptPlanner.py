from node import Node
from minBinaryHeap import MinBinaryHeap
import math as Math

class TimeOptPlanner(object):

    def __init__(self, gx, gy, rows, cols, matrix):
        # Swap start and end nodes for backwards dijkstra search
        self.rows = rows
        self.cols = cols
        self.matrix = matrix
        self.heap = MinBinaryHeap()
        self.visited = [[[None for z in range(2)] for y in range(self.cols)] for x in range(self.rows)]
        # print (len(self.visited), len(self.visited[0]), len(self.visited[0][0]))
        self.dXmX = [1, -1, 0]
        self.dYmX = [0, 0, 0]
        self.mX = [0, 0, 1]
        self.dXmY = [0, 0, 0]
        self.dYmY = [1, -1, 0]
        self.mY = [1, 1, 0]
        self.costs = [1, 1, 1.5]
        self.numDir = 3
        self.numNodes = self.rows * self.cols
        goal_node_id = (gy * self.cols + gx) + self.numNodes * 0
        goal_node = Node(goal_node_id, -1, False, 0, gx, gy, 0)
        self.start = goal_node

        # Initialize distance map for every (x, y, mode) to infinity
        self.dist = [[[float('inf') for z in range(2)] for y in range(self.cols)] for x in range(self.rows)] 

    # Returns true the (x, y) position in the map is valid 
    # 1 - obstacle
    # 0 - free
    def is_valid(self, x, y):
        # print (x, y)
        return (0 <= x and x < self.cols and 0 <= y and \
            y < self.rows and not(self.matrix[y][x]))

    # This function gets the successors/neighbors for the given node
    # Returns the neighbor nodes and the associated transition costs
    def get_succ(self, node):
        neighbors = []
        costs = []

        if (node.mode == 0):
            dx = self.dXmX
            dy = self.dYmX
            dm = self.mX
        else: 
            dx = self.dXmY
            dy = self.dYmY
            dm = self.mY

        for i in xrange(self.numDir):
            newX = node.x + dx[i]
            newY = node.y + dy[i]
            newM = dm[i]
            if (self.is_valid(newX, newY)):
                if (self.visited[newY][newX][newM] != None):
                    newNode = self.visited[newY][newX][newM]
                else:
                    newNodeId = (newY * self.cols + newX) + self.numNodes * newM
                    newNode = Node(newNodeId, -1, False, 0, newX, newY, newM)
                costs.append(self.costs[i])
                neighbors.append(newNode)

        return (neighbors, costs)


    # This function runs dijkstra's algorithm till completion (i.e. all nodes have been expanded)
    def dijkstra(self):        
        # Initialize the start node's distance to 0; add to visited map and heap
        self.dist[self.start.y][self.start.x][self.start.mode] = 0
        self.visited[self.start.y][self.start.x][self.start.mode] = self.start
        self.heap.insert(self.start)

        # Run algorithm until heap in empty
        while (not(self.heap.is_empty())):
            u = self.heap.pop()
            (neighbors, costs) = self.get_succ(u)
            if len(neighbors) != len(costs):
                print "ERROR: Number of successors does not equal number of costs"

            for i in xrange(len(neighbors)):
                alt = u.g + costs[i]
                dist_v = self.dist[neighbors[i].y][neighbors[i].x][neighbors[i].mode]
                v = self.visited[neighbors[i].y][neighbors[i].x][neighbors[i].mode]
                
                # If successor has not been visited, add it to the heap
                if v == None:
                    neighbors[i].g = alt
                    new = self.heap.insert(neighbors[i])
                    self.visited[neighbors[i].y][neighbors[i].x][neighbors[i].mode] = new
                    self.dist[neighbors[i].y][neighbors[i].x][neighbors[i].mode] = new.g
                
                # If the successor has been visited and the newly calculated g-value is less
                # than that stored in the heap, update the value
                elif (alt < dist_v and v.in_pq):
                    new = self.heap.update(neighbors[i], alt)
                    self.visited[neighbors[i].y][neighbors[i].x][neighbors[i].mode] = new
                    self.dist[neighbors[i].y][neighbors[i].x][neighbors[i].mode] = new.g


        # row = []
        # for mrow in self.dist:
        #     for mcol in mrow:
        #         row.append(mcol[0])
        #     print row
        #     row = []

        # print "\n"

        # row = []
        # for mrow in self.dist:
        #     for mcol in mrow:
        #         row.append(mcol[1])
        #     print row
        #     row = []    

################### TEST CODE ####################
# start = Node(0,-1,False, 0, 0, 1, 1)
# end = Node(0, -1, False, 0, 1, 0, 0)

# planner = TimeOptPlanner(start, end, 1)
# print "START: " + str(planner.map.matrix[0][1])
# print "GOAL: " + str(planner.map.matrix[1][1])

# planner.dijkstra()
###################################################







