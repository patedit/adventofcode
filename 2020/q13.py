from advent import Advent
import math

TEST_IN = "939\n\
7,13"

advent = Advent(13, test=TEST_IN)

# Part 1
timestamp = advent.lines[0]
bus_ids = [int(bus_id) for bus_id in advent.lines[1].split(',') if bus_id != 'x']

min_next_timestamp = float('inf')
next_bus_available = None
for bus_id in bus_ids:
    next_bus_departure = bus_id * math.ceil(timestamp / bus_id)
    if min_next_timestamp > next_bus_departure:
        min_next_timestamp = next_bus_departure
        next_bus_available = bus_id

print(next_bus_available * (min_next_timestamp - timestamp))

# Part 2
buses_offset = [(int(bus_id), int(i)) for i, bus_id in enumerate(advent.lines[1].split(',')) if bus_id != 'x']

next_pos_interval = buses_offset[0][0]
ts = 0
for bus_freq, offset in buses_offset[1:]:
    while (ts + offset) % bus_freq != 0:
        ts += next_pos_interval
    next_pos_interval *= bus_freq

print(ts)
