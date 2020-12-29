from advent import Advent
import re

DEBUG_TEST = "light red bags contain 1 bright white bag, 2 muted yellow bags.\ndark orange bags contain 3 bright white bags, 4 muted yellow bags.\nbright white bags contain 1 shiny gold bag.\nmuted yellow bags contain 2 shiny gold bags, 9 faded blue bags.\nshiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.\ndark olive bags contain 3 faded blue bags, 4 dotted black bags.\nvibrant plum bags contain 5 faded blue bags, 6 dotted black bags.\nfaded blue bags contain no other bags.\ndotted black bags contain no other bags."
advent = Advent(7, test=None)

# Part 1
bags = {}
def mark_gold_bags(bag):
    if bags[bag]['gold'] is True or len(bags[bag]['inner_bags']) == 0:
        return
    bags[bag]['gold'] = True
    for outer_bag in bags.keys():
        if bag in bags[outer_bag]['inner_bags']:
            mark_gold_bags(outer_bag)

for line in advent.lines:
    outer_bag_reg = re.match(r'(\w+ \w+) (bags|bag) contain', line)
    outer_bag = outer_bag_reg.group(1)
    inner_bags_reg = re.findall(r'(\d+) (\w+ \w+) (bags|bag)', line)
    inner_bags = set()
    for inner_bags_match in inner_bags_reg:
        inner_bags.add(inner_bags_match[1])
    
    if outer_bag in bags:
        bags[outer_bag]['inner_bags'].add(inner_bags)
    else:
        bags[outer_bag] = {'gold': False, 'inner_bags': inner_bags}
    
    should_mark_gold = False
    for inner_bag in inner_bags:
        if inner_bag in bags and bags[inner_bag]['gold'] is True:
            should_mark_gold = True
    should_mark_gold = should_mark_gold or 'shiny gold' in inner_bags
    if should_mark_gold and bags[outer_bag]['gold'] is False:
        mark_gold_bags(outer_bag)

c = sum([bags[bag]['gold'] for bag in bags])
print(c)


# Part 2
_bags = {}
for line in advent.lines:
    outer_bag_reg = re.match(r'(\w+ \w+) (bags|bag) contain', line)
    outer_bag = outer_bag_reg.group(1)
    inner_bags_reg = re.findall(r'(\d+) (\w+ \w+) (bags|bag)', line)
    inner_bags = {}
    for inner_bags_match in inner_bags_reg:
        inner_bags[inner_bags_match[1]] = inner_bags_match[0]
    
    _bags[outer_bag] = {'inner_bags': inner_bags}

def get_inner_bags_count(bag):
    if len(_bags[bag]['inner_bags']) == 0:
        return 0
    
    count = 0
    for inner_bag in _bags[bag]['inner_bags']:
        inner_bag_count = int(_bags[bag]['inner_bags'][inner_bag])
        count += inner_bag_count + inner_bag_count * get_inner_bags_count(inner_bag)
    return count

c = get_inner_bags_count('shiny gold')
print(c)

