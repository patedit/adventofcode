from advent import Advent

advent = Advent(2021, 13)

points = advent.paragraphs[0]
ins = advent.paragraphs[1]

paper = [['.' for i in range(2000)] for j in range(2000)]
paper_size_i, paper_size_j = 0, 0
for point in points:
    j, i = [int(p) for p in point.split(',')]
    paper[i][j] = '#'
    paper_size_i = max(paper_size_i, i + 1)
    paper_size_j = max(paper_size_j, j + 1)

fold_instructions = []
for instruction in ins:
    ins_axis, ins_coor = instruction.split('fold along ')[1].split('=')
    ins_coor = int(ins_coor)
    fold_instructions.append([ins_axis, ins_coor])

def print_paper():
    for r in range(paper_size_i):
        row = []
        for c in range(paper_size_j):
            row.append(paper[r][c])
        print(''.join([str(r) for r in row]))
    
def sum_paper():
    return sum([sum(1 for k in p[:paper_size_j] if k == '#') for p in paper[:paper_size_i]])

def fold(n):
    global paper_size_i, paper_size_j
    for fold_instruction in fold_instructions[:n]:
        axis, coord = fold_instruction
        if axis == 'y':
            for i in range(coord + 1, paper_size_i):
                for j in range(paper_size_j):
                    if paper[i][j] == '#':
                        paper[2 * coord - i][j] = '#'
            paper_size_i = coord
        elif axis == 'x':
            for i in range(paper_size_i):
                for j in range(coord + 1, paper_size_j):
                    if paper[i][j] == '#':
                        paper[i][2 * coord - j] = '#'
            paper_size_j = coord
fold(len(fold_instructions))
print_paper()
print(sum_paper())