from advent import Advent

advent = Advent(2022, 1)

# part 1
max_calories = max([sum(elf) for elf in advent.paragraphs])
print(max_calories)

# part 2
sum_calories = sorted([sum(elf) for elf in advent.paragraphs], reverse=True)
print(sum(sum_calories[:3]))