from advent import Advent
import re

advent = Advent(2)

# Part 1
valid_passwords = 0
for pwd in advent.lines:
    min_rep, max_rep, letter, password = re.findall(r'(\d+)-(\d+) (\w): (\w+)', pwd)[0]
    count = password.count(letter)
    valid_passwords += int(min_rep) <= count <= int(max_rep)

print(valid_passwords)

# Part 2
valid_passwords = 0
for pwd in advent.lines:
    pos_1, pos_2, letter, password = re.findall(r'(\d+)-(\d+) (\w): (\w+)', pwd)[0]
    pos_1 = int(pos_1) - 1
    pos_2 = int(pos_2) - 1
    valid_passwords += password[pos_1] != password[pos_2] and (password[pos_1] == letter or password[pos_2] == letter)

print(valid_passwords)
