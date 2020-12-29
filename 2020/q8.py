from advent import Advent

advent = Advent(8)

def acc_before_end(instructions):
    instruction_idx, acc = 0, 0
    visited = set()
    while instruction_idx not in visited and instruction_idx < len(instructions) - 1:
        visited.add(instruction_idx)
        instruction = instructions[instruction_idx][:3]
        offset = int(instructions[instruction_idx][4:])
        if instruction == 'jmp':
            instruction_idx += offset - 1
        elif instruction == 'acc':
            acc += offset
        instruction_idx += 1

    return acc, instruction_idx

# Part 1
print(acc_before_end(advent.lines)[0])

# Part 2
swaps = {'jmp': 'nop', 'nop': 'jmp'}
for idx, line in enumerate(advent.lines):
    last_idx = -1
    instruction = line[:3]
    offset = int(line[4:])
    if instruction in swaps:
        new_instructions = advent.lines.copy()
        new_instructions[idx] = "{} {}".format(swaps[instruction], offset)
        acc, last_idx = acc_before_end(new_instructions)

    if last_idx == len(advent.lines) - 1:
        break

print(acc)
