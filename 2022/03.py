from advent import Advent

advent = Advent(2022, 3)

def _priority_from_char(c):
    offset = 1 if common_l.islower() else 59
    return ord(common_l) - ord('a') + offset

priorities = 0
for rucksack in advent.lines:
    mid = len(rucksack) // 2
    common_l = list(set(rucksack[:mid]).intersection(set(rucksack[mid:])))[0]
    priorities += _priority_from_char(common_l)

print(priorities)


# part 2
priorities = 0
for i in range(0, len(advent.lines), 3):
    pack = advent.lines[i : i + 3]
    s = set(pack[0])
    for rucksack in pack[1:]:
        s = s.intersection(set(rucksack))
    common_l = list(s)[0]
    priorities += _priority_from_char(common_l)
print(priorities)
