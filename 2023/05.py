from advent import Advent

advent = Advent(2023, 5, use_file=False)

# Part 1
seeds = [int(s) for s in advent.paragraphs[0][0].split(': ')[1].split(' ')]
for j, seed in enumerate(seeds):
    if j == 0: continue
    for p in advent.paragraphs[1:]:
        for i in range(1, len(p)):
            ranges = [int(r) for r in p[i].split(' ')]
            if seeds[j] >= ranges[1] and seeds[j] <= (ranges[1] + ranges[2]):
                seeds[j] = int(ranges[0] + (seeds[j] - ranges[1]))
                break
print(min(seeds))


# Part 2
seeds = [int(s) for s in advent.paragraphs[0][0].split(': ')[1].split(' ')]
seeds_ranges = [(int(seeds[s]), int(seeds[s]) + int(seeds[s + 1]) - 1) for s in range(0, len(seeds), 2)]
# print(seeds)

pos_ranges = []
for j in range(len(seeds_ranges)):
    something = [seeds_ranges[j]]
    candidates = set(list(something))
    
    for p in advent.paragraphs[1:]:        
        something.extend(list(candidates) if candidates else [])
        
        while something:
            seed_range = something.pop()
            if seed_range in candidates:
                candidates.remove(seed_range)

            for p_i in range(1, len(p)):
                source, destination, l = [int(x) for x in p[p_i].split(' ')]
                if seed_range[0] >= destination and seed_range[1] <= destination + l - 1:
                    candidates.add((source + (seed_range[0] - destination), source + (seed_range[1] - destination)))
                if seed_range[0] < destination and seed_range[1] >= destination:
                    candidates.add((source, source + min(seed_range[1] - destination, l - 1)))
                    something.append((seed_range[0], destination - 1))
                    if seed_range[1] > destination + l - 1:
                        something.append((destination + l, seed_range[1]))
                if seed_range[0] >= destination and seed_range[0] < destination + l - 1 and seed_range[1] > (destination + l - 1):
                    candidates.add((source + (seed_range[0] - destination), source + (l - 1)))
                    something.append((destination + l, seed_range[1]))

    pos_ranges.extend(list(candidates))

print(min(pos_ranges)[0])
