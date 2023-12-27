from advent import Advent
from collections import defaultdict

advent = Advent(2023, 23, use_file=False)

M, N = len(advent.lines), len(advent.lines[0])

start = (0, advent.lines[0].index('.'))
end = (M - 1, advent.lines[-1].index('.'))

def neighbors(coord):
    i, j = coord
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_coord = (i + dx, j + dy)
        if (new_coord[0] < 0 or
            new_coord[0] >= M or
            new_coord[1] < 0 or
            new_coord[1] >= N or
            advent.lines[new_coord[0]][new_coord[1]] == '#'
        ): continue
        yield new_coord

# Part 1
q = [(0, start, set([start]), (1, 0))]

max_path = 0
while q:
    steps, coord, visited, d = q.pop()

    if coord == end:
        max_path = max(max_path, steps)
        continue

    new_steps = steps + 1
    for new_coord in neighbors(coord):
        if new_coord in visited: continue

        dx, dy = new_coord[0] - coord[0], new_coord[1] - coord[1]
        if advent.lines[new_coord[0]][new_coord[1]] == '>' and (dx, dy) != (0, 1): continue
        if advent.lines[new_coord[0]][new_coord[1]] == '<' and (dx, dy) != (0, -1): continue
        if advent.lines[new_coord[0]][new_coord[1]] == '^' and (dx, dy) != (-1, 0): continue
        if advent.lines[new_coord[0]][new_coord[1]] == 'v' and (dx, dy) != (1, 0): continue
    
        new_visited = set(visited)
        new_visited.add(new_coord)
        q.append((new_steps, new_coord, new_visited, d))

print(max_path)

# Part 2
v = set([start, end])
for i in range(M):
    for j in range(N):
        if len(list(neighbors((i, j)))) > 2:
            v.add((i, j))

distances = defaultdict(list)

for x, y in v:
    q  = []
    q.append((x, y))

    seen = set([(x, y)])
    dist = 0
    while q:
        new_q = []
        dist += 1
        for coord in q:
            for neighbor in neighbors(coord):
                if neighbor in seen: continue
                seen.add(neighbor)
                if neighbor in v:
                    distances[(x, y)].append((neighbor, dist))
                else:
                    new_q.append(neighbor)
        q = list(new_q)


q = [(0, start, set([start]))]
max_path = 0
while q:
    steps, coord, visited = q.pop()

    if coord == end:
        max_path = max(max_path, steps)
        continue
    for neighbor, dist in distances[coord]:
        if neighbor in visited: continue
        new_steps = steps + dist
        new_visited = set(visited)
        new_visited.add(neighbor)
        q.append((new_steps, neighbor, new_visited, d))

print(max_path)
