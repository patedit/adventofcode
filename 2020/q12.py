from advent import Advent

TEST_IN = "F10\n\
N3\n\
F7\n\
R90\n\
F11"

advent = Advent(12, test=None)

card_points_vec = {
    "E": (1, 0),
    "S": (0, -1),
    "W": (-1, 0),
    "N": (0, 1)
}
def manhattan_distance(coord):
    return sum([abs(c) for c in coord])

# Part 1
ordered_card_points = ["E", "S", "W", "N"] # Each 90 degrees apart
facing_coord = "E"
ship_coord = [0, 0]

for instruction in advent.lines:
    action, value = instruction[0], int(instruction[1:])

    if action == 'F':
        facing_card_point = card_points_vec[facing_coord]
        ship_coord = [ship_coord[i] + facing_card_point[i] * value for i in range(len(ship_coord))]
    elif action in ['R', 'L']:
        value = value if action == 'R' else -value
        facing_coord_idx = ordered_card_points.index(facing_coord)
        facing_coord_idx = (facing_coord_idx + value // 90) % len(ordered_card_points)
        facing_coord = ordered_card_points[facing_coord_idx]
    elif action in card_points_vec:
        idx_dir = 1 if card_points_vec[action][0] == 0 else 0
        ship_coord[idx_dir] += card_points_vec[action][idx_dir] * value

print(manhattan_distance(ship_coord))


# Part 2
waypoint_rel_coord = [10, 1]
ship_coord = [0, 0]

waypoint_rotated = {
    0: lambda w: [w[0], w[1]],
    90: lambda w: [w[1], -w[0]],
    180: lambda w: [-w[0], -w[1]],
    270: lambda w: [-w[1], w[0]]
}

for instruction in advent.lines:
    action, value = instruction[0], int(instruction[1:])

    if action == 'F':
        ship_coord = [ship_coord[i] +  waypoint_rel_coord[i] * value for i in range(len(ship_coord))]
    elif action in ['R', 'L']:
        value = value if action == 'R' else -value
        waypoint_rel_coord = waypoint_rotated[value % 360](waypoint_rel_coord)
    elif action in card_points_vec:
        idx_dir = 1 if card_points_vec[action][0] == 0 else 0
        waypoint_rel_coord[idx_dir] += card_points_vec[action][idx_dir] * value

print(manhattan_distance(ship_coord))