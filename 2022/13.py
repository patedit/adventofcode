from advent import Advent
from functools import cmp_to_key
import json

advent = Advent(2022, 13, use_file=False)

packets = [json.loads(p) for p in advent.lines]

ORDER_RIGHT = 1
ORDER_WRONG = -1
ORDER_UNKNOWN = 0

def _compare_n(n1, n2):
    return ORDER_RIGHT if n1 < n2 else ORDER_WRONG if n1 > n2 else ORDER_UNKNOWN

def compare(left, right):
    if type(left) != type(right):
        left = [left] if isinstance(left, int) else left
        right = [right] if isinstance(right, int) else right
    
    if isinstance(left, int):
        return _compare_n(left, right)

    elif isinstance(left, list):
        for l, r in zip(left, right):
            r = compare(l, r)
            if r != ORDER_UNKNOWN: return r
        return _compare_n(len(left), len(right))

# Part 1
sum_indices = 0
for i, (first, second) in enumerate(zip(packets[::2], packets[1::2])):
    sum_indices += (i + 1) if compare(first, second) == ORDER_RIGHT else 0
print(sum_indices)

# Part 2
DIVIDER_1, DIVIDER_2 = [[2]], [[6]]
packets.extend([DIVIDER_1, DIVIDER_2])

packets = sorted(packets, key=cmp_to_key(compare), reverse=True)

divider_indice_1, divider_indice_2 = [i + 1 for i in range(len(packets)) if packets[i] in [DIVIDER_1, DIVIDER_2]]

print(divider_indice_1 * divider_indice_2)