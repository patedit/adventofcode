from advent import Advent

advent = Advent(2022, 1)

# part 1
max_calories = 0
for elf in advent.paragraphs:
    elf_calories = sum(elf)
    max_calories = max(max_calories, elf_calories)
print(max_calories)

# part 2
sum_calories = [sum(elf) for elf in advent.paragraphs]
sum_calories.sort(reverse=True)
print(sum(sum_calories[:3]))