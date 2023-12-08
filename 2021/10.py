from advent import Advent

advent = Advent(2021, 10)

OPENING = {'{', '(', '<', '['}
CLOSING = {'}': 1197, ')': 3, '>': 25137, ']': 57}

def is_corrupted(opening, closing):
    return (closing == '}' and opening != '{') or (closing == ')' and opening != '(') or (closing == '>' and opening != '<') or (closing == ']' and opening != '[')

score = 0
for line in advent.lines:
    ops = []
    for c in line:
        if c in OPENING: ops.append(c)
        elif c in CLOSING and is_corrupted(ops.pop(), c):
            score += CLOSING[c]
            break
print(score)


# Part 2
CLOSING = {'}': 3, ')': 1, '>': 4, ']': 2}

def closing_for_opening(opening):
    if opening == '{': return '}'
    if opening == '(': return ')'
    if opening == '[': return ']'
    if opening == '<': return '>'

incomplete_scores = []
for line in advent.lines:
    ops = []
    for c in line:
        if c in OPENING: ops.append(c)
        elif c in CLOSING and is_corrupted(ops.pop(), c):
            ops.clear()
            break
    if len(ops) > 0:
        curr_score = 0
        for i in reversed(ops):
            curr_score = curr_score * 5 + CLOSING[closing_for_opening(i)]
        incomplete_scores.append(curr_score)

incomplete_scores.sort()
print(incomplete_scores[len(incomplete_scores) // 2])