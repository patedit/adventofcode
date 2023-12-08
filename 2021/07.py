from advent import Advent

advent = Advent(2021, 7)

crabs = [int(l) for l in advent.lines[0].split(',')]

# Part 1
fuel = float('inf')
for i in range(len(crabs)):
    crab = crabs[i]
    current_fuel = sum(abs(crabs[j] - crab) for j in range(len(crabs)))
    fuel = min(fuel, current_fuel)

print(fuel)


# Part 2 - TODO: Improve
fuel = float('inf')
for i in range(max(crabs)):
    crab = i
    current_fuel = 0
    for j in range(len(crabs)):
        s = abs(crabs[j] - crab)
        for k in range(s):
            current_fuel += k + 1
    fuel = min(fuel, current_fuel)

print(fuel)