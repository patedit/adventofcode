from advent import Advent

advent = Advent(2021, 5)

class Line:
    x1, y1, x2, y2 = 0, 0, 0, 0

    def __init__(self, orig, dest) -> None:
        self.x1 = int(orig.split(',')[0])
        self.y1 = int(orig.split(',')[1])
        self.x2 = int(dest.split(',')[0])
        self.y2 = int(dest.split(',')[1])

    def is_diagonal(self):
        return self.x1 != self.x2 and self.y1 != self.y2

    def __str__(self) -> str:
        return '{}, {} -> {}, {}'.format(self.x1, self.y1, self.x2, self.y2)

lines = []
diagram = [[0 for i in range(1000)] for j in range(1000)]
for line in advent.lines:
    orig, dest = line.split(' -> ')
    lines.append(Line(orig, dest))


# Part 1
for line in lines:
    if line.x1 == line.x2:
        for y in range(min(line.y1, line.y2), max(line.y1, line.y2) + 1):
            diagram[y][line.x1] += 1
    elif line.y1 == line.y2:
        for x in range(min(line.x1, line.x2), max(line.x1, line.x2) + 1):
            diagram[line.y1][x] += 1

overlaps = sum(1 for row in diagram for column in row if column >= 2)
print(overlaps)

# Part 2
for line in lines:
    if not line.is_diagonal():
        continue
    step_x = 1 if line.x1 < line.x2 else -1
    step_y = 1 if line.y1 < line.y2 else -1
    for x, y in zip(range(line.x1, line.x2 + step_x, step_x), range(line.y1, line.y2 + step_y, step_y)):
        diagram[y][x] += 1

overlaps = sum(1 for row in diagram for column in row if column >= 2)
print(overlaps)
