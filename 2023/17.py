from advent import Advent
import heapq

advent = Advent(2023, 17, cast=False)

M, N = len(advent.lines), len(advent.lines[0])

class Direction:
    LEFT = (0, -1)
    RIGHT = (0, 1)
    UP = (-1, 0)
    DOWN = (1, 0)

BLOCKED_DIRS = set([
    (Direction.UP, Direction.DOWN),
    (Direction.DOWN, Direction.UP),
    (Direction.LEFT, Direction.RIGHT),
    (Direction.RIGHT, Direction.LEFT),
])

def min_heat(min_count=1, max_count=3):
    q = [
        (0, (0, 0, Direction.RIGHT, 0)), # (heat, (x, y, direction, count)))
        (0, (0, 0, Direction.DOWN, 0)),
    ]
    heapq.heapify(q)

    loss_seen = set()
    while q:
        heat, (x, y, d, count) = heapq.heappop(q)

        if (x, y, d, count) in loss_seen :
            continue
        loss_seen.add((x, y, d, count))

        if (x, y) == (M - 1, N - 1) and count >= min_count:
            return heat

        for next_pos_dir in [Direction.LEFT, Direction.RIGHT, Direction.UP, Direction.DOWN]:
            if d == next_pos_dir and count >= max_count: continue
            if d != next_pos_dir and count < min_count: continue
            if (d, next_pos_dir) in BLOCKED_DIRS: continue

            next_x = x + next_pos_dir[0]
            next_y = y + next_pos_dir[1]
            if next_x < 0 or next_y < 0 or next_x >= M or next_y >= N:
                continue
            next_count = (count + 1) if next_pos_dir == d else 1
            next_heat = heat + int(advent.lines[next_x][next_y])

            heapq.heappush(q, (next_heat, (next_x, next_y, next_pos_dir, next_count)))

    return -1

print(min_heat(min_count=1, max_count=3))
print(min_heat(min_count=4, max_count=10))
