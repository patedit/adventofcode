puzzle_input_range = [307237, 769058]
possibles = []

def has_adjacents(num):
    single_digits = _list_single_digit(num)
    for i in range(1, len(single_digits)):
        if single_digits[i] == single_digits[i-1]:
            return True
    return False

def is_increasing(num):
    single_digits = _list_single_digit(num)
    for i in range(1, len(single_digits)):
        if single_digits[i] < single_digits[i-1]:
            return False
    return True

def _list_single_digit(num):
    num_str = str(num)
    list_single = [int(c) for c in num_str]
    return list_single

for n in range(puzzle_input_range[0], puzzle_input_range[1] + 1):
    if is_increasing(n) and has_adjacents(n):
        possibles.append(n)

print('All possibles is {}'.format(len(possibles)))
