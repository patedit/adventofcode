from advent import Advent
import re

advent = Advent(2021, 17)

ns = re.findall(r'[-\d]+', advent.lines[0])

x_target = (int(ns[0]), int(ns[1]))
y_target = (int(ns[2]), int(ns[3]))

max_y = 0
max_vel = ()

def _passed_target(x, y):
    return x > x_target[1] or y < y_target[0]

def _inside_target(x, y):
    return x >= x_target[0] and x <= x_target[1] and y >= y_target[0] and y <= y_target[1] 

def _try_velocity(x_vel, y_vel):
    vel_max_y = 0
    x, y = 0, 0
    while not _inside_target(x, y) and not _passed_target(x, y):
        x += x_vel
        y += y_vel
        vel_max_y = max(vel_max_y, y)
        if x_vel > 0:
            x_vel -= 1
        y_vel -= 1
    return _inside_target(x, y), vel_max_y

for x_vel in range(150):
    for y_vel in range(150):
        in_target, cur_max_y = _try_velocity(x_vel, y_vel)
        if in_target and cur_max_y > max_y:
            max_y = cur_max_y
            max_vel = (x_vel, y_vel)

print(max_vel, max_y)

# Part 2
distinct_velocities = 0
for x_vel in range(-500, 500, 1):
    for y_vel in range(-500, 500, 1):
        in_target, cur_max_y = _try_velocity(x_vel, y_vel)
        if in_target:
            distinct_velocities += 1

print(distinct_velocities)