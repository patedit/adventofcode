from advent import Advent

advent = Advent(2021, 6)

DAYS_P1 = 80
lanterfishes = [int(l) for l in advent.lines[0].split(',')]

# Part 1
for day in range(1, DAYS_P1 + 1):
    for lanter_i in range(len(lanterfishes)):
        if lanterfishes[lanter_i] == 0:
            lanterfishes[lanter_i] = 6
            lanterfishes.append(8)
        else:
            lanterfishes[lanter_i] -= 1
         
print(len(lanterfishes))

# Part 2
DAYS_P2 = 256
days = [0] * 9
lanterfishes = [int(l) for l in advent.lines[0].split(',')]
for lanter in lanterfishes:
    days[lanter] += 1

for day in range(DAYS_P2):
    temp = days[len(days) - 1]
    for i in range(len(days) - 2, -1, -1):
        temp, days[i] = days[i], temp
    days[8] = temp
    days[6] += temp

print(sum(days))