from advent import Advent

advent = Advent(2022, 17, use_file=False)

push_jet_moves = []
for p in advent.lines[0]:
    if p == '>': push_jet_moves.append(1)
    if p == '<': push_jet_moves.append(-1)

CONSTANT = 1000
grid = [['.' for __ in range(7)] for _ in range(CONSTANT)]

push_jet_index = 0
def push_jet(shape, i, j=2, steps=1):
    global push_jet_index
    for _ in range(steps):
        d = push_jet_moves[push_jet_index]
        if d == 1:
            if can_move_right([i, j], shape['type']):
                j += 1
        if d == -1:
            if can_move_left([i, j], shape['type']):
                j -= 1

        push_jet_index += 1
        if push_jet_index == len(push_jet_moves):
            push_jet_index = 0

    return j

shape_index = 0

_SHAPES = [
    {'type': 0, 'height': 1, 'width': 4},
    {'type': 1, 'height': 3, 'width': 3},
    {'type': 2, 'height': 3, 'width': 3},
    {'type': 3, 'height': 4, 'width': 1},
    {'type': 4, 'height': 2, 'width': 2}
]
def can_move_down(pos, type):
    i, j = pos
    
    if type == 0:
        height = 1
        if i + height >= len(grid): return False
        if grid[i + 1][j] == '#' or grid[i + 1][j + 1] == '#' or grid[i + 1][j + 2] == '#' or grid[i + 1][j + 3] == '#':
            return False
        return True
    if type == 1:
        if i + 2 >= len(grid) - 1: return False
        if grid[i + 2][j] == '#' or grid[i + 3][j + 1] == '#' or grid[i + 2][j + 2] == '#':
            return False
        return True
    if type == 2:
        if i + 2 >= len(grid) - 1: return False
        if grid[i + 3][j] == '#' or grid[i + 3][j + 1] == '#' or grid[i + 3][j + 2] == '#':
            return False
        return True
    if type == 3:
        height = 4
        if i + height >= len(grid): return False
        if grid[i + height][j] == '#': return False
        return True
    if type == 4:
        height = 2
        if i + height >= len(grid): return False
        if grid[i + height][j] == '#' or grid[i + height][j + 1] == '#': return False
        return True

def can_move_left(pos, type):
    i, j = pos
    if j <= 0: return False
    
    if type == 0:
        if grid[i][j - 1] == '#': return False
        return True
    if type == 1:
        if grid[i][j] == '#' or grid[i + 1][j - 1] == '#' or grid[i+2][j] == '#': return False
        return True

    if type == 2:
        if grid[i][j+1] == '#' or grid[i+1][j+1] == '#' or grid[i+2][j-1] == '#': return False
        return True
    if type == 3:
        if grid[i][j-1] == '#' or grid[i+1][j-1] == '#' or grid[i+2][j-1] == '#' or grid[i+3][j-1] == '#': return False
        return True
    if type == 4:
        if grid[i][j-1] == '#' or grid[i+1][j-1] == '#': return False
        return True 

def can_move_right(pos, type):
    i, j = pos
    
    if type == 0:
        final_j = j + 4 - 1
        if final_j >= len(grid[0]) - 1: return False
        if grid[i][final_j + 1] == '#': return False
        return True
    if type == 1:
        final_j = j + 3 - 1
        if final_j >= len(grid[0]) - 1: return False
        if grid[i][j + 2] == '#' or grid[i + 1][j + 3] == '#' or grid[i+2][j + 2] == '#': return False
        return True
    if type == 2:
        final_j = j + 3 - 1
        if final_j >= len(grid[0]) - 1: return False
        if grid[i][j + 3] == '#' or grid[i + 1][j + 3] == '#' or grid[i+2][j + 3] == '#': return False
        return True
    if type == 3:
        final_j = j + 1 - 1
        if final_j >= len(grid[0]) - 1: return False
        if grid[i][j + 1] == '#' or grid[i + 1][j + 1] == '#' or grid[i + 2][j + 1] == '#' or grid[i + 3][j + 1] == '#': return False
        return True
    if type == 4:
        final_j = j + 2 - 1
        if final_j >= len(grid[0]) - 1: return False
        if grid[i][j + 2] == '#' or grid[i + 1][j + 2] == '#': return False
        return True

def draw_shape(pos, type):
    i, j = pos
    if type == 0:
        grid[i][j] = '#'
        grid[i][j+1] = '#'
        grid[i][j+2] = '#'
        grid[i][j+3] = '#'
    if type == 1:
        grid[i][j+1] = '#'
        grid[i+1][j] = '#'
        grid[i+1][j+1] = '#'
        grid[i+1][j+2] = '#'
        grid[i+2][j+1] = '#'
    if type == 2:
        grid[i][j+2] = '#'
        grid[i+1][j+2] = '#'
        grid[i+2][j] = '#'
        grid[i+2][j+1] = '#'
        grid[i+2][j+2] = '#'
    if type == 3:
        grid[i][j] = '#'
        grid[i+1][j] = '#'
        grid[i+2][j] = '#'
        grid[i+3][j] = '#'

    if type == 4:
        grid[i][j] = '#'
        grid[i][j+1] = '#'
        grid[i+1][j] = '#'
        grid[i+1][j+1] = '#'

top_i = len(grid)
curr_i = top_i - 3

ROUNDS = 2022
CHUNKS = 1000
for _ in range(ROUNDS):
    shape = _SHAPES[shape_index]
    curr_i -= shape['height']
    curr_j = 2

    curr_j = push_jet(shape, i=curr_i, j=curr_j, steps=1)
    while can_move_down([curr_i, curr_j], shape['type']):
        curr_i += 1
        curr_j = push_jet(shape, i=curr_i, j=curr_j, steps=1)
    
    # draw
    draw_shape([curr_i, curr_j], shape['type'])

    shape_index += 1
    if shape_index == len(_SHAPES):
        shape_index = 0

    top_i = min(top_i, curr_i)
    curr_i = top_i - 3

    # for g in grid:
    #     print(g)
    # print()
    # print(grid)


print(len(grid) - top_i)




