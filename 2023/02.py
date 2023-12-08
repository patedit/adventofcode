from advent import Advent

advent = Advent(2023, 2, use_file=False)


# Part 1 and 2
s_game_ids = 0
s_power = 0 # part 2

for line in advent.lines:
  max_colors = {
    'blue': 0,
    'red': 0,
    'green': 0,
  }
  game_id, bags = line[len('Game') + 1:].split(': ')
  rounds = bags.split('; ')
  for round in rounds:
    for t in round.split(', '):
      cnt, color = t.split(' ')
      if int(cnt) > max_colors[color]:
        max_colors[color] = int(cnt)
  if max_colors['blue'] <= 14 and max_colors['green'] <= 13 and max_colors['red'] <= 12:
    s_game_ids += int(game_id)
  # Part 2
  s_power += max_colors['blue'] * max_colors['green'] * max_colors['red']

print(s_game_ids)
print(s_power)
