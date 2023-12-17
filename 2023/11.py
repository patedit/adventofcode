from advent import Advent
from itertools import combinations

advent = Advent(2023, 11, use_file=False)

expand_i = [i for i in range(len(advent.lines)) if '#' not in advent.lines[i]]
expand_j = [j for j in range(len(advent.lines[0])) if '#' not in [line[j] for line in advent.lines]]
galaxies = [(i, j) for i in range(len(advent.lines)) for j in range(len(advent.lines[0])) if advent.lines[i][j] == '#']

def shortest_distance(galaxies):
    distance = 0
    for galaxy, other_galaxy in combinations(galaxies, 2):
        distance += abs(galaxy[0] - other_galaxy[0]) + abs(galaxy[1] - other_galaxy[1])
    return distance

def expand_galaxies(factor):
    expanded_galaxies = []
    for i, j in galaxies:
        extra_i = sum([1 for x in expand_i if x < i]) * factor
        extra_j = sum([1 for y in expand_j if y < j]) * factor
        expanded_galaxies.append((i + extra_i, j + extra_j))
    return expanded_galaxies

# Part 1
expanded_galaxies = expand_galaxies(1)
print(shortest_distance(expanded_galaxies))

# Part 2
expanded_galaxies = expand_galaxies(1000000 - 1)
print(shortest_distance(expanded_galaxies))

