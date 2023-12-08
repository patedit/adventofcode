from advent import Advent

advent = Advent(2019, 6, use_file=False)

orbits = {}
for orbit in advent.lines:
    orbit_left, orbit_right = orbit.split(')')
    if orbit_left in orbits:
        orbits[orbit_left][orbit_right] = {}
    else:
        orbits[orbit_left] = {orbit_right: {}}
    if orbit_right in orbits:
        orbits[orbit_right]['parent'] = orbit_left
    else:
        orbits[orbit_right] = {'parent' : orbit_left}
orbits['COM']['parent'] = None

def dfs(r, i):
    if not r or len(r) == 0 or r not in orbits: return i
    total = i
    i += 1
    for planet in orbits[r].keys():
        if planet == 'parent': continue
        total += dfs(planet, i)
    return total

# part 1
result = dfs('COM', 0)
print(result)

# part 2
seen_parents = dict()
parent = orbits['YOU']['parent']
i = 0
while parent:
    seen_parents[parent] = i
    parent = orbits[parent]['parent']
    i += 1

parent = orbits['SAN']['parent']
i = 0
while parent and parent not in seen_parents:
    parent = orbits[parent]['parent']
    i += 1

if parent:
    print(seen_parents[parent] + i)
