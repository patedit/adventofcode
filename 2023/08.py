from advent import Advent
import math

advent = Advent(2023, 8, use_file=False)

# Part 1
sequence = [str(l) for l in advent.paragraphs[0][0]]
MAP = {}
for line in advent.paragraphs[1]:
  k, v = line.split(' = ')
  MAP[k] = {
    'L': v[1:4],
    'R': v[6:9],
  }

node = 'AAA'
instruction_idx = 0
steps = 0
while node != 'ZZZ':
  l_or_r = sequence[instruction_idx]
  node = MAP[node][l_or_r]
  instruction_idx = (instruction_idx + 1) % len(sequence)
  steps += 1
print(steps)


# Part 2
z_set = set()
for k in MAP.keys():
  if k[-1] != 'A': continue
  steps, instruction_idx = 0, 0
  seen = set()
  node = k
  while (node, instruction_idx) not in seen:
    seen.add((node, instruction_idx))
    l_or_r = sequence[instruction_idx]
    node = MAP[node][l_or_r]

    steps += 1
    if node[-1] == 'Z':
      z_set.add((node, steps))

    instruction_idx = (instruction_idx + 1) % len(sequence)

lcm = math.lcm(*[z[1] for z in z_set])
print(lcm)
