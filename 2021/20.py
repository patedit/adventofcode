from advent import Advent
import copy

advent = Advent(2021, 20)

image_algorithm = advent.paragraphs[0][0]
image = [[str(i) for i in line] for line in advent.paragraphs[1]]

_GRID_BIN = {
    '#': 1,
    '.': 0
}
_EXPAND_BY = 3
_GRID_TO_DEC_CACHE = {}

def enhance_grid(grid):
    if len(grid) != 9: raise Exception('Grid must be lenght 9')
    dec_v = _GRID_TO_DEC_CACHE[grid] if grid in _GRID_TO_DEC_CACHE else int(''.join([str(_GRID_BIN[c]) for c in grid]), 2)    
    if grid not in _GRID_TO_DEC_CACHE:
        _GRID_TO_DEC_CACHE[grid] = dec_v
    return image_algorithm[dec_v]

def print_image():
    for i in range(len(image)):
        line = ''
        for j in range(len(image[i])):
            line += image[i][j]
        print(line)
    print('\n')

def enhance_image(runs):
    global image
    for run in range(runs):
        infinity_ch = '.' if run == 0 else image[0][0]
        iter_grid = [[infinity_ch for j in range(len(image[0]) + _EXPAND_BY * 2)] for i in range(len(image) + _EXPAND_BY * 2)]
        for i in range(len(image)):
            for j in range(len(image[i])):
                iter_grid[i+_EXPAND_BY][j+_EXPAND_BY] = image[i][j]
        image = copy.deepcopy(iter_grid)
        
        for i in range(len(image)):
            for j in range(len(image[i])):
                grid = ''
                for grid_i in [i - 1, i + 0, i + 1]:
                    for grid_j in [j - 1, j +  0, j + 1]:
                        if grid_i >= 0 and grid_i < len(image) and grid_j >= 0 and grid_j < len(image[grid_i]):
                            grid += image[grid_i][grid_j]
                        else:
                            grid += infinity_ch
                iter_grid[i][j] = enhance_grid(grid)
        
        image = copy.deepcopy(iter_grid)

def count_lights():
    return sum([1 for j in range(_EXPAND_BY, len(image[0]) - _EXPAND_BY) for i in range(_EXPAND_BY, len(image) - _EXPAND_BY) if image[i][j] == '#'])

enhance_image(2)
print(count_lights())

image = [[str(i) for i in line] for line in advent.paragraphs[1]]
enhance_image(50)
print(count_lights())
