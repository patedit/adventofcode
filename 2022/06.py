from advent import Advent

advent = Advent(2022, 6)

communication = advent.lines[0]

def first_diff_char(min_len):
    for i in range(len(communication) - 1):
        if len(set(communication[i : i + min_len])) == min_len:
            return i + min_len

# Part 1
print(first_diff_char(4))

# Part 2
print(first_diff_char(14))