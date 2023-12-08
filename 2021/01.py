from advent import Advent

advent = Advent(2021, 1)

# Part 1
result = sum([1 for idx in range(1, len(advent.lines)) if advent.lines[idx] > advent.lines[idx - 1]])
print(result)


# Part 2
result = 0
prev_sum = sum(advent.lines[0:3])
for idx in range(1, len(advent.lines)):
    curr_sum = sum(advent.lines[idx:idx+3])
    result += 1 if curr_sum > prev_sum else 0
    prev_sum = curr_sum
print(result)