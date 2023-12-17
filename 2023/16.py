from advent import Advent
from collections import deque

advent = Advent(2023, 16, use_file=False)

M, N = len(advent.lines), len(advent.lines[0])

class Direction:
    UP = (-1, 0)
    RIGHT = (0, 1)
    DOWN = (1, 0)
    LEFT = (0, -1)

CHANGE_DIRS = {
    '-': {
        Direction.UP: [Direction.LEFT, Direction.RIGHT],
        Direction.DOWN: [Direction.LEFT, Direction.RIGHT]
    },
    '|': {
        Direction.LEFT: [Direction.UP, Direction.DOWN],
        Direction.RIGHT: [Direction.UP, Direction.DOWN]
    },
    '/': {
        Direction.UP: [Direction.RIGHT],
        Direction.RIGHT: [Direction.UP],
        Direction.DOWN: [Direction.LEFT],
        Direction.LEFT: [Direction.DOWN]
    },
    '\\': {
        Direction.UP: [Direction.LEFT],
        Direction.RIGHT: [Direction.DOWN],
        Direction.DOWN: [Direction.RIGHT],
        Direction.LEFT: [Direction.UP]
    },
    '.': {},
}

def next_tiles(curr_tile):

    def add_tile(n_tile, array):
        if n_tile[0] < 0 or n_tile[0] >= M or n_tile[1] < 0 or n_tile[1] >= N: return
        array.append(n_tile)

    next_tiles = []
    x, y, current_dir = curr_tile

    next_directions = CHANGE_DIRS[advent.lines[x][y]]
    if current_dir in next_directions:
        [add_tile((x + next_d[0], y + next_d[1], next_d), next_tiles) for next_d in next_directions[current_dir]]
    else:
        add_tile((x + current_dir[0], y + current_dir[1], current_dir), next_tiles)

    return next_tiles

def energized_tiles(from_tile):
    visited_tiles_dir = set()
    q = deque([from_tile])
    while q:
        tile = q.popleft()
        visited_tiles_dir.add(tile)

        for next_tile in next_tiles(tile):
            if next_tile in visited_tiles_dir: break
            q.append(next_tile)

    return set([(x, y) for x, y, _ in visited_tiles_dir])

# Part 1
from_tile = (0, 0, Direction.RIGHT)
print(len(energized_tiles(from_tile)))

# Part 2
max_seen = 0
for j in range(N):
    from_tile = (0, j, Direction.DOWN)
    max_seen = max(max_seen, len(energized_tiles(from_tile)))
    from_tile = (M - 1, j, Direction.UP)
    max_seen = max(max_seen, len(energized_tiles(from_tile)))
for i in range(M):
    from_tile = (i, 0, Direction.RIGHT)
    max_seen = max(max_seen, len(energized_tiles(from_tile)))
    from_tile = (i, N - 1, Direction.LEFT)
    max_seen = max(max_seen, len(energized_tiles(from_tile)))
print(max_seen)
