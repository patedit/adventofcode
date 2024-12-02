from advent import Advent

advent = Advent(2024, 2)

lines = advent.lines

def is_seq_monotonic(sequence):
    return all(x < y for x, y in zip(sequence, sequence[1:])) or all(x > y for x, y in zip(sequence, sequence[1:]))

def is_report_safe(levels):
    return is_seq_monotonic(levels) and all(abs(levels[i - 1] - levels[i]) <= 3 for i in range(1, len(levels)))

def can_report_be_safe(levels):
    for i in range(len(levels)):
        new_levels = levels[:i] + levels[i + 1:]
        if is_report_safe(new_levels):
            return True
    return False

safe_reports = 0
can_be_safe_reports = 0

for l in lines:
    levels = [int(x) for x in l.split(" ")]
    if is_report_safe(levels):
        safe_reports += 1
    else:
        if can_report_be_safe(levels):
            can_be_safe_reports += 1
            
print(safe_reports)
print(safe_reports + can_be_safe_reports)