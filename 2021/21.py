from advent import Advent

advent = Advent(2021, 21)

players_pos = [int(advent.lines[0][-1]), int(advent.lines[1][-1])]
scores = [0, 0]
MAX_SCORE = 1000

rolls = 0
dice_n = 1

while max(scores) < MAX_SCORE:
    spaces, player = 0, rolls % 2
    for i in range(3):
        spaces, dice_n = spaces + dice_n, dice_n % 100 + 1

    new_player_position = (players_pos[player] + spaces) % 10
    players_pos[player] = 10 if new_player_position == 0 else new_player_position
    scores[player] += players_pos[player]

    rolls += 3

print(min(scores) * rolls)
