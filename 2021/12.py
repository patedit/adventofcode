from advent import Advent

advent = Advent(2021, 12)

connections = {}
for line in advent.lines:
    orig, dest = line.split('-')
    if orig in connections:
        connections[orig].append(dest)
    else:
        connections[orig] = [dest]

    if orig != 'start' and dest != 'end':
        if dest in connections:
            connections[dest].append(orig)
        else:
            connections[dest] = [orig]

# Part 1
def find_paths(from_point, visited):
    if from_point == 'end': return 1
    if from_point in visited: return 0

    paths = 0
    if from_point.islower():
        visited.append(from_point)
    for next_point in connections[from_point]:
        paths += find_paths(next_point, list(visited))
    return paths

paths = find_paths('start', [])
print(paths)

# Part 2
# Modified the code so I could see the paths since I had an error at first. The error turned out to be that it could go back to start...
def find_paths2(from_point, visited, visited_twice):
    if from_point == 'end': return [visited + ['end']]
    if from_point.islower() and from_point in visited:
        if visited_twice is True: return []
        visited_twice = True

    paths = []
    new_visited = visited + [from_point]
    for next_point in connections[from_point]:
        if next_point not in ['start']:
            path = find_paths2(next_point, new_visited, visited_twice)
            if path and len(path) > 0:
                paths.extend(path)
    return paths

paths = find_paths2('start', [], False)
# for path in paths:
#     print(','.join(path))
print(len(paths))
