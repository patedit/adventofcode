from advent import Advent
from collections import Counter

advent = Advent(2023, 7, use_file=False)

_HANDS_CHECKED = {}
def check_hand(hand):
    if hand in _HANDS_CHECKED:
        return _HANDS_CHECKED[hand]
    counter = Counter(hand)
    symbols = counter.keys()
    result = 1
    if len(symbols) == 1:
        # Five of a kind
        result = 10
    if len(symbols) == 2:
        if counter.most_common(1)[0][1] == 4:
            # Four of a kind
            result = 9
        else:
            # Full house
            result = 8
    if len(symbols) == 3:
        if counter.most_common(1)[0][1] == 3:
            # Three of a kind
            result = 7
        else:
            # Two pairs
            result = 6
    if len(symbols) == 4:
        # One pair
        result = 5

    _HANDS_CHECKED[hand] = result
    return result

import functools

def comp_hands(h1, h2):
    rh1 = check_hand(h1[0])
    rh2 = check_hand(h2[0])

    if rh1 == rh2:
        for h1_card, h2_card in zip(h1[0], h2[0]):
            if h1_card == h2_card: continue
            return 1 if card_order_dict[h1_card[0]] > card_order_dict[h2_card[0]] else -1
        return 0
    return 1 if rh1 > rh2 else -1

# Part 1
card_order_dict = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10, "J": 11, "Q":12, "K":13, "A":14}
all_hands = []
for l in advent.lines:
    all_hands.append((str(l.split(' ')[0]), int(l.split(' ')[1])))

total = 0
for i, hand in enumerate(sorted(all_hands, key=functools.cmp_to_key(comp_hands))):
    total += (i+1) * hand[1]
print(total)


# Part 2
from collections import deque
def generate_combinations(s):
    queue = deque([s])
    result = []
    replaced = set()
    while queue:
        current = queue.popleft()
        if 'J' in current:
            for r in card_order_dict.keys():
                n = current.replace('J', r, 1)
                if n not in replaced:
                  queue.append(n)
                  replaced.add(n)
        else:
            result.append(current)

    return result

def compare2(h1, h2):
    rh1 = check_hand(h1)
    rh2 = check_hand(h2)

    if rh1 == rh2:
        for a, b in zip(h1, h2):
            if card_order_dict[a[0]] > card_order_dict[b[0]]:
                return 1
            elif card_order_dict[a[0]] < card_order_dict[b[0]]:
                return -1
        return 0
    return 1 if rh1 > rh2 else -1

def find_best_hand(hand):
    hands = [hand]
    if 'J' in hand:
        hands = generate_combinations(hand)
    best_hand = sorted(hands, key=functools.cmp_to_key(compare2))[-1]
    return (best_hand, hand)

def comp_hands2(h1, h2):
    rh1 = check_hand(h1[0])
    rh2 = check_hand(h2[0])

    if rh1 == rh2:
        for h1_orig_card, h2_orig_card in zip(h1[2], h2[2]):
            if h1_orig_card == h2_orig_card: continue
            return 1 if card_order_dict[h1_orig_card[0]] > card_order_dict[h2_orig_card[0]] else -1
        return 0
    return 1 if rh1 > rh2 else -1

# Part 2
card_order_dict = {"J": 1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10, "Q":12, "K":13, "A":14}
all_hands_bids = []
for l in advent.lines:
    h, x = find_best_hand(l.split(' ')[0])
    all_hands_bids.append((h, int(l.split(' ')[1]), x))

ordered_hands = sorted(all_hands_bids, key=functools.cmp_to_key(comp_hands2))
total = 0
for i, hand in enumerate(ordered_hands):
    total += (i + 1) * hand[1]
print(total)
