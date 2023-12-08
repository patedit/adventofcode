from advent import Advent

advent = Advent(2022, 18, use_file=False)

min_coord = 1 << 60
max_coord = -(1 << 60)

cubes = set()
for l in advent.lines:
    x, y, z = map(int, l.split(","))
    cubes.add(tuple(map(int, l.split(','))))
    for num in [x, y, z]:
        min_coord = min(min_coord, num)
        max_coord = max(max_coord, num)

def overlaps():
    overlaps = 0
    for x, y, z in cubes:
        for coord in range(3):
            cube = [x, y, z]
            cube[coord] += 1
            if tuple(cube) in cubes: overlaps += 1
            cube[coord] -= 2
            if tuple(cube) in cubes: overlaps += 1

    return overlaps

print(len(cubes) * 6 - 2 * (overlaps() // 2))

# Part 2

def can_surface_exterior(cube):
    if cube in cubes: return False
    
    stack = [cube]
    seen = set()
    while len(stack) > 0:
        next_cube = stack.pop()
        if next_cube in cubes: continue
        for coord in range(3):
            if not (min_coord <= next_cube[coord] <= max_coord): return True
        if next_cube in seen: continue
        seen.add(next_cube)
        for coord in range(3):
            a_cube = list(next_cube)
            a_cube[coord] += 1
            stack.append(tuple(a_cube))
            a_cube[coord] -= 2
            stack.append(tuple(a_cube))
    return False

s = 0
for x, y, z in cubes:
    for coord in range(3):
        cube = [x, y, z]
        cube[coord] += 1
        s += can_surface_exterior(tuple(cube))
        cube[coord] -= 2
        s += can_surface_exterior(tuple(cube))

print(s)
