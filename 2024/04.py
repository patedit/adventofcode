from advent import Advent

test="""
.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
"""
advent = Advent(2024, 4, test=None)
LEN_X = len(advent.lines)
LEN_Y = len(advent.lines[0])
POS_DIRS = [(x, y) for x in (0, 1, -1) for y in (0, 1, -1) if not (x == 0 and y == 0)]

def dfs(i, j, find_word, letter_idx, d):
    if i >= LEN_X or i < 0 or j >= LEN_Y or j < 0:
        return False

    if advent.lines[i][j] == find_word[letter_idx]:
        if letter_idx == len(find_word) - 1:
            return True
        if dfs(i + d[0], j + d[1], find_word, letter_idx + 1, d):
            return True

    return False

find_word = "XMAS"
word_times = 0
for i in range(LEN_X):
    for j in range(LEN_Y):
        if advent.lines[i][j] == find_word[0]:
            word_times += sum(dfs(i + n[0], j + n[1], find_word, 1, n) for n in POS_DIRS)
print(word_times)

find_word = "MAS"
find_word_reversed = find_word[::-1]
word_times = 0
for i in range(LEN_X):
    for j in range(LEN_Y):
        if advent.lines[i][j] == find_word[0]:
            for n in [(1, 1), (-1, -1), (-1, 1), (1, -1)]:
                if dfs(i + n[0], j + n[1], find_word, 1, n):
                    new_j = j + n[1] * 2
                    new_d = (n[0], -1 * n[1])
                    if dfs(i, new_j, find_word, 0, new_d) or dfs(i, new_j, find_word_reversed, 0, new_d):
                        word_times += 1 
                
print(word_times // 2)