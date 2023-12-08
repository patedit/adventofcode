from advent import Advent

advent = Advent(2021, 11)

energy_levels = [[int(i) for i in str(r)] for r in advent.lines]
flashes = 0
def increase_energy(i, j):
    global flashes
    if i < 0 or i >= len(energy_levels) or j < 0 or j >= len(energy_levels[i]) or energy_levels[i][j] == -1: return

    energy_levels[i][j] += 1
    if energy_levels[i][j] == 10:
        flashes += 1
        energy_levels[i][j] = -1
        for dx, dy in [(0, -1), (0, 1), (1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1)]:
            increase_energy(i + dx, j + dy)

STEPS = 100
for step in range(STEPS):
    for r in range(len(energy_levels)):
        for c in range(len(energy_levels[r])):
            increase_energy(r, c)

    for r in range(len(energy_levels)):
        for c in range(len(energy_levels[r])):
            if energy_levels[r][c] == -1:
                energy_levels[r][c] = 0
print(flashes)

# Part 2
STEPS = 1960
energy_levels = [[int(i) for i in str(r)] for r in advent.lines]
flashes = 0
for step in range(STEPS):
    for r in range(len(energy_levels)):
        for c in range(len(energy_levels[r])):
            increase_energy(r, c)

    zero_c = 0
    for r in range(len(energy_levels)):
        for c in range(len(energy_levels[r])):
            if energy_levels[r][c] == -1:
                energy_levels[r][c] = 0
                zero_c += 1
    
    if zero_c == len(energy_levels) * len(energy_levels[0]):
        print(step + 1)
        break
