from advent import Advent

import re
import time

advent = Advent(2022, 15, use_file=False)

start_time = time.time()

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

sensors, closest_beacons, distances = [], [], []
beacons = set()
for line in advent.lines:
    sx, sy, bx, by = map(int, re.findall( "-?\d+", line))

    sensors.append((sx, sy))
    closest_beacons.append((bx, by))
    distances.append(manhattan((sx, sy), (bx, by)))
    beacons.add((bx, by))

def no_beacons_slow(y_check):
    no_beacons, visited = 0, set()
    for i in range(len(sensors)):
        sensor, distance = sensors[i], distances[i]
        for dx in [1, -1]:
            pos_p = (sensor[0], y_check)
            while manhattan(sensor, pos_p) <= distance:
                if pos_p not in beacons and pos_p not in visited:
                    no_beacons += 1
                    visited.add(pos_p)
                pos_p = (pos_p[0] + dx, pos_p[1])

    return no_beacons

def no_beacons_fast(y_check):
    xh, xl = float('-inf'), float('inf')
    for i in range(len(sensors)):
        sensor, distance = sensors[i], distances[i]
        diff = distance - abs(y_check - sensor[1])
        if diff > 0:
            xl = min(xl, sensor[0] - diff)
            xh = max(xh, sensor[0] + diff)
    return xh - xl

# Part 1
Y_CHECK = 2000000
print(no_beacons_fast(Y_CHECK))
print("--- %s seconds ---" % (time.time() - start_time))
print(no_beacons_slow(Y_CHECK))
print("--- %s seconds ---" % (time.time() - start_time))


def available_point():

    def get_next_line_limits(sensor, distance):
        i, j = sensor[0] - distance, sensor[1]
        for di, dj in [(1, -1), (1, 1), (-1, 1), (-1, -1)]:
            while i < sensor[0]:
                if 0 <= i <= MAX and 0 <= j <= MAX: yield ((i, j))
                i += di
                j += dj

    for sensor, distance in zip(sensors, distances):
        for (lx, ly) in get_next_line_limits(sensor, distance + 1):
            sensors_out_limit = 0
            for i in range(len(sensors)):
                if manhattan(sensors[i], (lx, ly)) <= distances[i]:
                    break
                sensors_out_limit += 1
            if sensors_out_limit == len(sensors):
                return lx * 4000000 + ly

# Part 2
MAX = 4000000
print(available_point())
print("--- %s seconds ---" % (time.time() - start_time))