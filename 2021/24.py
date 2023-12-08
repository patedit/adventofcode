from advent import Advent


advent = Advent(2021, 24, use_file=False)

TOTAL_DIGITS = 14
PROCESSING_UNITS = {
    'w': 0,
    'x': 0,
    'y': 0,
    'z': 0
}
# inps_i = [i for i in range(len(advent.lines)) if advent.lines[i].startswith("inp")]

# instructions = [advent.lines[idx : (inps_i[i + 1]) if i < len(inps_i) - 1 else len(advent.lines)] for i, idx in enumerate(inps_i)]

instructions = advent.lines

def run_input(instructions, n):
    i = 0
    zz = []
    for instruction in instructions:
        if instruction[:3] == "inp":
            PROCESSING_UNITS[instruction[4:]] = n[i]
            i += 1
        elif instruction[:3] == "add":
            a, b = instruction[4:].split(" ")
            if b in PROCESSING_UNITS:
                PROCESSING_UNITS[a] += PROCESSING_UNITS[b]
            else:
                PROCESSING_UNITS[a] += int(b)
        elif instruction[:3] == "mul":
            a, b = instruction[4:].split(" ")

            if b in PROCESSING_UNITS:
                PROCESSING_UNITS[a] *= PROCESSING_UNITS[b]
            else:
                PROCESSING_UNITS[a] *= int(b)
        elif instruction[:3] == "div":
            # print(a, b)

            a, b = instruction[4:].split(" ")
            

            if b in PROCESSING_UNITS:
                PROCESSING_UNITS[a] = int(PROCESSING_UNITS[a] // PROCESSING_UNITS[b])
            else:
                PROCESSING_UNITS[a] = int(PROCESSING_UNITS[a] // int(b))
        elif instruction[:3] == "mod":
            a, b = instruction[4:].split(" ")
            
            if b in PROCESSING_UNITS:
                PROCESSING_UNITS[a] = int(PROCESSING_UNITS[a] % PROCESSING_UNITS[b])
            else:
                PROCESSING_UNITS[a] = int(PROCESSING_UNITS[a] % int(b))
        elif instruction[:3] == "eql":
            a, b = instruction[4:].split(" ")
            # print(a, b)
            if b in PROCESSING_UNITS:
                PROCESSING_UNITS[a] = 1 if PROCESSING_UNITS[a] == PROCESSING_UNITS[b] else 0
            else:
                PROCESSING_UNITS[a] = 1 if PROCESSING_UNITS[a] == int(b) else 0

# highest_model = [-1 for _ in range(TOTAL_DIGITS)]
# for digit_i in range(TOTAL_DIGITS):
#     for n in range(9, 0, -1):
#         run_input(instructions[digit_i], n)
#         if PROCESSING_UNITS['z'] == 0:
#             highest_model[digit_i] = n
#             break

import itertools
a = itertools.combinations_with_replacement([i for i in range(1, 10)], TOTAL_DIGITS)
a = sorted(a, reverse=True)
solution = -1
for n in a:
    PROCESSING_UNITS = {
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0
    }
    # print(n)
    resul = run_input(instructions, n)
    # print(PROCESSING_UNITS['z'])
    if resul == 0:
        solution = n
        break

print(solution)

# for i in range(99999999999999, 0):
#     run_input(instructions[digit_i], n)
#     if PROCESSING_UNITS['z'] == 0:


# print(PROCESSING_UNITS)
# print(' '.join([str(m) for m in highest_model]))


