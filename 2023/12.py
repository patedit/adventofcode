import functools
from itertools import product
from advent import Advent

advent = Advent(2023, 12, use_file=False)

'''
Keeping here the original solution for part 1 (brute force) because why not

total_combinations = 0
for line in advent.lines:
    record, groups = line.split(' ')[0], tuple([int(i) for i in line.split(' ')[1].split(',')])
    # TODO Improve. Max lenght is 18 so 2^18 should be doable. refactor using part 2
    index = 0
    indices = []
    while index < len(record):
        index = record.find('?', index)
        if index == -1: break
        indices.append(index)
        index += 1
    for p in product('.#', repeat=len(indices)):
        for c, idx in zip(p, indices):
            record = record[:idx] + c + record[idx+1:]
        if valid_record(record, groups):
            total_combinations += 1

print(total_combinations)
'''

def valid_record(record, group):
    group_i = 0
    record_i = 0
    while record_i < len(record) and group_i < len(group):
        if record[record_i] == '.':
            record_i += 1
        elif record[record_i] == '#':
            start_i = record_i
            while record_i < len(record) and record[record_i] == '#':
                record_i += 1
            if record_i - start_i != group[group_i]:
                return False
            group_i += 1
        else:
            return False
    return group_i == len(group) and (record_i == len(record) or '#' not in record[record_i:])

@functools.lru_cache
def count(record, group):
    if valid_record(record, group):
        return 1
    if not record or not group:
        return 0
    
    result = 0
    if record[0] in ".?":
        result += count(record[1:], group)
    if record[0] in "#?":
        if group[0] <= len(record) and "." not in record[:group[0]] and (group[0] == len(record) or record[group[0]] != '#'):
            result += count(record[group[0] + 1:], group[1:])

    return result

# Part 1
total_combinations = 0
for line in advent.lines:
    record, groups = line.split(' ')[0], tuple([int(i) for i in line.split(' ')[1].split(',')])
    total_combinations += count(record, groups)

print(total_combinations)

# Part 2
total_combinations = 0
for line in advent.lines:
    record, groups = line.split(' ')[0], tuple([int(i) for i in line.split(' ')[1].split(',')])

    record = '?'.join(record for _ in range(5))
    groups = groups * 5

    total_combinations += count(record, groups)

print(total_combinations)
