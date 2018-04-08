
class OccupancyGrid(object):

	def __init__(self, mapID):
		map = Map(mapID)
		self.size_x = map.rows
		self.size_y = map.cols
		self.grid = map.matrix


	def is_valid(self, x, y):
		return (0 <= x && x < self.size_x && 0 <= y && y < self.size_y && self.grid[x][y])

	def get_succ(self, x, y):
		neighbors = []
		if (is_valid(x - 1, y)): neighbors.append((x - 1, y))
		if (is_valid(x + 1, y)): neighbors.append((x + 1, y))
		if (is_valid(x, y - 1)): neighbors.append((x, y - 1))
		if (is_valid(x, y + 1)): neighbors.append((x, y + 1))
		return neighbors

