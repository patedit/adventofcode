from advent import Advent
import enum

class HandType(enum.Enum):
    Rock = 1
    Paper = 2
    Scissors = 3

    @classmethod
    def from_letter(self, l):
        if l in ['A', 'X']: return HandType.Rock
        if l in ['B', 'Y']: return HandType.Paper
        if l in ['C', 'Z']: return HandType.Scissors

    def score(self):
        if self == HandType.Rock: return 1
        if self == HandType.Paper: return 2
        if self == HandType.Scissors: return 3

class Hand():
    WON_SCORE = 6
    DRAW_SCORE = 3
    LOST_SCORE = 0
    players_hand = [None, None]

    def __init__(self, p1, p2) -> None:
        self.players_hand[0] = HandType.from_letter(p1)
        self.players_hand[1] = HandType.from_letter(p2)

    def player_score(self, pi):
        score_hand = self.players_hand[pi].score()
        game_score = Hand.LOST_SCORE
        if self.players_hand[0] == self.players_hand[1]: game_score = Hand.DRAW_SCORE
        if self.players_hand[pi] == HandType.Rock and self.players_hand[not pi] == HandType.Scissors: game_score = Hand.WON_SCORE
        if self.players_hand[pi] == HandType.Paper and self.players_hand[not pi] == HandType.Rock: game_score = Hand.WON_SCORE
        if self.players_hand[pi] == HandType.Scissors and self.players_hand[not pi] == HandType.Paper: game_score = Hand.WON_SCORE
        return score_hand + game_score

advent = Advent(2022, 2)

# part 1
my_score = 0
for game in advent.lines:
    hand = Hand(game[0], game[2])
    my_score += hand.player_score(1)

print(my_score)

# part 2
my_score = 0
for game in advent.lines:
    opponent_hand = HandType.from_letter(game[0])
    desired_outcome = game[2]
    hand_score, game_score = 0, 0
    if desired_outcome == 'X':
        game_score = Hand.LOST_SCORE
        if opponent_hand == HandType.Rock: hand_score = HandType.Scissors.score()
        if opponent_hand == HandType.Paper: hand_score = HandType.Rock.score()
        if opponent_hand == HandType.Scissors: hand_score = HandType.Paper.score()
    if desired_outcome == 'Y': # we need to draw
        game_score = Hand.DRAW_SCORE
        hand_score = opponent_hand.score()
    if desired_outcome == 'Z': # we need to win
        game_score = Hand.WON_SCORE
        if opponent_hand == HandType.Rock: hand_score = HandType.Paper.score()
        if opponent_hand == HandType.Paper: hand_score = HandType.Scissors.score()
        if opponent_hand == HandType.Scissors: hand_score = HandType.Rock.score()
    my_score += game_score + hand_score

print(my_score)