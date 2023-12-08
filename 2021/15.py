from advent import Advent
import heapq

advent = Advent(2021, 15)

grid = [[int(i) for i in str(l)] for l in advent.lines]
risk_grid = [[-1 for i in str(l)] for l in advent.lines]

def discover_path(i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]): return float('inf')
    if i == len(grid) - 1 and j == len(grid[0]) - 1: return grid[i][j]

    if risk_grid[i][j] != -1:
        min_distance = risk_grid[i][j]
    else:
        min_distance = min(discover_path(i+1, j), discover_path(i, j+1))
        risk_grid[i][j] = min_distance

    return grid[i][j] + min_distance

print(discover_path(0, 0) - grid[0][0])

# Part 2
pq = [(0,0,0)]
M = len(grid)
N = len(grid[0])

end_point = (M * 5 - 1, N * 5 - 1)
heapq.heapify(pq)
visited = set()

def get(r, c):
    x = (grid[r % N][c % M] +
         (r // N) + (c // M))
    return (x - 1) % 9 + 1

while len(pq) > 0:
    cost, row, col = heapq.heappop(pq)

    if (row, col) in visited:
        continue
    visited.add((row, col))

    if (row, col) == end_point:
        break

    for n_row, n_col in [(row, col + 1), (row, col - 1), (row + 1, col), (row - 1, col)]:
        if not (0 <= n_row <= end_point[0] and 0 <= n_col <= end_point[1]):
            continue
        n_cost = cost + get(n_row, n_col)
        heapq.heappush(pq, (n_cost, n_row, n_col))

print(cost)
