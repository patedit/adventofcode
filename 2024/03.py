import re
from advent import Advent

advent = Advent(2024, 3)

INST_PATTERN = r'mul\((\d{1,3}),(\d{1,3})\)'

def run_sequence(seq):
    matches = re.findall(INST_PATTERN, seq)
    return sum([int(match[0]) * int(match[1]) for match in matches])

# part 1
result = run_sequence(''.join(advent.lines))
print(result)

# part 2
ENABLE_INSTRUCTION = "do()"
DISABLE_INSTRUCTION = "don't()"
program = ENABLE_INSTRUCTION + ''.join(advent.lines) + DISABLE_INSTRUCTION

i, result = 0, 0
while i < len(program):
    enable_index = program.find(ENABLE_INSTRUCTION, i)
    i = enable_index + len(ENABLE_INSTRUCTION)
    disable_inst_index = program.find(DISABLE_INSTRUCTION, i)
    result += run_sequence(program[i : disable_inst_index + 1])
    i = disable_inst_index + len(ENABLE_INSTRUCTION)    
print(result)
