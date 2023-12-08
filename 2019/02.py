from advent import Advent
advent = Advent(2019, 2)

program = [int(i) for i in advent.lines[0].split(',')]

SOMETHING = {
    1: lambda x, i: x[x[i + 1]] + x[x[i + 2]],
    2: lambda x, i: x[x[i + 1]] * x[x[i + 2]]
}

def run_program(program, pos1, pos2):
    program[1] = pos1
    program[2] = pos2

    idx = 0
    while program[idx] != 99:
        program[program[idx + 3]] = SOMETHING[program[idx]](program, idx)
        idx += 4
    return program[0]

print(run_program(list(program), 12, 2))

# Part 2
for i in range(0, 99):
    for j in range(0, 99):
        output = run_program(list(program), i, j)
        if output == 19690720:
            print(100 * i + j)
            break