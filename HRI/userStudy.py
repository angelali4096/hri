from maps import Map
from mazeMap import MazeMap
from itertools import permutations
from random import randint

l = list(permutations(range(1, 4)))
idx = randint(0, len(l) - 1)

assistance_order = l[idx]

# map1 = Map(1)
# map1.run()

# map2 = MazeMap()
# map2.run()

for i in assistance_order:
    map3 = Map(2, i)
    map3.run()


