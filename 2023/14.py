from advent import Advent

advent = Advent(2023, 14, use_file=False)

def print_dish(rocks, blocks):
    for i in range(len(advent.lines)):
        for j in range(len(advent.lines[0])):
            if (i, j) in rocks:
                print('O', end='')
            elif (i, j) in blocks:
                print('#', end='')
            else:
                print('.', end='')
        print()

# Part 1
rocks = [0] * len(advent.lines)
for j in range(len(advent.lines[0])):
    next_rock_i = 0
    for i in range(len(advent.lines)):
        c = advent.lines[i][j]
        if c == '#':
            next_rock_i = i + 1
        if c == 'O':
            rocks[next_rock_i] += 1
            next_rock_i += 1
load = sum(n * (len(advent.lines) - i) for i, n in enumerate(rocks))
print(load)

# Part 2
def read_rocks_blocks():
    rocks = set()
    blocks = set()
    for i in range(len(advent.lines)):
        for j in range(len(advent.lines[0])):
            if advent.lines[i][j] == 'O':
                rocks.add((i, j))
            if advent.lines[i][j] == '#':
                blocks.add((i, j))
    return rocks, blocks

def tilt(rocks, d):
    if d == 0:
        # north
        for j in range(len(advent.lines[0])):
            next_rock_i = 0
            for i in range(len(advent.lines)):
                if (i, j) in rocks:
                    rocks.remove((i, j))
                    rocks.add((next_rock_i, j))
                    next_rock_i += 1
                if (i, j) in blocks:
                    next_rock_i = i + 1

        return rocks
    if d == 1:
        # west
        for i in range(len(advent.lines)):
            next_rock_j = 0
            for j in range(len(advent.lines[0])):
                if (i, j) in rocks:
                    rocks.remove((i, j))
                    rocks.add((i, next_rock_j))
                    next_rock_j += 1
                if (i, j) in blocks:
                    next_rock_j = j + 1
        return rocks
    if d == 2:
        # south
        for j in range(len(advent.lines[0]) - 1, -1, -1):
            next_rock_i = len(advent.lines) - 1
            for i in range(len(advent.lines) -1, -1, -1):
                if (i, j) in rocks:
                    rocks.remove((i, j))
                    rocks.add((next_rock_i, j))
                    next_rock_i -= 1
                if (i, j) in blocks:
                    next_rock_i = i - 1

        return rocks
    if d == 3:
        # east
        for i in range(len(advent.lines)):
            next_rock_j = len(advent.lines[0]) - 1
            for j in range(len(advent.lines[0]) - 1, -1, -1):
                if (i, j) in rocks:
                    rocks.remove((i, j))
                    rocks.add((i, next_rock_j))
                    next_rock_j -= 1
                if (i, j) in blocks:
                    next_rock_j = j - 1
        return rocks

seen_rocks = []
rocks, blocks = read_rocks_blocks()
BILLION = 1000000000
load = 0
for cycle in range(0, BILLION):
    for d in range(4):
        rocks = tilt(rocks, d)

    if tuple(rocks) in seen_rocks:
        seen_index = seen_rocks.index(tuple(rocks))
        cycle_loop = seen_rocks[seen_index:]
        remaining_cycles = BILLION - cycle - 1
        index_billionth = remaining_cycles % len(cycle_loop)
        for (i, j) in cycle_loop[index_billionth]:
            load += len(advent.lines) - i
        break

    seen_rocks.append(tuple(rocks))
print(load)
