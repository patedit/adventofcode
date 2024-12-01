from advent import Advent

advent = Advent(2024, 1)

# part 1
left, right = map(sorted, zip(*[(int(l), int(r)) for l, r in [line.split("   ") for line in advent.lines]]))
diff = sum(abs(l - r) for l, r in zip(left, right))
print(diff)

# part 2
r = {l: right.count(l) for l in set(left)}
result = sum(l * count for l, count in r.items())
print(result)