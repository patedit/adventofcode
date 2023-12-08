from advent import Advent

advent = Advent(2019, 3)

def all_coordinates_for_commands(commands):
    wire_coordinates = set()
    i = 0
    j = 0
    for command in commands.split(','):
        direction = command[0]
        steps = int(command[1:])
        orig_x = i
        orig_y = j
        if direction == 'U':
            i += steps
        elif direction == 'D':
            i -= steps
        elif direction == 'R':
            j += steps
        elif direction == 'L':
            j -= steps
        else:
            print("Error!!")
        
        if orig_x != i:
            range1 = i if orig_x > i else orig_x
            range2 = orig_x if orig_x > i else i
            for diff in range(range1, range2):
                wire_coordinates.update([(diff, j)])
        elif (orig_y != j):
            range1 = j if orig_y > j else orig_y
            range2 = orig_y if orig_y > j else j
            for diff in range(range1, range2):
                wire_coordinates.update([(i, diff)])

    return wire_coordinates


first_wire_coordinates = set(all_coordinates_for_commands(advent.lines[0]))
second_wire_coordinates = set(all_coordinates_for_commands(advent.lines[1]))

intersections = first_wire_coordinates.intersection(second_wire_coordinates)

min_distance = float('inf')
for coor_x, coor_y in intersections:
    distance = abs(coor_x) + abs(coor_y)
    min_distance = min(min_distance, distance)
print(min_distance)

# if __name__ == "__main__":
#     main() 