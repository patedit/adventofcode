from advent import Advent
import re
from math import prod

advent = Advent(2022, 11, use_file=False)

_EXTRACT_MONKEY_INFO = {
    0: lambda l: int(re.search("Monkey (\\d+)", l).group(1)),
    1: lambda l: [int(item) for item in l.split("Starting items: ")[1].split(", ")],
    2: lambda l: l.split("Operation: new = ")[1],
    3: lambda l: int(re.search("divisible by (\\d+)", l).group(1)),
    4: lambda l: int(re.search("If true: throw to monkey (\\d+)", l).group(1)),
    5: lambda l: int(re.search("If false: throw to monkey (\\d+)", l).group(1))
}

def parse_input():
    monkeys = []
    for monkey_info in advent.paragraphs:
        monkey_args = [_EXTRACT_MONKEY_INFO[i](line) for i, line in enumerate(monkey_info)]
        monkeys.append(Monkey(monkey_args))
    return monkeys

class MonkeyItem:
    def __init__(self, worry_level: int) -> None:
        self.worry_level = int(worry_level)

class Monkey:
    def __init__(self, args: list) -> None:
        self.items = []
        self.total_inspects = 0
        self.id = args[0]
        for item in args[1]:
            self.add_item(MonkeyItem(item))
        self.op = "lambda old: " + args[2]
        self.divisible_by = args[3]
        self.throw_monkey_true = args[4]
        self.throw_monkey_false = args[5]

    def _throw_item(self, monkey_item: MonkeyItem) -> tuple[int, MonkeyItem]:
        if monkey_item.worry_level % self.divisible_by == 0:
            return (self.throw_monkey_true, monkey_item)
        return (self.throw_monkey_false, monkey_item)

    def can_inspect(self):
        return len(self.items) > 0

    def inspect(self, worry_fn):
        if len(self.items) == 0: return
        new_worry = eval(worry_fn)(int(eval(self.op)(self.items.pop(0).worry_level)))
        new_monkey_item = MonkeyItem(new_worry)
        self.total_inspects += 1
        return self._throw_item(new_monkey_item)

    def add_item(self, item: MonkeyItem) -> None:
        self.items.append(item)

def monkey_business(part):
    monkeys = parse_input()
    rounds = 20 if part == 1 else 10_000
    monkeys_prod = prod([monkey.divisible_by for monkey in monkeys])
    reduce_worry_fn = "lambda worry: worry // 3" if part == 1 else "lambda worry: worry % {}".format(monkeys_prod)
    for _ in range(rounds):
        for monkey in monkeys:
            while monkey.can_inspect():
                monkey_i, monkey_item = monkey.inspect(reduce_worry_fn)
                monkeys[monkey_i].add_item(monkey_item)
    monkeys = sorted(monkeys, key=lambda monkey: monkey.total_inspects, reverse=True)
    return monkeys[0].total_inspects * monkeys[1].total_inspects

# Part 1
print(monkey_business(1))

# Part 2
print(monkey_business(2))
