from advent import Advent

advent = Advent(2022, 14)

_SEED = (0, 500)

def straight_line(s, e):
    slice = 1 if s[1] < e[1] or s[0] < e[0] else -1
    return [(j, i) for i in range(s[0], e[0] + slice, slice) for j in range(s[1], e[1] + slice, slice)]

def get_bounds(points):
    min_j, max_j, max_i = float('inf'), float('-inf'), float('-inf')
    for i, j in points:
        min_j = min(min_j, j)
        max_j = max(max_j, j)
        max_i = max(max_i, i)

    return min_j, max_j, max_i

def initial_blocked_state():
    blocked = set()
    for path in advent.lines:
        points = [tuple(int(i) for i in p.split(',')) for p in path.split(' -> ')]
        for start, end in zip(points[::], points[1::]):
            blocked.update(straight_line(start, end))
    return blocked

def num_sand_at_rest(blocked, can_continue, can_do_move):
    curr_i, curr_j = _SEED
    sand_at_rest = 0

    while can_continue(curr_i, curr_j):
        can_move = False
        for di, dj in [(1, 0), (1, -1), (1, 1)]:
            if can_do_move(curr_i + di, curr_j + dj):
                curr_i += di
                curr_j += dj
                can_move = True
                break
        if not can_move:
            sand_at_rest += 1
            blocked.add((curr_i, curr_j))
            curr_i, curr_j = _SEED

    return sand_at_rest

# Part 1
blocked = initial_blocked_state()
min_j, max_j, max_i = get_bounds(blocked)
print(num_sand_at_rest(blocked, can_continue=lambda i, j: min_j <= j <= max_j and i <= max_i, can_do_move=lambda i, j: (i, j) not in blocked))

# Part 2
blocked = initial_blocked_state()
max_i += 2
print(num_sand_at_rest(blocked, can_continue=lambda i, j: _SEED not in blocked, can_do_move=lambda i, j: (i, j) not in blocked and i < max_i))