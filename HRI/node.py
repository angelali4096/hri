# Graph-Node Implemenation 
# 16-467: Human-Robot Interaction

class Node:
	def __init__(self, nid, pq_id, in_pq, g, x, y, mode):
		self.id = nid 			  # The node ID
		self.pq_id = pq_id        # The nodes index/priority in the priority queue
		self.in_pq = in_pq		  # Whether or not the node is in the priority queue
		self.g = g    			  # The g-value for the node
		self.x = x    			  # The x coordinate 
		self.y = y 	  			  # The y coordinate
		self.mode = mode		  # The mode (horizontal or vertical)

	def parent(self, idx):
		return (idx - 1)/2

	def left(self, idx):
		return 2*idx + 1

	def right(self, idx):
		return 2*idx + 2

