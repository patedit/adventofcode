from advent import Advent
import re

advent = Advent(2022, 5)
stacks_raw = advent.paragraphs[0]
num_stacks = int(stacks_raw[-1][-2])

stacks = [[] for _ in range(num_stacks)]
for stack in stacks_raw[:-1]:
    for i in range(num_stacks):
        letter = stack[i * 4 + 1].strip()
        if letter:
            stacks[i] += [stack[i * 4 + 1].strip()]

instructions = advent.paragraphs[1]

def solve_stack(stacks, reversed=True):
    slice = -1 if reversed else 1
    for instruction in instructions:
        quantity, origin, dest = [int(i) for i in re.findall(r'\d+', instruction)]
        stacks[dest-1] = stacks[origin - 1][ : quantity][::slice] + stacks[dest - 1]
        stacks[origin - 1] = stacks[origin - 1][quantity : ]
    return ''.join([l[0] for l in stacks])

# part 1
part1_stacks = list(stacks)
print(solve_stack(part1_stacks))

# part 2
part2_stacks = list(stacks)
print(solve_stack(part2_stacks, False))
