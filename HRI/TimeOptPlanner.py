from minBinaryHeap import MinBinaryHeap
from maps import Map
import numpy as np
import math

class TimeOptPlanner(object):

	def __init__(self, start_node, end_node, mapID):
		self.start = start_node
		self.end = end_node
		self.map = Map(mapID)
		self.visited = [[[None for z in range(2)] for y in range(self.map.cols)] for x in range(self.map.rows)]
	
	def is_valid(self, x, y):
		return (0 <= x && x < self.map.rows && 0 <= y && \
			y < self.map.cols && self.map.matrix[x][y])

	def get_succ(self, node):
		neighbors = []
		numNodes = self.map.rows * self.map.cols
		if (node.mode == 0): # horizontal
			if (is_valid(node.x - 1, y)): 
				if (self.visited[node.x - 1][node.y][node.mode] != None):
					oldNode = self.visited[node.x - 1][node.y][node.mode]
					newNode = heap.update(oldNode, oldNode.g + 1)
				else:
					newNodeId = node.y * self.map.cols + (node.x - 1)
					newNode = Node(newNodeId, -1, False, node.g + 1, node.x - 1, node.y, node.mode)
				neighbors.append(newNode)
			
			if (is_valid(x + 1, y)):
				if (self.visited[node.x + 1][node.y][node.mode] != None):
					oldNode = self.visited[node.x + 1][node.y][node.mode]
					newNode = heap.update(oldNode, oldNode.g + 1)
				else:
					newNodeId = node.y * self.map.cols + (node.x + 1)
					newNode = Node(newNodeId, -1, False, node.g + 1, node.x + 1, node.y, node.mode)
				neighbors.append(newNode)
			
			if (self.visited[node.x][node.y][1 - node.mode] != None):
				oldNode = self.visited[node.x][node.y][1 - node.mode]
				newNode = heap.update(oldNode, oldNode.g + 1.5)
			else:
				newNode = Node(node.id + numNodes, -1, False, node.g + 1.5, node.x, node.y, 1 - node.mode)
				neighbors.append(newNode)
		else :
			if (is_valid(x, y - 1)): 
				if (self.visited[node.x][node.y - 1][node.mode] != None):
					oldNode = self.visited[node.x][node.y - 1][node.mode]
					newNode = heap.update(oldNode, oldNode.g + 1)
				else:
					newNodeId = (node.y - 1) * self.map.cols + (node.x) + numNodes
					newNode = Node(newNodeId, -1, False, node.g + 1, node.x, node.y - 1, node.mode)
				neighbors.append(newNode)
			
			if (is_valid(x, y + 1)): neighbors.append((x, y + 1)):
				if (self.visited[node.x][node.y + 1][node.mode] != None):
					oldNode = self.visited[node.x][node.y + 1][node.mode]
					newNode = heap.update(oldNode, oldNode.g + 1)
				else:
					newNodeId = (node.y + 1) * self.map.cols + (node.x) + numNodes
					newNode = Node(newNodeId, -1, False, node.g + 1, node.x, node.y + 1, node.mode)
				neighbors.append(newNode)

			if (self.visited[node.x][node.y][1 - node.mode] != None):
				oldNode = self.visited[node.x][node.y][1 - node.mode]
				newNode = heap.update(oldNode, oldNode.g + 1.5)
			else:
				newNode = Node(node.id - numNodes, -1, False, node.g + 1.5, node.x, node.y, 1 - node.mode)
				neighbors.append(newNode)

		return (neighbors, gvals)


	def dijkstra(self, heap):

		dist = [[[Math.inf for z in range(2)] for y in range(self.map.cols)] for x in range(self.map.rows)] 
		dist[self.start.x][self.start.y][self.start.mode] = 0
		
		self.visited[self.start.x][self.start.y][self.start.mode] = self.start
		
		heap.insert(self.start)
		while !heap.is_empty()
			u = heap.pop()
			neighbors = self.get_succ(u)
			for neighbor in neighbors:
				alt = neighbor.g
				if (alt < dist(neighbor.x, neighbor.y, neighbor.mode)):
					new = heap.update(neighbor, alt)
				else:
					new = heap.insert(neighbor)
				self.visited[neighbor.x][neighbor.y][neighbor.mode] = new
				dist[neighbor.x][neighbor.y][neighbor.mode] = new.g
		printf(dist[self.end.x][self.end.y][self.end.mode])

start = Node(0,-1,False,0,0,1,1)
end = Node(0, -1, False, 0, 1, 1, 1)
pq = MinBinaryHeap()

planner = TimeOptPlanner(start, end, 1)
dijkstra(pq)








