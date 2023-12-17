from advent import Advent

advent = Advent(2023, 4, use_file=False)

# Part 1
s = 0
for line in advent.lines:
    winning_numbers, card_numbers = line.split(': ')[1].split(' | ')

    winning_numbers = set([int(x) for x in winning_numbers.split(' ') if x])
    card_numbers = set([int(x) for x in card_numbers.split(' ') if x])
    n = card_numbers.intersection(winning_numbers)
    s += 2**(len(n) - 1) if n else 0
print(s)


# Part 2
repeats = [1 for _ in range(len(advent.lines))]
for i, line in enumerate(advent.lines):
    winning_numbers, card_numbers = line.split(': ')[1].split(' | ')

    winning_numbers = set([int(x) for x in winning_numbers.split(' ') if x])
    card_numbers = set([int(x) for x in card_numbers.split(' ') if x])
    n = card_numbers.intersection(winning_numbers)
    for j in range(i + 1, i + len(n) + 1):
        repeats[j] += repeats[i]

print(sum(repeats))
