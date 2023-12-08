from advent import Advent

advent = Advent(2021, 19)

scanners_input = [advent.paragraphs[i][1:] for i in range(len(advent.paragraphs) - 0)]

def eu(p1, p2):
    if len(p1) == 3:
        return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)**0.5
    if len(p1) == 2:
        return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5
    return p1[0] - p2[0]

scanner_eu_distances = [{} for i in range(len(scanners_input))]

for scanner_i, scanner in enumerate(scanners_input):
    for line_i in range(len(scanner)):
        for line_j in range(line_i + 1, len(scanner)):
            distance = eu([int(i) for i in scanner[line_i].split(',')], [int(i) for i in scanner[line_j].split(',')])
            scanner_eu_distances[scanner_i][distance] = [scanner[line_i], scanner[line_j]]

pos = [[[1,0,0],[0,1,0],[0,0,1]],
[[0,1,0],[0,0,1],[1,0,0]],
[[0,0,1],[1,0,0],[0,1,0]],
[[-1,0,0],[0,1,0],[0,0,1]],
[[0,-1,0],[0,0,1],[1,0,0]],
[[0,0,-1],[1,0,0],[0,1,0]],
[[-1,0,0],[0,-1,0],[0,0,1]],
[[0,-1,0],[0,0,-1],[1,0,0]],
[[0,0,-1],[-1,0,0],[0,1,0]],
[[-1,0,0],[0,-1,0],[0,0,-1]],
[[0,-1,0],[0,0,-1],[-1,0,0]],
[[0,0,-1],[-1,0,0],[0,-1,0]],
[[-1,0,0],[0,1,0],[0,0,-1]],
[[0,-1,0],[0,0,1],[-1,0,0]],
[[0,0,-1],[1,0,0],[0,-1,0]],
[[1,0,0],[0,-1,0],[0,0,1]],
[[0,1,0],[0,0,-1],[1,0,0]],
[[0,0,1],[-1,0,0],[0,1,0]],
[[1,0,0],[0,-1,0],[0,0,-1]],
[[0,1,0],[0,0,-1],[-1,0,0]],
[[0,0,1],[-1,0,0],[0,-1,0]],
[[1,0,0],[0,1,0],[0,0,-1]],
[[0,1,0],[0,0,1],[-1,0,0]],
[[0,0,1],[1,0,0],[0,-1,0]]]

pos_scanners_relative = {k: {'from': None, 'pos': None} for k in range(1, len(scanners_input))}
visited = {0}
while len(visited) != len(scanners_input):
    for scanner_i in range(1, len(scanner_eu_distances)):
        if scanner_i in visited: continue
        for scanner_j in visited:
            if scanner_i == scanner_j: continue
            matches = 0
            reps_dist_scanners = {0: {}, 1: {}, 2:{}}
            for scanner_dis in scanner_eu_distances[scanner_j]:
                if scanner_dis not in scanner_eu_distances[scanner_i]: continue
                matches += 1
                beacon_i = [int(i) for i in scanner_eu_distances[scanner_i][scanner_dis][0].split(',')]
                for m in pos:
                    beacon_i_orientation = [m[c][0] * beacon_i[0] + m[c][1] * beacon_i[1] + m[c][2] * beacon_i[2] for c in range(3)]
                    for line_num in range(0, 2):
                        beacon_j = [int(i) for i in scanner_eu_distances[scanner_j][scanner_dis][line_num].split(',')]
                        for coord in range(3):
                            dist_scanners = beacon_j[coord] - beacon_i_orientation[coord]
                            if dist_scanners not in reps_dist_scanners[coord]:
                                reps_dist_scanners[coord][dist_scanners] = {'count': 1, 'm': m[coord]}
                            else:
                                reps_dist_scanners[coord][dist_scanners]['count'] += 1

            if matches == 66: # n(n-1)/2 n=12
                # print('Adding ' + str(scanner_i) + ' using ' + str(scanner_j))
                visited.add(scanner_i)
                counts = [0,0,0]
                ms = [0, 0, 0]
                relative_pos = [0,0,0]
                for i in reps_dist_scanners:
                    for d in reps_dist_scanners[i]:
                        if reps_dist_scanners[i][d]['count'] >= counts[i]:
                            counts[i] = reps_dist_scanners[i][d]['count']
                            ms[i] = reps_dist_scanners[i][d]['m']
                            relative_pos[i] = d
                pos_scanners_relative[scanner_i]['from'] = scanner_j
                pos_scanners_relative[scanner_i]['pos'] = relative_pos
                pos_scanners_relative[scanner_i]['m'] = ms
                break

scanner_pos = [[0,0,0] for i in range(len(scanner_eu_distances))]
for scanner_i in pos_scanners_relative:
    scanner_from = pos_scanners_relative[scanner_i]['from']
    scanner_rel_pos = pos_scanners_relative[scanner_i]['pos']
    scanner_pos[scanner_i] = scanner_rel_pos
    while scanner_from != 0:
        from_scanner_rel = pos_scanners_relative[scanner_from]
        scanner_pos[scanner_i] = [
            scanner_rel_pos[0] * from_scanner_rel['m'][0][0] + scanner_rel_pos[1] * from_scanner_rel['m'][0][1] + scanner_rel_pos[2] * from_scanner_rel['m'][0][2] + from_scanner_rel['pos'][0],
            scanner_rel_pos[0] * from_scanner_rel['m'][1][0] + scanner_rel_pos[1] * from_scanner_rel['m'][1][1] + scanner_rel_pos[2] * from_scanner_rel['m'][1][2] + from_scanner_rel['pos'][1],
            scanner_rel_pos[0] * from_scanner_rel['m'][2][0] + scanner_rel_pos[1] * from_scanner_rel['m'][2][1] + scanner_rel_pos[2] * from_scanner_rel['m'][2][2] + from_scanner_rel['pos'][2],
        ]
        scanner_rel_pos = scanner_pos[scanner_i]
        scanner_from = pos_scanners_relative[scanner_from]['from']

computed = 0
beacons = set()
for scanner_i, scanner in enumerate(scanners_input):
    for line_i in range(len(scanner)):
        computed += 1
        scanner_i_pos = scanner_pos[scanner_i]
        beacon_coor = [int(i) for i in scanner[line_i].split(',')]
        prev_coor = [int(i) for i in scanner[line_i].split(',')]
        
        if scanner_i in pos_scanners_relative:
            scanner_from = scanner_i
            while scanner_from != 0:
                rotation_matrix_from = pos_scanners_relative[scanner_from]['m']
                beacon_coor = [
                    prev_coor[0] * rotation_matrix_from[0][0] + prev_coor[1] * rotation_matrix_from[0][1] + prev_coor[2] * rotation_matrix_from[0][2] ,
                    prev_coor[0] * rotation_matrix_from[1][0] + prev_coor[1] * rotation_matrix_from[1][1] + prev_coor[2] * rotation_matrix_from[1][2],
                    prev_coor[0] * rotation_matrix_from[2][0] + prev_coor[1] * rotation_matrix_from[2][1] + prev_coor[2] * rotation_matrix_from[2][2],
                ]
                prev_coor = [beacon_coor[0], beacon_coor[1], beacon_coor[2]]
                if pos_scanners_relative[scanner_from]['from'] in pos_scanners_relative:
                    scanner_from = pos_scanners_relative[scanner_from]['from']
                else:
                    scanner_from = 0

        beacon_coor = [
            beacon_coor[0] + scanner_i_pos[0], beacon_coor[1] + scanner_i_pos[1], beacon_coor[2] + scanner_i_pos[2]
        ]
        beacons.add(str(beacon_coor))

print('Total beacons ' + str(computed) + '. Different beacons: ' + str(len(beacons)))

def manhattan_distance(a, b):
    return sum([abs(xa-xb) for xa, xb in zip(a,b)])

def part2():
    max_manhattan_distance = 0
    for scanner_i_pos in range(len(scanner_pos)):
        for scanner_j_pos in range(scanner_i_pos + 1, len(scanner_pos)):
            max_manhattan_distance = max(max_manhattan_distance, manhattan_distance(scanner_pos[scanner_i_pos], scanner_pos[scanner_j_pos]))
    return max_manhattan_distance

print('Max Manhattan distance: ' + str(part2()))
