from advent import Advent
import math

advent = Advent(5)

def find_value_bounds(lower_half_c, lower_half_v, upper_half_c, upper_half_v, values):
    for v in values:
        if v == lower_half_c:
            upper_half_v = (lower_half_v + upper_half_v) // 2
        elif v == upper_half_c:
            lower_half_v = (lower_half_v + 1 + upper_half_v) // 2
    return upper_half_v


# Part 1
highest_seat_id = 0
for seat in advent.lines:
    row = find_value_bounds('F', 0, 'B', 127, seat[:7])
    column = find_value_bounds('L', 0, 'R', 7, seat[7:])

    seat_id = row * 8 + column
    highest_seat_id = max(seat_id, highest_seat_id)

print(highest_seat_id)


# Part 2
all_seats = []
for seat in advent.lines:
    row = find_value_bounds('F', 0, 'B', 127, seat[:7])
    column = find_value_bounds('L', 0, 'R', 7, seat[7:])

    seat_id = row * 8 + column
    all_seats.append(seat_id)

s = 0
for i in range(min(all_seats), max(all_seats) + 1):
    s += i
print(s - sum(all_seats))