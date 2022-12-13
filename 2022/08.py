from advent import Advent

advent = Advent(2022, 8, use_file=False)

grid = [[int(i) for i in str(l)] for l in advent.lines]

# Matrix with top, left, bottom, right maxs
maxs = [[[h for h in l] for l in grid] for _ in range(4)]

# Part 1
def find_interior_maxs():
    
    def traverse_tree(start, end):
        step = 1 if end > start else -1
        maxs_idxs = [[0, (-1, 0)], [1, (0, -1)]] if step == 1 else [[2, (1, 0)], [3, (0, 1)]]
        for i in range(start, end, step):
            for j in range(start, end, step):
                for maxs_i, (dx, dy) in maxs_idxs:
                    prev_max_height = maxs[maxs_i][i + dx][j + dy]
                    maxs[maxs_i][i][j] = max(grid[i + dx][j + dy], prev_max_height) 

    traverse_tree(1, len(grid) - 1)
    traverse_tree(len(grid) - 2, 0)

    visible_interior = sum([1 for i in range(len(grid)) for j in range(len(grid[i])) if any([m[i][j] < grid[i][j] for m in maxs])])
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