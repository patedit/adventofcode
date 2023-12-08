def main():
    with open('q5_input.txt') as q5file:
        i = 0
        lines = [0, 0]
        for line in q5file:
            lines[i] = line.rstrip('\n').split(',')
            i += 1

    first_wire_coordinates = all_coordinates_for_commands(list(lines[0]))
    second_wire_coordinates = all_coordinates_for_commands(list(lines[1]))

    min_steps = 9999999
    for coord in first_wire_coordinates:
        if coord in second_wire_coordinates:
            total_steps = first_wire_coordinates[coord] + second_wire_coordinates[coord]
            if total_steps > 0 and total_steps < min_steps:
                min_steps = total_steps

    print(min_steps)

def all_coordinates_for_commands(commands):
    wire_coordinates = {}
    i = 0
    j = 0
    total_steps = 0
    for command in commands:
        direction = command[0]
        steps = int(command[1:])
        orig_x = i
        orig_y = j
        if direction == 'U':
            i += steps
            orig_x += 1
        elif direction == 'D':
            i -= steps
            orig_x -= 1
        elif direction == 'R':
            j += steps
            orig_y += 1
        elif direction == 'L':
            j -= steps
            orig_y -= 1
        else:
            print("Error!!")

        if orig_x != i:
            temp = 1 if orig_x < i else -1
            for diff in range(orig_x, i + temp, temp):
                total_steps += 1
                if (diff, j) not in wire_coordinates:
                    wire_coordinates[(diff, j)] = total_steps
        elif orig_y != j:
            temp = 1 if orig_y < j else -1
            for diff in range(orig_y, j + temp, temp):
                total_steps += 1
                if (i, diff) not in wire_coordinates:
                    wire_coordinates[(i, diff)] = total_steps

    return wire_coordinates

if __name__ == "__main__":
    main() 