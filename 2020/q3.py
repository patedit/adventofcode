from advent import Advent

TREE = '#'

advent = Advent(3)

forest_map = advent.lines

# Part 1
x, y, trees = 0, 0, 0
while y < len(forest_map) - 1:
    x = (x + 3) % len(forest_map[0])
    y += 1
    trees += forest_map[y][x] == TREE

print(trees)


# Part 2
slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
result = 1
for slope in slopes:
    x, y, trees = 0, 0, 0
    while y < len(forest_map) - 1:
        x = (x + slope[0]) % len(forest_map[0])
        y += slope[1]
        trees += forest_map[y][x] == TREE
    result *= trees

print(result)
