from random import random
import sys

n = int(sys.argv[1])
number_of_runs = int(sys.argv[2])

def addLilyPadToPond(side_length, groups):
    new_lilypad = (random()*side_length, random()*side_length)

    if new_lilypad[0] - 1 <= 0: touhing_left_edge = True
    else: touhing_left_edge = False

    if new_lilypad[0] + 1 >= side_length: touhing_right_edge = True
    else: touhing_right_edge = False

    new_lilypad_groups = []
    for id, group in enumerate(groups):
        for lilypad in group[0]:
            if (lilypad[0]-new_lilypad[0])**2 + (lilypad[1]-new_lilypad[1])**2 <= 2**2:
                new_lilypad_groups.append(id)
                break

    if len(new_lilypad_groups) > 0:
        new_lilypad_groups.sort()
        groups[new_lilypad_groups[0]][0].append(new_lilypad)
        for id in new_lilypad_groups[-1:1:-1]:
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
        if group[1][0]&group[1][1]:
            return True
    return False

runs = []
side_length = n**(1/2)

for _ in range(number_of_runs):
    groups = []
    for numberOfLilypads in range(1, 100000):
        groups = addLilyPadToPond(side_length, groups)
        if checkForCompletePath(groups):
            break
    runs.append(numberOfLilypads)

print(runs)
print(sum(runs)/len(runs))