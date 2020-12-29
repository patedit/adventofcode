from advent import Advent

TEST_INPUT_1 = "16\n10\n15\n5\n1\n11\n7\n19\n6\n12\n4"
TEST_INPUT_2  = "28\n33\n18\n42\n31\n14\n46\n20\n48\n47\n24\n23\n49\n45\n19\n38\n39\n11\n1\n32\n25\n35\n8\n17\n7\n9\n4\n2\n34\n10\n3"

advent = Advent(10, test=None)

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


# Part 2
jolts = advent.lines
jolts.sort()

max_jolt = jolts[-1]
adapters_valid_paths = {k : 0 for k in jolts}
adapters_valid_paths[max_jolt] = 1

for i in reversed(range(max_jolt)):
    if i in adapters_valid_paths:
        paths_for_jolt = sum([adapters_valid_paths[j] if j in adapters_valid_paths else 0 for j in range(i + 1, i + 4)])
        adapters_valid_paths[i] = paths_for_jolt

diff_ways = sum([adapters_valid_paths[i] if i in adapters_valid_paths else 0 for i in range(1, 4)])
print(diff_ways)