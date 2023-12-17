from advent import Advent

advent = Advent(2023, 10, use_file=False)

def find_start_coord():
    for x in range(len(advent.lines)):
        for y in range(len(advent.lines[x])):
            if advent.lines[x][y] == 'S':
                return (x, y)

NORTH = (-1, 0)
SOUTH = (1, 0)
WEST = (0, -1)
EAST = (0, 1)
PIPES = {
    '|': lambda di, dj: NORTH if (di, dj) in [NORTH] else SOUTH if (di, dj) in [SOUTH] else None,
    '-': lambda di, dj: WEST if (di, dj) in [WEST] else EAST if (di, dj) in [EAST] else None,
    '7': lambda di, dj: WEST if (di, dj) in [NORTH] else SOUTH if (di, dj) in [EAST] else None,
    'J': lambda di, dj: NORTH if (di, dj) in [EAST] else WEST if (di, dj) in [SOUTH] else None,
    'L': lambda di, dj: EAST if (di, dj) in [SOUTH] else NORTH if (di, dj) in [WEST] else None,
    'F': lambda di, dj: EAST if (di, dj) in [NORTH] else SOUTH if (di, dj) in [WEST] else None,
    '.': lambda di, dj: None,
}

def find_loop_path(x, y, d, steps):
    if x < 0 or y < 0 or x >= len(advent.lines) or y >= len(advent.lines[x]):
        return False

    c = advent.lines[x][y]

    if c == 'S':
        return True
    
    dd = PIPES[c](d[0], d[1])
    if dd and find_loop_path(x + dd[0], y + dd[1], dd, steps):
        steps.append((x, y))
        return True

    return False

import sys
sys.setrecursionlimit(100000) # BFS preferred but too late now. Oh well, it works
S = find_start_coord()
max_steps = 0
for dx, dy in [NORTH, SOUTH, EAST, WEST]:
    steps = [S]
    is_loop = find_loop_path(S[0] + dx, S[1] + dy, (dx, dy), steps)
    if is_loop:
        max_steps = len(steps) // 2
        break
print(max_steps)


# Part 2
def valid_crossings(x, y):
    c = 0
    for j in range(y):
        if (x, j) in steps and advent.lines[x][j] in ['J', 'L', '|']:
            c += 1
    return c

def replace_start_pipe():
    # TODO Improve
    last_p, second_p = steps[-1], steps[1]
    diff = [last_p[0] - second_p[0], last_p[1] - second_p[1]]
    if diff == [-1, -1]:
        advent.lines[S[0]] = advent.lines[S[0]].replace('S', 'L')
    elif diff == [1, -1]:
        advent.lines[S[0]] = advent.lines[S[0]].replace('S', 'J')
    elif diff == [1, 1]:
        advent.lines[S[0]] = advent.lines[S[0]].replace('S', '7')
    elif diff == [-1, 1]:
        advent.lines[S[0]] = advent.lines[S[0]].replace('S', 'F')
    elif diff == [0, -1] or diff == [0, 1]:
        advent.lines[S[0]] = advent.lines[S[0]].replace('S', '-')
    elif diff == [-1, 0] or diff == [1, 0]:
        advent.lines[S[0]] = advent.lines[S[0]].replace('S', '|')


replace_start_pipe()
steps = set(steps)
enclosed = 0
for x in range(len(advent.lines)):
    for y in range(len(advent.lines[x])):
        if (x, y) in steps: continue
        if valid_crossings(x, y) % 2 == 1:
            enclosed += 1
        
print(enclosed)
