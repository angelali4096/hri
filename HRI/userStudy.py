from maps import Map
from mazeMap import MazeMap
from itertools import permutations
from random import randint
import argparse

parser = argparse.ArgumentParser(description='Enter the user ID')
parser.add_argument('--userid', type=int, required=True,
                    help='an integer for the user ID')
args = parser.parse_args()

l = list(permutations(range(1, 4)))
idx = randint(0, len(l) - 1)

assistance_order = l[idx]

userID = args.userid

# This map need to terminate with the next button
map1 = Map(2, 1, False)
map1.run()

for i in xrange(len(assistance_order)):
    assistanceType = assistance_order[i]
    if i != len(assistance_order) - 1:
        map2 = MazeMap(userID, assistanceType, False)
    else:
        map2 = MazeMap(userID, assistanceType, True)
    map2.run()
