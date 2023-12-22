from advent import Advent
import re
from functools import reduce

advent = Advent(2023, 19, use_file=False)

def read_parts(parts_in):
    matches = re.findall(r'(\w)=([0-9]+)', parts_in)
    return {k: int(v) for k, v in matches}

def read_workflow(workflow_in):
    matches = re.findall(r'(\w+){(.*?)}', workflow_in)
    return {
        matches[0][0]: {
            'rules': [r.split(':') for r in matches[0][1].split(',')[:-1]],
            'default': matches[0][1].split(',')[-1]
        }
    }

parts = [read_parts(p) for p in advent.paragraphs[1]]
workflows = {}
[workflows.update(read_workflow(w)) for w in advent.paragraphs[0]]


# Part 1
def eval_workflow(workflow_name, x, m, a, s):
    if workflow_name not in workflows: return workflow_name
    for rule in workflows[workflow_name]['rules']:
        condition, destination = rule
        if eval(condition):
            return eval_workflow(destination, x, m, a, s)
    return eval_workflow(workflows[workflow_name]['default'], x, m, a, s)

sum_rating_numbers = 0
for part in parts:
    x, m, a, s = [part[k] for k in 'xmas']
    final_workflow = eval_workflow('in', x, m, a, s)
    if final_workflow == 'A':
        sum_rating_numbers += sum([x, m, a, s])

print(sum_rating_numbers)


# Part 2
def workflow_combinations(ranges, workflow_name):
    if workflow_name == 'A':
        return reduce(lambda a, k: a * (ranges[k][1] - ranges[k][0] + 1), 'xmas', 1)
    if workflow_name == 'R':
        return 0
    combinations = 0
    opposite_range = dict(ranges)
    for rules in workflows[workflow_name]['rules']:
        v, n = rules[0][0], int(rules[0][2:])
        new_ranges = dict(opposite_range)
        if '>' in rules[0]:
            new_ranges[v] = [max(n + 1, opposite_range[v][0]), opposite_range[v][1]]
            opposite_range[v] = [opposite_range[v][0], n]
        else:
            new_ranges[v] = [opposite_range[v][0], min(n - 1, opposite_range[v][1])]
            opposite_range[v] = [n, opposite_range[v][1]]

        combinations += workflow_combinations(new_ranges, rules[1])
    combinations += workflow_combinations(opposite_range, workflows[workflow_name]['default'])
    return combinations

ranges = {
    'x': [1, 4000],
    'm': [1, 4000],
    'a': [1, 4000],
    's': [1, 4000],
}
print(workflow_combinations(ranges, 'in'))
