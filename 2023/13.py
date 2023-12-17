from advent import Advent

advent = Advent(2023, 13, use_file=False)

def get_columns(array, i, j):
    columns = []
    for k in range(i, j):
        columns.append(''.join([array[q][k] for q in range(len(array))]))
    return columns

def find_reflection(pattern):
    min = 0
    for i in range(1, len(pattern)):
        if i > len(pattern) // 2:
            min = i - (len(pattern) - i)
        if pattern[min : i] == pattern[i : i + (i - min)][::-1]:
            return 100 * i


    min = 0
    for j in range(1, len(pattern[0])):
        if j > len(pattern[0]) // 2:
            min = j - (len(pattern[0]) - j)
        if get_columns(pattern, min, j) == get_columns(pattern, j, j + (j - min))[::-1]:
            return 1 * j
    return s

# Part 1
s = 0
for pattern in advent.paragraphs:
    s += find_reflection(pattern)
print(s)

# Part 2
def find_smudge(pattern):
    min = 0
    for i in range(1, len(pattern)):
        diff = 0
        if i > len(pattern) // 2:
            min = i - (len(pattern) - i)
        for c1, c2 in zip(pattern[min : i], pattern[i : i + (i - min)][::-1]):
            diff += sum([1 for ccc1, ccc2 in zip(*[c1, c2]) if ccc1 != ccc2])
        if diff == 1:
            return 100 * i


    min = 0
    for j in range(1, len(pattern[0])):
        diff = 0
        if j > len(pattern[0]) // 2:
            min = j - (len(pattern[0]) - j)
        for c1, c2 in zip(get_columns(pattern, min, j), get_columns(pattern, j, j + (j - min))[::-1]):
            diff += sum([1 for ccc1, ccc2 in zip(*[c1, c2]) if ccc1 != ccc2])
        if diff == 1:
            return 1 * j

    return s

s = 0
for pattern in advent.paragraphs:
    s += find_smudge(pattern)
print(s)