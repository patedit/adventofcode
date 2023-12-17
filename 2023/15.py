from advent import Advent

advent = Advent(2023, 15, use_file=False)

def hash(s):
    curr_value = 0
    for c in s:
        curr_value += ord(c)
        curr_value *= 17
        curr_value %= 256
    return curr_value

# Part 1
print(sum(hash(s) for s in advent.lines[0].split(',')))

# Part 2
boxes = [[] for _ in range(256)]

def find_box(box, l):
    return next((i for i, lens in enumerate(box) if list(lens.keys())[0] == l), -1)

for seq in advent.lines[0].split(','):
    if seq[-1] == '-':
        label = seq[:-1]

        h = hash(label)
        box_i = find_box(boxes[h], label)
        if boxes[h] and box_i >= 0:
            del boxes[h][box_i]

    elif seq[-2] == '=':
        label = seq[:-2]
        value = int(seq[-1])
    
        h = hash(label)
        box_i = find_box(boxes[h], label)

        if box_i >= 0:
            boxes[h][box_i][label] = value
        else:
            boxes[h].append({label: value})

focus = 0
for box_i, box in enumerate(boxes):
    focus += sum([(box_i + 1) * (slot + 1) * focal_len for slot, l in enumerate(box) for _, focal_len in l.items()])
print(focus)
