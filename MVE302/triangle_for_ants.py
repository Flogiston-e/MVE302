from random import random
from math import pi,sqrt
import sys

n = int(sys.argv[1])
number_of_runs = int(sys.argv[2])


def lilypad_creator(side_length, side, height):
    x,y = random()*side_length, random()*side_length
    
    corners = [(x, y+(2/3)*height), (x-side/2, y-(1/3)*height), (x+side/2, y-(1/3)*height)]
    return corners

def what_side(c1, c2, p):
    return (p[0]-c2[0])*(c1[1]-c2[1]) - (c1[0]-c2[0])*(p[1]-c2[1])


def pointintriangle(t, p):
    s1 = what_side(t[0], t[1], p) < 0
    s2 = what_side(t[1], t[2], p) < 0
    s3 = what_side(t[2], t[0], p) < 0
    return s1 == s2 == s3

def addLilyPadToPond(side_length, groups, side, height):
    new_lilypad = lilypad_creator(side_length, side, height)
    
    if new_lilypad[1][0] <= 0: touhing_left_edge = True
    else: touhing_left_edge = False

    if new_lilypad[2][0] >= side_length: touhing_right_edge = True
    else: touhing_right_edge = False

    new_lilypad_groups = []
    for id, group in enumerate(groups):
        for lilypad in group[0]:
            if (lilypad[0][0]-new_lilypad[0][0])**2 + (lilypad[0][1]-new_lilypad[0][1])**2 <= side**2:
                intersects = False
                for t1,t2 in [(new_lilypad, lilypad), (lilypad, new_lilypad)]:
                    for p in t1:
                        if pointintriangle(t2, p):
                            intersects = True
                            break
                    if intersects:
                        new_lilypad_groups.append(id)
                        break
                if intersects:
                    break

    if len(new_lilypad_groups) > 0:
        new_lilypad_groups.sort()
        groups[new_lilypad_groups[0]][0].append(new_lilypad)
        for id in new_lilypad_groups[-1:0:-1]:
            merge_group = groups.pop(id)
            groups[new_lilypad_groups[0]][0].extend(merge_group[0])
            groups[new_lilypad_groups[0]][1] = [groups[new_lilypad_groups[0]][1][0] | merge_group[1][0], groups[new_lilypad_groups[0]][1][1] | merge_group[1][1]]
        if touhing_left_edge:
            groups[new_lilypad_groups[0]][1][0] = 1
        if touhing_right_edge:
            groups[new_lilypad_groups[0]][1][1] = 1
    else:
        groups.append([[new_lilypad], [touhing_left_edge, touhing_right_edge]])
    return groups

def checkForCompletePath(groups):
    for group in groups:
        if group[1][0] and group[1][1]:
            return True 
    return False

runs = []
side_length = n**(1/2)
side = 2*sqrt(pi/sqrt(3))
height = sqrt(pi*(sqrt(3)))

for _ in range(number_of_runs):
    groups = []
    for numberOfLilypads in range(1, 100000):
        groups = addLilyPadToPond(side_length, groups, side, height)
        if checkForCompletePath(groups):
            break
    runs.append(numberOfLilypads)

print(runs)
print(sum(runs)/len(runs))