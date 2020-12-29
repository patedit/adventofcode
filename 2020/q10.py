from advent import Advent

advent = Advent(10)

# Part 1
jolts = set(advent.lines)
max_jolt = max(jolts)

def find_path(current_jolt, steps):
    if current_jolt != 0 and current_jolt not in jolts or current_jolt > max_jolt:
        return None
    if current_jolt == max_jolt:
        return steps
    
    for i in range(1, len(steps) + 1):
        new_steps = steps.copy()
        new_steps[i - 1] += 1
        path = find_path(current_jolt + i, new_steps)
        if path:
            return path

    return None

steps = find_path(0, [0, 0, 0])
print(steps[0] * (steps[2] + 1))
