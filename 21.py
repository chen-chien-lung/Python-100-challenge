# Question 21
# Level 3
#
# Question£º
# A robot moves in a plane starting from the original point (0,0).
# The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
# The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# ¡­
# The numbers after the direction are steps.
# Please write a program to compute the distance from current position after a sequence of movement and original point.
# If the distance is a float, then just print the nearest integer.
# Example:
# If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 2

distance = 0

while True:
    s = input()
    if not s:
        break
    v = 0
    h = 0
    steps = s.split(" ")
    if steps[0] == "UP":
        v += int(steps[1])
    elif steps[0] == "DOWN":
        v -= int(steps[1])
    elif steps[0] == "LEFT":
        h += int(steps[1])
    elif steps[0] == "RIGHT":
        h -= int(steps[1])
    else:
        pass

    distance = round((h**2 + v**2)**(1/2))

print(distance)