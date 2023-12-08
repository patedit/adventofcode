from advent import Advent

advent = Advent(2021, 3)

MAX_POWER = 12
result_bin = [0] * MAX_POWER

for line in advent.lines:
    line = int(str(line), 2)
    for power in range(MAX_POWER):
        mask = 2**power
        result = line & mask
        result_bin[len(result_bin) - power - 1] += 1 if result > 0 else 0

gamma_rate, epsilon_rate = '', ''
for result_bit in result_bin:
    gamma_rate += '1' if result_bit > len(advent.lines) // 2 else '0'
    epsilon_rate += '0' if result_bit > len(advent.lines) // 2 else '1'
print(int(gamma_rate, 2) * int(epsilon_rate, 2))

# Part 2
def _masks_at_index(ratings, idx):
    mask_one = list()
    mask_zero = list()
    mask = 2**idx
    for rating in ratings:
        is_mask_one = int(str(rating), 2) & mask > 0
        if is_mask_one:
            mask_one.append(rating)
        else:
            mask_zero.append(rating)

    return mask_one, mask_zero

oxy_ratings = list(advent.lines)
co2_ratings = list(advent.lines)

for i in range(MAX_POWER - 1, -1, -1):
    if len(oxy_ratings) <= 1 and len(co2_ratings) <= 1:
        break

    if len(oxy_ratings) > 1:
        mask_one, mask_zero = _masks_at_index(oxy_ratings, i)
        oxy_ratings = mask_one if len(mask_one) >= len(mask_zero) else mask_zero

    if len(co2_ratings) > 1:
        mask_one, mask_zero = _masks_at_index(co2_ratings, i)
        co2_ratings = mask_one if len(mask_one) < len(mask_zero) else mask_zero

print(int(str(oxy_ratings[0]), 2) * int(str(co2_ratings[0]), 2))