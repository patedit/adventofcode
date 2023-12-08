from advent import Advent

advent = Advent(2021, 9)

heightmap = [[int(c) for c in str(k)] for k in advent.lines]
sum_risk = 0
for r in range(len(heightmap)):
    for c in range(len(heightmap[r])):
        v = heightmap[r][c]
        if r > 0 and heightmap[r-1][c] <= v: continue
        if r < (len(heightmap) - 1) and heightmap[r+1][c] <= v: continue
        if c > 0 and heightmap[r][c-1] <= v: continue
        if c < (len(heightmap[r]) - 1) and heightmap[r][c+1] <=v: continue
        sum_risk += int(v) + 1

print('Part 1: {}'.format(sum_risk))


# Part 2
def compute_basil(i, j):
    if i < 0 or i >= len(heightmap) or j < 0 or j >= len(heightmap[i]) or heightmap[i][j] == 9 or heightmap[i][j] == -1:
        return 0

    basil = 1
    heightmap[i][j] = -1

    basil += compute_basil(i + 1, j)
    basil += compute_basil(i - 1, j)
    basil += compute_basil(i, j - 1)
    basil += compute_basil(i, j + 1)

    return basil

basils = []
for r in range(len(heightmap)):
    for c in range(len(heightmap[r])):
        v = int(heightmap[r][c])
        if v == -1: continue
        if r > 0 and heightmap[r-1][c] <= v: continue
        if r < (len(heightmap) - 1) and heightmap[r+1][c] <= v: continue
        if c > 0 and heightmap[r][c-1] <= v: continue
        if c < (len(heightmap[r]) - 1) and heightmap[r][c+1] <=v: continue
        basils.append(compute_basil(r, c))

basils.sort(reverse=True)
print(basils[0] * basils[1] * basils[2])