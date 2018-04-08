# Min-Binary Heap Implementation
# 16-467: Human-Robot Interaction

from node import Node

class MinBinaryHeap():
	def __init__(self):
		self.size = 0  # The size of the heap
		self.data = [] # An array of the nodes in the heap

	# Helper function that returns true if the heap is empty
	def is_empty(self):
		return self.size == 0

	# Helper function that compares the g-values of two nodes
	def cmp(self, n1, n2):
		return n1.g <= n2.g

	# Helper function to print the nodes in the heap
	def print_data(self):
		for i in range(0, self.size):
			print "(PQID: " + str(self.data[i].pq_id) + ", G: " + str(self.data[i].g) + ", NID: " + str(self.data[i].id) + ")"
		print "\n"

	# Helper function to print the node cooedinates in the heap
	def print_data_coords(self):
		for i in range(0, self.size):
			print "(X: " + str(self.data[i].x) + ", Y: " + str(self.data[i].y) + ", M: " + str(self.data[i].mode) +  ", G: " + str(self.data[i].g) + ", NID: " + str(self.data[i].id) + ")"
		print "\n"

	# This function inserts a node into the heap
	# node: The node to insert into the heap
	# Returns the node that was inserted
	def insert(self, node):
		idx = self.size
		tmp_idx = idx
		pidx = node.parent(idx)
		self.data.append(node)
		while(not self.is_empty() and pidx > -1  and pidx <= self.size):
			if(self.cmp(self.data[pidx], node)):
				break

			tmp = self.data[idx]
			self.data[idx] = self.data[pidx]
			self.data[pidx] = tmp

			self.data[idx].pq_id = idx
			self.data[pidx].pq_id = pidx

			tmp_idx = idx
			idx = pidx
			pidx = node.parent(idx)

		self.data[tmp_idx].pq_id = tmp_idx
		self.data[tmp_idx].in_pq = True
		self.size += 1
		return self.data[tmp_idx]

	# This function reorders the nodes around a given index
	def min_heapify(self, idx):
		l = 2*idx + 1
		r = 2*idx + 2
		smallest = idx

		if (l < self.size and self.data[l].g < self.data[idx].g):
			smallest = l

		if (r < self.size and self.data[r].g < self.data[smallest].g):
			smallest = r			

		if (smallest != idx):
			tmp = self.data[idx]
			self.data[idx] = self.data[smallest]
			self.data[idx].pq_id = idx
			self.data[smallest] = tmp
			self.data[smallest].pq_id = smallest
			self.min_heapify(smallest)

	# This function returns the node with the lowest priority
	def pop(self):
		if (self.is_empty()):
			print "ERROR: Cannot pop node; the heap is empty\n"
			return

		min_ele = self.data[0]
		min_ele.in_pq = False
		self.data[0].pq_id = 0
		self.size -= 1

		if not self.is_empty():
			self.data[0] = self.data.pop(self.size)
			self.min_heapify(0)
		else:
			self.data.pop(self.size - 1)

		return min_ele

	# This function updates the g-value of a node in the heap
	# node: The node who's g-value needs to be updated
	# new_g: The new g-value
	# Returns the updated node
	def update(self, node, new_g):
		idx = node.pq_id
		self.data[idx].g = new_g
		pidx = node.parent(idx)

		if (self.is_empty() or (not node.in_pq)):
			print "ERROR: This node is not the in heap!\n"
			return

		while idx != 0 and self.data[pidx].g > self.data[idx].g:
			tmp = self.data[pidx]
			self.data[pidx] = self.data[idx]
			self.data[pidx].pq_id = pidx
			self.data[idx] = tmp			
			self.data[idx].pq_id = idx
			idx = pidx
			pidx = node.parent(idx)

		return self.data[idx]


############# TEST CODE ###############
# pq = MinBinaryHeap()

# n1 = Node(0,-1,False,3,0,1,1)
# n2 = Node(1,-1,False,5,1,1,1)
# n3 = Node(2,-1,False,1,0,1,1)
# n4 = Node(3,-1,False,9,0,1,1)

# pq.insert(n1)
# print "size: " + str(pq.size)
# pq.print_data()

# pq.insert(n2)
# print "size: " + str(pq.size)
# pq.print_data()

# pq.insert(n3)
# print "size: " + str(pq.size)
# pq.print_data()

# pq.insert(n4)
# print "size: " + str(pq.size)
# pq.print_data()

# id = pq.update(pq.data[3], 0)
# print "size: " + str(pq.size)
# print "updated priority: " + str(id)
# pq.print_data()

# pq.pop()
# print "size: " + str(pq.size)
# pq.print_data()
#######################################