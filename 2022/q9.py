from advent import Advent

advent = Advent(2022, 9, use_file=False)

def _follow(tail, head):
    if abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1: return

    for i in [0,1]:
        if head[i] - tail[i] > 0:
            tail[i] += 1
        elif head[i] - tail[i] < 0:
            tail[i] -= 1

def visited_points(n_tails: int):
    tail_visited_p = set()
    head = [0, 0]
    tails = [[0,0] for _ in range(n_tails)]

    for move in advent.lines:
        dir, steps = move.split(' ')
        if dir == 'R': r_c, sig = 1, 1
        if dir == 'L': r_c, sig = 1, -1
        if dir == 'U': r_c, sig = 0, -1
        if dir == 'D': r_c, sig = 0, 1

        for _ in range(int(steps)):
            head[r_c] += 1 * sig
            for i, tail in enumerate(tails):
                _follow(tail, head if i == 0 else tails[i - 1])
            tail_visited_p.add(tuple(tails[-1]))

    return tail_visited_p

# Part 1
print(len(visited_points(1)))

# Part 2
print(len(visited_points(9)))
