from advent import Advent
advent = Advent(2019, 1)

# part 1
total_fuel = 0
for mass in advent.lines:
    total_fuel += int(mass) // 3 - 2
print(total_fuel)

# part 2
total_fuel = 0
def comp_fuel(mass):
    fuel = mass // 3 - 2
    if (fuel > 0):
        fuel += comp_fuel(fuel)
    else:
        fuel = 0
    return fuel
for mass in advent.lines:
    total_fuel += comp_fuel(int(mass))
print(total_fuel)
