from advent import Advent
from collections import deque

advent = Advent(2022, 12, use_file=False)

grid = [[ord(c) - ord('a') for c in grid_line] for grid_line in advent.lines]

def find_char(c, replace_c=None):
    found_ps = [(i, j) for i in range(len(grid)) for j in range(len(grid[i])) if grid[i][j] == c]
    if replace_c is not None:
        for i, j in found_ps:
            grid[i][j] = replace_c
    return found_ps

def bfs(origin_ps, dest_p):
    seen, q = set([origin_p for origin_p in origin_ps]), deque([(origin_p, 0) for origin_p in origin_ps])
    while q:
        current_p, steps = q.popleft()
        if current_p == dest_p: return steps
        for dx, dy in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
            next_p = nx, ny = current_p[0] + dx, current_p[1] + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[nx]) and next_p not in seen and grid[nx][ny] - grid[current_p[0]][current_p[1]] <= 1:
                seen.add(next_p)
                q.append((next_p, steps + 1))

    return float('inf')

# Part 1
start_ps = find_char(ord('S') - ord('a'), 0)
end_p = find_char(ord('E') - ord('a'), 26)[0]
print(bfs(start_ps, end_p))

# Part 2
start_ps = find_char(0)
print(bfs(start_ps, end_p))