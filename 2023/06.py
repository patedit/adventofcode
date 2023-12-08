from advent import Advent
import math

advent = Advent(2023, 6, use_file=False)

# Part 1
times = [int(t) for t in advent.lines[0].split(':')[1].strip().split(' ') if t]
distances = [int(t) for t in advent.lines[1].split(':')[1].strip().split(' ') if t]
records = []

for i, time in enumerate(times):
  record = 0
  for hold in range(1, time + 1):
    traveled = hold * (time - hold)
    if traveled > distances[i]:
      record += 1
  records.append(record)

print(math.prod(records))

# Part 2
time = int(''.join([str(t) for t in advent.lines[0].split(':')[1].strip().split(' ') if t]))
distance = int(''.join([str(t) for t in advent.lines[1].split(':')[1].strip().split(' ') if t]))
record = 0
for hold in range(1, time + 1):
  traveled = hold * (time - hold)
  if traveled > distance:
    record += 1
print(record)