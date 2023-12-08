from advent import Advent

advent = Advent(2021, 8)

# Part 1
outputs = [line.split('|')[1].strip().split(' ') for line in advent.lines]
print(sum(1 for output in outputs for digit in output if len(digit) in {2, 4, 3, 7}))


'''
1 segment -> X
2 segments -> 1
3 segments -> 7
4 segments -> 4
5 segments -> 2, 3 (only with C and F, easy to find), 5
6 segments -> 0, 6, 9
7 segmetns -> 8

1 -> len(2)
7 -> len(3)
4 -> len(4)
8 -> len(7)
3 -> len(5) all segments that 7 (len(3)) all segments there
9 -> len(6) all segments that 3 (len7) has
0 -> len(3) all segments that appear and is not 9
6 -> reamining len(3) the other one
2 -> use 6 and 2 differences means 2. one diff means 5
'''

# Part 2
outputs_sum = 0
for line in advent.lines:
    display, outputs = line.split(' | ')
    mapping = {}

    patterns = display.split(' ')

    while len(mapping) < 10:
        for pattern in patterns:
            if set(pattern) in mapping.values(): continue
            if len(pattern) == 2:
                mapping[1] = set(pattern)
            elif len(pattern) == 3:
                mapping[7] = set(pattern)
            elif len(pattern) == 4:
                mapping[4] = set(pattern)
            elif len(pattern) == 7:
                mapping[8] = set(pattern)
            elif len(pattern) == 5:
                if 7 in mapping and len(mapping[7] - set(pattern)) == 0:
                    mapping[3] = set(pattern)
                elif 6 in mapping and len(mapping[6] - set(pattern)) == 2:
                    mapping[2] = set(pattern)
                elif 6 in mapping and len(mapping[6] - set(pattern)) == 1:
                    mapping[5] = set(pattern)
            elif len(pattern) == 6:
                if 3 in mapping and len(mapping[3] - set(pattern)) == 0:
                    mapping[9] = set(pattern)
                elif all(k in mapping for k in [7, 9]) and len(mapping[7] - set(pattern)) == 0:
                    mapping[0] = set(pattern)
                elif all(k in mapping for k in [0, 9]):
                    mapping[6] = set(pattern)


    output_digit = ''
    for output in outputs.split(' '):
        output_digit += str(list(mapping.keys())[list(mapping.values()).index(set(output))])
    outputs_sum += int(output_digit)
print(outputs_sum)