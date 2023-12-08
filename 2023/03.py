from advent import Advent

advent = Advent(2023, 3, use_file=False)

def _find_coord_checks(i, j, length):
    checks = []
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + length + 1):
            if x >= 0 and x < len(advent.lines) and y >= 0 and y < len(advent.lines[x]) and (x == i or y >= j or y <= j + length - 1):
                checks.append((x,y))
    return checks

def _has_symbol(i, j, d):
    for x, y in _find_coord_checks(i, j, len(d)):
        if not advent.lines[x][y].isnumeric() and advent.lines[x][y] != '.':
            return True


# Part 1
s = 0
for i, line in enumerate(advent.lines):
    j = 0
    while j < len(line):
        c = line[j]
        d = ''
        while c.isdigit():
            d += c
            j += 1
            if j < len(line):
                c = line[j]
            else:
                break
        s += int(d) if d and _has_symbol(i, j - len(d), d) else 0
        j += 1

print(s)


# Part 2
def find_adjacent_numbers(i, j):
    n = []
    added = set()
    for x, y in _find_coord_checks(i, j, 1):
        d = ''
        j = y
        while j < len(advent.lines[x]) and advent.lines[x][j].isdigit() and (x, j) not in added:
            d += advent.lines[x][j]
            added.add((x, j))
            j += 1
        j = y - 1
        if d:
            while j >= 0 and advent.lines[x][j].isdigit() and (x, j) not in added:
                d = advent.lines[x][j] + d
                added.add((x, j))
                j -= 1
        if d != '':
            n.append(int(d))
    return n

s = 0
for i, line in enumerate(advent.lines):
    for j, c in enumerate(line):
        if c == '*':
            adjacent_numbers = find_adjacent_numbers(i, j)
            if len(adjacent_numbers) == 2:
                s += adjacent_numbers[0] * adjacent_numbers[1]
print(s)
