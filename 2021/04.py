from advent import Advent

advent = Advent(2021, 4)
MARKED = -1

numbers_to_draw = [int(n) for n in advent.paragraphs[0][0].split(',')]
boards_unparsed = advent.paragraphs[1:]
boards = [[0] * 5 for i in range(len(boards_unparsed))]
for idx, board_unparsed in enumerate(boards_unparsed):
    for board_row_idx, board_unparsed_row in enumerate(board_unparsed):
        board_unparsed_row = board_unparsed_row.split(' ')
        board_row = []
        for board_unparsed_row_num in board_unparsed_row:
            if board_unparsed_row_num.isnumeric():
                board_row.append(int(board_unparsed_row_num))

        boards[idx][board_row_idx] = board_row

# Part 1
def _has_won(board, i, j):
    return (sum(board[i]) == MARKED * len(board[i])) or (sum([board[ix][j] for ix in range(len(board))]) == MARKED * len(board[i]))

def _sum_unmarked_board(board):
    board_sum = 0
    for i, row in enumerate(board):
        for j, n in enumerate(row):
            board_sum += n if board[i][j] != MARKED else 0

    return board_sum

def _mark_number_board(number_to_draw, board):
    for i, row in enumerate(board):
        for j, n in enumerate(row):
            if n == number_to_draw:
                board[i][j] = MARKED
                return _has_won(board, i, j)

    return False


for number_to_draw in numbers_to_draw:
    has_won = False
    for board in boards:
        if _mark_number_board(number_to_draw, board):
            board_sum = _sum_unmarked_board(board)
            print(number_to_draw * board_sum)
            has_won = True
            break
    if has_won:
        break


# Part 2
last_board = []
idx_to_remove = set()
last_index_removed = -1
for number_to_draw in numbers_to_draw:
    for board_idx, board in enumerate(boards):
        if board_idx in idx_to_remove:
            continue
        if _mark_number_board(number_to_draw, board):
            idx_to_remove.add(board_idx)
            last_index_removed = board_idx

    if len(idx_to_remove) == len(boards):
        break
board_sum = _sum_unmarked_board(boards[last_index_removed])
print(number_to_draw * board_sum)
