from maps import Map
from mazeMapPartiallyVisible import MazeMapPartiallyVisible
from mazeMapFullyVisible import MazeMapFullyVisible
from itertools import permutations
from random import randint
import argparse
import time

parser = argparse.ArgumentParser(description='Enter the user ID')
parser.add_argument('--userid', type=int, required=True,
                    help='an integer for the user ID')
args = parser.parse_args()

l = list(permutations(range(1, 4)))

idx = randint(0, len(l) - 1)
assistance_order_partial = l[idx]

idx = randint(0, len(l) - 1)
assistance_order_full = l[idx]

userID = args.userid

map1 = Map(2, 1)
map1.run()
time.sleep(2)

for i in xrange(len(assistance_order_full)):
    assistanceTypeFull = assistance_order_full[i]
    assistanceTypePartial = assistance_order_partial[i]
    if i != len(assistance_order_full) - 1:
        map2 = MazeMapFullyVisible(userID, assistanceTypeFull, False)
        map2.run()
        time.sleep(2)

        map2 = MazeMapPartiallyVisible(userID, assistanceTypePartial, False)
        map2.run()
        time.sleep(2)
    else:
        map2 = MazeMapFullyVisible(userID, assistanceTypeFull, False)
        map2.run()
        time.sleep(2)

        map2 = MazeMapPartiallyVisible(userID, assistanceTypePartial, True)
        map2.run()
