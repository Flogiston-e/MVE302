from random import random
from math import ceil,floor
import sys

n = int(sys.argv[1])
number_of_runs = int(sys.argv[2])

def grid(side_length,density, epsilon = 10**(-10)):
    grid = set()
    for x in range(ceil(side_length*density + epsilon)):
        for y in range(ceil(side_length*density + epsilon)):
            grid.add((x,y))
    return grid

def add_lily(density, grid,side_length, epsilon = 10**(-10)):
    x, y = random()*side_length*density, random()*side_length*density
    for dx in range(floor(x-density-epsilon), ceil(x+density+epsilon)):
        for dy in range(floor(y-density-epsilon), ceil(y+density+epsilon)):
            if (x-dx)**2 + (y-dy)**2 <= density**2:
                if (dx,dy) in grid:
                    grid.remove((dx,dy))
    return grid

side_length = n**(1/2)
density = 15
runs = []

for _ in range(number_of_runs):
    pond = grid(side_length, density)
    lilys = 0
    while pond:
        pond = add_lily(density, pond, side_length)
        lilys += 1
    runs.append(lilys)

print(runs)
print(sum(runs)/len(runs))