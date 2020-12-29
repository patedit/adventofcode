from advent import Advent

advent = Advent(9)

PREAMBLE_LEN = 25

# Part 1
previous_preamble = {}
def is_valid_sum(previous_preamble, s):
    for n in previous_preamble:
        if (s - n) in previous_preamble and n != (s - n):
            return True

    return False

for i in range(PREAMBLE_LEN, len(advent.lines)):
    next_sum = advent.lines[i]
    previous_preamble = set(advent.lines[i - PREAMBLE_LEN : i])
    if not is_valid_sum(previous_preamble, next_sum):
        break

print(next_sum)

# Part 2
invalid_number = next_sum

lower_idx, upper_idx, total_sum = 0, 0, -1
while total_sum != invalid_number:
    if total_sum > invalid_number:
        lower_idx += 1
    elif total_sum < invalid_number:
        upper_idx += 1

    total_sum = sum(advent.lines[lower_idx : upper_idx + 1])

s = advent.lines[lower_idx : upper_idx + 1]
print(max(s) + min(s))
