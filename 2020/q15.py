from advent import Advent

TEST_IN = "0,3,6"
advent = Advent(15, test=None)

def play_game(steps):
    starting_numbers = [int(n) for n in advent.lines[0].split(',')]
    seen_nums_idx = {k: [0, i] for i, k in enumerate(starting_numbers[:-1])}

    game = starting_numbers + [0] * (steps - len(starting_numbers))

    for i in range(len(starting_numbers), len(game)):
        last_spoken = game[i - 1]
        if last_spoken in seen_nums_idx:
            second_closest, closest = seen_nums_idx[last_spoken]
            game[i] = closest - second_closest
            if game[i] in seen_nums_idx:
                seen_nums_idx[game[i]] = [seen_nums_idx[game[i]][1], i]
        else:
            seen_nums_idx[last_spoken] = [0, i - 1]
            seen_nums_idx[0] = [seen_nums_idx[0][1], i]

    return game

# Part 1
print(play_game(2020)[-1])

# Part 2
print(play_game(30000000)[-1])
