from advent import Advent
import re

advent = Advent(16)

passport_fields = advent.paragraphs[0]
field_intervals = {}
for field in passport_fields:
    field_name_intervals = re.findall(r'^(.*): (\d+)-(\d+) or (\d+)-(\d+)$', field)[0]
    field_name = field_name_intervals[0]
    field_intervals[field_name] = [(int(field_name_intervals[i]), int(field_name_intervals[i+1])) for i in range(1, 4, 2)]

my_ticket = [int(f) for f in advent.paragraphs[1][1:][0].split(',')]

nearby_tickets = advent.paragraphs[2][1:]

# Part 1
nearby_valid_tickets = []
invalid_sum = 0
for ticket in nearby_tickets:
    valid_ticket = True
    for n in ticket.split(','):
        n = int(n)
        valid_n = False
        for first_interval, second_interval in field_intervals.values():
            if first_interval[0] <= n <= first_interval[1] or second_interval[0] <= n <= second_interval[1]:
                valid_n = True
                break
        if valid_n is False:
            invalid_sum += n
            valid_ticket = False
            
    if valid_ticket: # for part 2
        nearby_valid_tickets.append([int(f) for f in ticket.split(',')])

print(invalid_sum)

# Part 2
def find_pos_fields(ticket_field):
    pos_fields = set()
    for field_name in field_intervals:
        for interval in field_intervals[field_name]:
            if interval[0] <= ticket_field <= interval[1]:
                pos_fields.add(field_name)
                break
    
    return pos_fields

all_pos_fields = [0] * len(field_intervals)
for i in range(len(field_intervals)):
    all_pos_fields[i] = set(field_intervals.keys())
    
    for nearby_ticket in nearby_valid_tickets:
        field_ticket = nearby_ticket[i]
        possible_ticket_fields = find_pos_fields(field_ticket)
        all_pos_fields[i] = all_pos_fields[i].intersection(possible_ticket_fields)

unordered_pos_fields = all_pos_fields
all_pos_fields = sorted(all_pos_fields, key=len)
fields_matched = set()
for i in range(len(all_pos_fields)):
    all_pos_fields[i] -= fields_matched
    fields_matched.update(all_pos_fields[i] - fields_matched)

product = 1
for i, f in enumerate(my_ticket):
    if any(t.startswith("departure") for t in unordered_pos_fields[i]):
        product *= f

print(product)
