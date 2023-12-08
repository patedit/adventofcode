from advent import Advent

advent = Advent(2021, 2)
FORWARD = 'forward'
DOWN = 'down'
UP = 'up'

# Part 1
instructions = [{line.split(' ')[0] : int(line.split(' ')[1])} for line in advent.lines]

f = 0
d = 0
for instruction in instructions:
    if FORWARD in instruction:
        f += instruction[FORWARD]
    elif DOWN in instruction:
        d += instruction[DOWN]
    elif UP in instruction:
        d -= instruction[UP]
print(f*d)

# Part 2
f = 0
d = 0
a = 0
for instruction in instructions:
    if FORWARD in instruction:
        f += instruction[FORWARD]
        d += a * instruction[FORWARD]
    elif DOWN in instruction:
        a += instruction[DOWN]
    elif UP in instruction:
        a -= instruction[UP]

print(f*d)