from advent import Advent

advent = Advent(2023, 9, use_file=False)

# Part 1
next_sum = 0
for line in advent.lines:
    numbers = [[int(i) for i in line.split(' ')]]
    while not all(d == 0 for d in numbers[-1]):
        numbers.append([numbers[-1][i+1] - numbers[-1][i] for i in range(0, len(numbers[-1]) - 1)])
    next_sum += sum([n[-1] for n in numbers])
print(next_sum)

# Part 2
next_sum = 0
for line in advent.lines:
    numbers = [[int(i) for i in line.split(' ')][::-1]]
    while not all(d == 0 for d in numbers[-1]):
        numbers.append([numbers[-1][i+1] - numbers[-1][i] for i in range(0, len(numbers[-1]) - 1)])
    next_sum += sum([n[-1] for n in numbers])
print(next_sum)