from advent import Advent
from collections import Counter

advent = Advent(2021, 14)

template = advent.paragraphs[0][0]
mappings = {}
for mapping in advent.paragraphs[1]:
    mp = mapping.split(' -> ')
    mappings[mp[0]] = mp[1]
STEPS = 10
for step in range(STEPS):
    new_template = ''
    for i in range(len(template) - 1):
        new_template += template[i] + mappings[template[i] + template[i+1]]
    template = str(new_template) + template[-1]

c = Counter(template)
print(max(c.values()) - min(c.values()))

# Part 2
STEPS = 40
template = advent.paragraphs[0][0]

mappings = {}
freq_letters = {}
for mapping in advent.paragraphs[1]:
    mp = mapping.split(' -> ')
    mappings[mp[0]] = [mp[0][0] + mp[1], mp[1] + mp[0][1]]
    freq_letters[mp[1]] = 0

tuple_freq = {k: 0 for k in mappings.keys()}

for i in range(len(template) - 1):
    tuple_freq[template[i] + template[i + 1]] = 1

steps = 0
while steps < STEPS:
    new_tuple_freq = dict(tuple_freq)
    for pair in new_tuple_freq:
        if new_tuple_freq[pair] >= 1:
            freq = new_tuple_freq[pair]
            tuple_freq[mappings[pair][0]] += freq
            tuple_freq[mappings[pair][1]] += freq
            tuple_freq[pair] -= freq
    steps += 1

for pair in tuple_freq:
    if tuple_freq[pair] >= 1:
        freq_letters[pair[1]] += tuple_freq[pair]

freq_val = freq_letters.values()
print(max(freq_val) - min(freq_val))

