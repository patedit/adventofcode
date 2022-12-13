from advent import Advent

advent = Advent(2022, 8, use_file=False)

grid = [[int(i) for i in str(l)] for l in advent.lines]

max_top = [[0 for _ in range(len(str(advent.lines[0])))] for _ in range(len(advent.lines))]
max_bottom = [[0 for _ in range(len(str(advent.lines[0])))] for _ in range(len(advent.lines))]
max_left = [[0 for _ in range(len(str(advent.lines[0])))] for _ in range(len(advent.lines))]
max_right = [[0 for _ in range(len(str(advent.lines[0])))] for _ in range(len(advent.lines))]

for i, n in enumerate(advent.lines):
    for j, s in enumerate(str(n)):
        max_top[i][j] = int(s)
        max_bottom[i][j] = int(s)
        max_left[i][j] = int(s)
        max_right[i][j] = int(s)

maxs = [max_top, max_left, max_bottom, max_right]

# Part 1
def find_interior_maxs():
    for i in range(1, len(grid)):
        for j in range(1, len(grid[i])):
            if i == 0 or j == 0 or i == len(grid) - 1 or j == len(grid[i]) - 1: continue
            prev_max_height = maxs[0][i-1][j]
            maxs[0][i][j] = max(grid[i-1][j], prev_max_height) # top
            prev_max_height = maxs[1][i][j-1]
            maxs[1][i][j] = max(grid[i][j-1], prev_max_height) # left

    for i in range(len(grid) - 2, 0, -1):
        for j in range(len(grid[i]) - 2, 0, -1):
            if i == 0 or j == 0 or i == len(grid) - 1 or j == len(grid[i]) - 1: continue
            prev_max_height = maxs[2][i + 1][j]
            maxs[2][i][j] = max(grid[i+1][j], prev_max_height) # bottom
            prev_max_height = maxs[3][i][j + 1]
            maxs[3][i][j] = max(grid[i][j+1], prev_max_height) # right

    visible_interior = sum([1 for j in range(len(grid[i])) for i in range(len(grid)) if any([m[i][j] < grid[i][j] for m in maxs])])
    visible_edges = len(grid) * 4 - 4

    return visible_interior + visible_edges


print(find_interior_maxs())

# Part 2
def max_scenic_score():
    max_scenic_score = 0
    for i in range(1, len(grid)):
        for j in range(1, len(grid[i])):
            total_score_ij = 1
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                score = 0
                x, y = i + dx, j + dy
                while 0 <= x < len(grid) and 0 <= y < len(grid[i]):
                    if grid[x][y] >= grid[i][j]:
                        score += 1
                        break
                    x += dx
                    y += dy
                    score += 1

                total_score_ij *= score
            max_scenic_score = max(max_scenic_score, total_score_ij)

    return max_scenic_score

print(max_scenic_score())