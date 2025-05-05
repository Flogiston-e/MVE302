from random import random
from shapely.geometry import Polygon
from math import pi,sqrt


def lilypad_creator(side_length):
    x,y = random()*side_length, random()*side_length
    side = 2*sqrt(pi/sqrt(3))
    height = sqrt(pi*(sqrt(3)))
    corners = [(x, y+(2/3)*height), (x-side/2, y-(1/3)*height), (x+side/2, y-(1/3)*height)]
    return corners

def addLilyPadToPond(side_length,groups):
    new_lilypad = lilypad_creator(side_length)
    polygon_lilypad = Polygon(new_lilypad)
    
    if new_lilypad[1][0] <= 0: touhing_left_edge = True
    else: touhing_left_edge = False

    if new_lilypad[2][0] >= side_length: touhing_right_edge = True
    else: touhing_right_edge = False

    new_lilypad_groups = []
    for id,group in enumerate(groups):
        for lilypad in group[0]:
            if lilypad.intersects(polygon_lilypad):
                new_lilypad_groups.append(id)
                break

    if len(new_lilypad_groups) > 0:
        new_lilypad_groups.sort()
        groups[new_lilypad_groups[0]][0].append(polygon_lilypad)
        for id in new_lilypad_groups[-1:1:-1]:
            merge_group = groups.pop(id)
            groups[new_lilypad_groups[0]][0].extend(merge_group[0])
            groups[new_lilypad_groups[0]][1] = [groups[new_lilypad_groups[0]][1][0] | merge_group[1][0], groups[new_lilypad_groups[0]][1][1] | merge_group[1][1]]
        if touhing_left_edge:
            groups[new_lilypad_groups[0]][1][0] = 1
        if touhing_right_edge:
            groups[new_lilypad_groups[0]][1][1] = 1
    else:
        groups.append([[polygon_lilypad],[touhing_left_edge,touhing_right_edge]])
    return groups

def checkForCompletePath(groups):
    for group in groups:
        if group[1][0]&group[1][1]:
            return True 
    return False

runs = []
n = 100
side_length = n**(1/2)

for _ in range(100):
    groups = []
    for numberOfLilypads in range(1,100000):
        groups = addLilyPadToPond(side_length,groups)
        if checkForCompletePath(groups):
            break
    runs.append(numberOfLilypads)

print(runs)
print(sum(runs)/len(runs))