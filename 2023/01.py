from advent import Advent

advent = Advent(2023, 1, use_file=False)

# Part 1
s = 0
for line in advent.lines:
  numbers = []
  for c in str(line):
    if c.isdigit():
      numbers.append(c)
  s += int(numbers[0] + numbers[-1])
print(s)


# Part 2
s = 0
for l in advent.lines:
  line = str(l)
  numbers = []
  for i, c in enumerate(line):
    if c.isdigit():
      numbers.append(c)
    for j, n in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
      if line[i:].startswith(n):
        numbers.append(str(j + 1))
  s += int(numbers[0] + numbers[-1])
print(s)