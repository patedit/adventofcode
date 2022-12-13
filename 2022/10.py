from advent import Advent

advent = Advent(2022, 10, use_file=False)

X, cycles = 1, 0
signal_strenth = 0

def _update_cycle():
    global cycles
    global signal_strenth
    cycles += 1
    if cycles in {20, 60, 100, 140, 180, 220}:
        signal_strenth += cycles * X

for instruction in advent.lines:
    op = instruction[:4]
    if op == 'noop': _update_cycle()
    elif op == 'addx':
        _update_cycle()
        _update_cycle() 
        X += int(instruction[5:])

# Part 1
print(signal_strenth)

X, n_cycle, sprite = 1, 0, ''
CRT_ROW_LEN = 40
def _update_sprite():
    global sprite
    sprite = '{}{}{}'.format('.' * (X - 1), '#' * 3, '.' * (CRT_ROW_LEN - (X - 1) - 3))

def _update_row(row: str):
    row += sprite[n_cycle % CRT_ROW_LEN]
    if len(row) == CRT_ROW_LEN:
        crt_rows.append(row)
        row = ''
    return row

crt_rows = []
current_row = ''

_update_sprite()

for instruction in advent.lines:
    op = instruction[:4]
    if op == 'noop':
        current_row = _update_row(current_row)
        n_cycle += 1
    else:
        current_row = _update_row(current_row)
        n_cycle += 1
        current_row = _update_row(current_row)
        n_cycle += 1
        X += int(instruction[5:])
        _update_sprite()

for crt_row in crt_rows:
    print(crt_row)
