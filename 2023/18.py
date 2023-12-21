from advent import Advent

advent = Advent(2023, 18, use_file=True)

DIRECTION = {
    "L": (-1, 0),
    "R": (1, 0),
    "U": (0, 1),
    "D": (0, -1)
}

def area_with_perimeter(points):
    area, perimeter = 0, 0
    for ((x0, y0), (x1, y1)) in zip(points, points[1:]):
        area += x0 * y1 - x1 * y0
        perimeter += abs(x1 - x0) + abs(y1 - y0)
    return abs(area) // 2 + (perimeter // 2 + 1)

def points_part1():
    x, y = 0, 0
    points = [(x, y)]
    for dig in advent.lines:
        dir_letter, l, _ = dig.split(" ")
        dx, dy = DIRECTION[dir_letter]
        x += dx * int(l)
        y += dy * int(l)
        points.append((x, y))
    return points

def points_part2():
    DIR_MAPPING = {
        "0": "R",
        "1": "D",
        "2": "L",
        "3": "U"
    }
    x, y = 0, 0
    points = [(x, y)]
    for dig in advent.lines:
        _, __, color = dig.split(" ")
        l = int(color[2:-2], 16)
        dx, dy = DIRECTION[DIR_MAPPING[color[-2]]]
        x += dx * int(l)
        y += dy * int(l)
        points.append((x, y))
    return points

print(area_with_perimeter(points_part1()))
print(area_with_perimeter(points_part2()))