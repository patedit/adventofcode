from advent import Advent

advent = Advent(1)
GOAL  = 2020

# Part 1
entries = set(advent.lines)
for entry in advent.lines:
    if (GOAL - entry) in entries:
        product = (GOAL - entry) * entry
        break

print(product)


# Part 2
entries = advent.lines
entries.sort()

first_idx, second_idx, third_idx = 0, 1, len(entries) - 1
cash = 0
while first_idx < len(entries) - 3 and cash != GOAL:
    second_idx = first_idx + 1
    third_idx = len(entries) - 1

    while second_idx < third_idx and cash != GOAL:
        cash = entries[first_idx] + entries[second_idx] + entries[third_idx]
        if cash > GOAL:
            third_idx -= 1
        elif cash < GOAL:
            second_idx += 1

    first_idx += 1

product = entries[first_idx - 1] * entries[second_idx] * entries[third_idx]
print(product)
