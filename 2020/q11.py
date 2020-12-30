from advent import Advent
import copy 


TEST_INPUT = "L.LL.LL.LL\n\
LLLLLLL.LL\n\
L.L.L..L..\n\
LLLL.LL.LL\n\
L.LL.LL.LL\n\
L.LLLLL.LL\n\
..L.L.....\n\
LLLLLLLLLL\n\
L.LLLLLL.L\n\
L.LLLLL.LL"

OCCUPIED_SEAT = '#'
EMPTY_SEAT = 'L'
FLOOR_SEAT = '.'

adjacent_seats = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, 1), (1, 0), (1, -1)]

advent = Advent(11, test=None)
seats = [list(row) for row in advent.lines]
columns_len = len(seats[0])
rows_len = len(seats)

def is_seat_occupied(row, column):
    return seats[row][column] == OCCUPIED_SEAT

def is_seat_empty(row, column):
    return seats[row][column] == EMPTY_SEAT

def is_seat_floor(row, column):
    return seats[row][column] == FLOOR_SEAT

def is_seat_in_bounds(row, column):
    return 0 <= row < rows_len and 0 <= column < columns_len

def count_total_occupied():
    return sum([is_seat_occupied(row, column) for row in range(0, rows_len) for column in range(0, columns_len)])

def change_seats(count_closest_occupied, max_adjacent_seats = 4):
    seat_map_changes = {}
    has_changes = True
    while has_changes:
        for k, v in seat_map_changes.items():
            for r, c in v:
                seats[r][c] = k

        seat_map_changes = {OCCUPIED_SEAT : [], EMPTY_SEAT: []}
        has_changes = False
        for seat_row in range(0, rows_len):
            for seat_column in range(0, columns_len):
                if is_seat_empty(seat_row, seat_column) and count_closest_occupied(seat_row, seat_column) == 0:
                    seat_map_changes[OCCUPIED_SEAT].append((seat_row, seat_column))
                    has_changes = True
                elif is_seat_occupied(seat_row, seat_column) and count_closest_occupied(seat_row, seat_column) >= max_adjacent_seats:
                    seat_map_changes[EMPTY_SEAT].append((seat_row, seat_column))
                    has_changes = True

# Part 1
def count_adjacent_occupied_seats(row, column):
    occupied = 0
    for adjacent in adjacent_seats:
        if is_seat_in_bounds(row + adjacent[0], column + adjacent[1]):
            occupied += is_seat_occupied(row + adjacent[0], column + adjacent[1])
    return occupied
            

change_seats(count_adjacent_occupied_seats)
print(count_total_occupied())


# Part 2
seats = [list(row) for row in advent.lines]

def count_closest_occupied_seats(row, column):
    occupied = 0
    for adjacent in adjacent_seats:
        closest_row, closest_column = row + adjacent[0], column + adjacent[1]
        while is_seat_in_bounds(closest_row, closest_column) and is_seat_floor(closest_row, closest_column):
            closest_row += adjacent[0]
            closest_column += adjacent[1]
        
        if is_seat_in_bounds(closest_row, closest_column):
            occupied += is_seat_occupied(closest_row, closest_column)

    return occupied

change_seats(count_closest_occupied_seats, 5)
print(count_total_occupied())