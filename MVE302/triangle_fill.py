from random import random
from math import ceil,pi,sqrt
import sys

n = int(sys.argv[1])
number_of_runs = int(sys.argv[2])


def grid(side_length, density, epsilon = 10**(-10)):
    grid = set()
    for x in range(ceil(side_length*density + epsilon)):
        for y in range(ceil(side_length*density + epsilon)):
            grid.add((x,y))
    return grid

def lilypad_creator(side_length, density, side, height):
    x,y = random()*side_length, random()*side_length
    corners = [(x*density, (y+(2/3)*height)*density), ((x-side/2)*density, (y-(1/3)*height)*density), ((x+side/2)*density, (y-(1/3)*height)*density)]
    return corners

def what_side(c1,c2,p):
    return (p[0]-c2[0])*(c1[1]-c2[1]) - (c1[0]-c2[0])*(p[1]-c2[1])


def pointintriangle(t,p):
    s1 = what_side(t[0], t[1], p) < 0
    s3 = what_side(t[2], t[0], p) < 0
    return s1 == s3
     

def add_lily(density, grid, side_length, side, height): 
    new_lilypad = lilypad_creator(side_length,density,side,height)
    min_x, max_x = new_lilypad[1][0], new_lilypad[2][0]
    min_y, max_y = new_lilypad[1][1], new_lilypad[0][1]
    for dx in range(ceil(min_x),ceil(max_x)):
        for dy in range(ceil(min_y),ceil(max_y)):
            if pointintriangle(new_lilypad,(dx,dy)):
                if (dx,dy) in grid:
                    grid.remove((dx,dy))
    return grid

side_length = n**(1/2)
density = 10
runs = []
side = 2*sqrt(pi/sqrt(3))
height = sqrt(pi*(sqrt(3)))

for _ in range(number_of_runs):
    pond = grid(side_length, density)
    lilys = 0
    while pond:
        pond = add_lily(density, pond, side_length, side, height)
        lilys += 1
    runs.append(lilys)

print(runs)
print(sum(runs)/len(runs))