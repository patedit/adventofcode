from advent import Advent

advent = Advent(2022, 4)

# part 1
overlaps = 0
for group in advent.lines:
    sections = [[int(i) for i in g.split('-')] for g in group.split(',')]

    if (sections[0][0] <= sections[1][0] and sections[0][1] >= sections[1][1]) or \
        (sections[0][0] >= sections[1][0] and sections[0][1] <= sections[1][1]):
            overlaps += 1

print(overlaps)

# part 2
overlaps = 0
for group in advent.lines:
    sections = [[int(i) for i in g.split('-')] for g in group.split(',')]
    if (sections[0][0] >= sections[1][0] and sections[0][0] <= sections[1][1]) or \
        (sections[0][1] >= sections[1][0] and sections[0][1] <= sections[1][1]) or \
        (sections[1][0] >= sections[0][0] and sections[1][0] <= sections[0][1]) or \
        (sections[1][1] >= sections[0][0] and sections[1][1] <= sections[0][1]):
            overlaps += 1 
print(overlaps)
