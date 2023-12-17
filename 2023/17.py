from advent import Advent
import heapq

advent = Advent(2023, 17, use_file=False)

M, N = len(advent.lines), len(advent.lines[0])

class Direction:
    LEFT = (0, -1)
    RIGHT = (0, 1)
    UP = (-1, 0)
    DOWN = (1, 0)

def min_heat(min_count=1, max_count=3):
    q = [
        (0, (0, 0, Direction.RIGHT, 0)), # (heap, (x, y, diretion, count)))
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

        next_dirs = []
        for pos_d in [Direction.LEFT, Direction.RIGHT, Direction.UP, Direction.DOWN]:
            if d == pos_d:
                if count < max_count:
                    next_dirs.append(pos_d)
            elif pos_d == Direction.UP and d == Direction.DOWN:
                continue
            elif pos_d == Direction.DOWN and d == Direction.UP:
                continue
            elif pos_d == Direction.LEFT and d == Direction.RIGHT:
                continue
            elif pos_d == Direction.RIGHT and d == Direction.LEFT:
                continue
            else:
                next_dirs.append(pos_d)

        for next_direction in next_dirs:
            if next_direction == d:
                next_count = count + 1
            elif count >= min_count:
                next_count = 1
            else: continue
            next_x = x + next_direction[0]
            next_y = y + next_direction[1]
            if next_x < 0 or next_y < 0 or next_x >= M or next_y >= N:
                continue
            next_heat = heat + int(advent.lines[next_x][next_y])
            heapq.heappush(q, (next_heat, (next_x, next_y, next_direction, next_count)))

    return -1
import time
start_time = time.time()
print(min_heat(min_count=1, max_count=3))
print(min_heat(min_count=4, max_count=10))
end_time = time.time()
print(end_time - start_time)