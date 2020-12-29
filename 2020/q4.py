from advent import Advent

advent = Advent(4)

# Part 1
fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}
valid = 0 
for passport in advent.paragraphs:
    passport_fields = set([field.split(':')[0] for line in passport for field in line.split(' ')])
    sub_fields = fields - passport_fields
    valid += len(sub_fields) == 0 or sub_fields == {'cid'}

print('Part I: {}'.format(valid))


# Part 2
import re

validate_fields = {
    'byr': lambda x: int(x) >= 1920 and int(x) <= 2002,
    'iyr': lambda x: int(x) >= 2010 and int(x) <= 2020,
    'eyr': lambda x: int(x) >= 2020 and int(x) <= 2030,
    'hgt': lambda x: int(x[:-2]) >= 150 and int(x[:-2]) <= 193 if x[-2:] == 'cm' else int(x[:-2]) >= 59 and int(x[:-2]) <= 76 if x[-2:] == 'in' else False,
    'hcl': lambda x: re.match("^#[a-f0-9]{6}$", x) or False,
    'ecl': lambda x: x in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
    'pid': lambda x: re.match("^[0-9]{9}$", x) or False,
    'cid': lambda x: True
}

valid = 0 

fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
valid = 0 
for passport in advent.paragraphs:
    paragraph_valid_fields = set()
    for line in passport:
        for e in line.split(' '):
            k, v = e.split(':')
            if k != 'cid' and validate_fields[k](v):
                paragraph_valid_fields.add(k)
    
    sub_fields = fields - paragraph_valid_fields
    valid += len(sub_fields) == 0

print('Part II: {}'.format(valid))
