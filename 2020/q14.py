from advent import Advent
from itertools import permutations
import re

TEST_IN = "mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X\n\
mem[8] = 11\n\
mem[7] = 101\n\
mem[8] = 0"

TEST_IN_P2 = "mask = 000000000000000000000000000000X1001X\n\
mem[42] = 100\n\
mask = 00000000000000000000000000000000X0XX\n\
mem[26] = 1"

advent = Advent(14, test=None)

def read_mask(line):
    mask_match = re.match(r'mask = (\w{36})', line)
    if mask_match:
        return mask_match.group(1)
    return None

def read_mem(line):
    mem_match = re.match(r'mem\[(\d+)\] = (\d+)', line)
    if mem_match:
        return int(mem_match.group(1)), int(mem_match.group(2))
    return None, None


current_masks = []
local_mem = {}
for line in advent.lines:
    mask = read_mask(line)
    if mask:
        current_masks = [int(mask.replace('X', '1'), 2), int(mask.replace('X', '0'), 2)]
    
    mem_addr, mem_val = read_mem(line)
    if mem_addr and mem_val:
        masked_val = int(mem_val) & current_masks[0] | current_masks[1]
        local_mem[mem_addr] = masked_val

print(sum(local_mem.values()))


# Part 2
advent = Advent(14, test=None)

local_mem = {}
non_floating_mask = None
floating_masks = []
for line in advent.lines:
    mask = read_mask(line)
    if mask:
        non_floating_mask = int(mask.replace('X', '0'), 2)
        floating_points = [pos for pos, char in enumerate(mask) if char == 'X']
        exp_comb = len(floating_points)
        floating_masks = []
        for floating_point in range(2 ** exp_comb):
            bin_comb = bin(floating_point)[2:].zfill(exp_comb)
            mask = ['0'] * 36
            for i, c in enumerate(bin_comb):
                mask[floating_points[i]] = c
            floating_masks.append(int(''.join(mask), 2))

    
    mem_addr, mem_val = read_mem(line)
    if mem_addr and mem_val:
        masked_non_float_mem = mem_addr | non_floating_mask
        for floating_mask in floating_masks:
            masked_memory = masked_non_float_mem ^ floating_mask
            local_mem[masked_memory] = mem_val

print(sum(local_mem.values()))