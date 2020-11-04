def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


def get_matrix_first_diagonal(matrix):
    n = len(matrix)
    return set(matrix[i][i] for i in range(n))


def get_matrix_second_diagonal(matrix):
    n = len(matrix)
    return set(matrix[i][n-i-1] for i in range(n))


def is_set_winning(symbols_set):
    assert isinstance(symbols_set, set)

    return len(symbols_set) == 1


def get_rows_winner(board):
    for row in board:
        # if all symbols in a row are the same
        if is_set_winning(set(row)):
            return row[0]
    return None


def get_columns_winner(board):
    # check rows on transposed board will check columns instead
    return get_rows_winner(transpose(board))


def get_diagonals_winner(board):
    n = len(board)

    # check first diagonal
    if is_set_winning(get_matrix_first_diagonal(board)):
        return board[0][0]

    # check second diagonal
    if is_set_winning(get_matrix_second_diagonal(board)):
        return board[0][n-1]

    return None


def get_tic_tac_toe_winner(board):
    """
    Returns winner symbol if one is found
    Returns None if there is no winner
    """
    row_winner = get_rows_winner(board)
    if row_winner:
        return row_winner

    column_winner = get_columns_winner(board)
    if column_winner:
        return column_winner

    diagonal_winner = get_diagonals_winner(board)
    return diagonal_winner


print(get_tic_tac_toe_winner(
    [['x', 'o', 'o'],
     ['x', 'o', 'x'],
     ['x', 'x', 'o']]))
print(get_tic_tac_toe_winner(
    [['o', 'o', 'o'],
     ['x', 'o', 'x'],
     ['x', 'x', 'o']]))
print(get_tic_tac_toe_winner(
    [['o', 'x', 'o'],
     ['x', 'o', 'x'],
     ['x', 'x', 'o']]))
print(get_tic_tac_toe_winner(
    [['x', 'o', 'x'],
     ['o', 'x', 'x'],
     ['x', 'x', 'o']]))
print(get_tic_tac_toe_winner(
    [['o', 'x', 'o'],
     ['x', 'o', 'x'],
     ['x', 'x', 'o']]))
print(get_tic_tac_toe_winner(
    [['x', 'x', 'o'],
     ['o', 'o', 'x'],
     ['x', 'x', 'o']]))
