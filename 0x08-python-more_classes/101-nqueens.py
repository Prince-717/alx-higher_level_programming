#!/usr/bin/python3
"""Works out the N-queens puzzle"""

import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    chess_board = []
    [chess_board.append([]) for index in range(n)]
    [board_row.append(' ') for index in range(n) for board_row in chess_board]
    return (chess_board)


def board_deepcopy(chess_board):
    """Return a deepcopy of a chessboard."""
    if isinstance(chess_board, list):
        return list(map(board_deepcopy, chess_board))
    return (chess_board)


def get_solution(chess_board):
    """Return the list of lists representation of a solved chessboard."""
    answer = []
    for q in range(len(chess_board)):
        for b in range(len(chess_board)):
            if chess_board[q][b] == "Q":
                answer.append([q, b])
                break
    return (answer)


def xout(chess_board, board_row, board_column):
    """X out spots on a chessboard.

    All spots where non-attacking queens can no
    longer be played are X-ed out.

    Args:
        chess_board (list): The current working chessboard.
        board_row (int): The board_row where a queen was last played.
        board_column (int): The column where a queen was last played.
    """
    # X out all forward spots
    for b in range(board_column + 1, len(chess_board)):
        chess_board[board_row][b] = "x"
    # X out all backwards spots
    for b in range(board_column - 1, -1, -1):
        chess_board[board_row][b] = "x"
    # X out all spots below
    for q in range(board_row + 1, len(chess_board)):
        chess_board[q][board_column] = "x"
    # X out all spots above
    for q in range(board_row - 1, -1, -1):
        chess_board[q][board_column] = "x"
    # X out all spots diagonally down to the right
    b = board_column + 1
    for q in range(board_row + 1, len(chess_board)):
        if b >= len(chess_board):
            break
        chess_board[q][b] = "x"
        b += 1
    # X out all spots diagonally up to the left
    b = board_column - 1
    for q in range(board_row - 1, -1, -1):
        if b < 0:
            break
        chess_board[q][b]
        b -= 1
    # X out all spots diagonally up to the right
    b = board_column + 1
    for q in range(board_row - 1, -1, -1):
        if b >= len(chess_board):
            break
        chess_board[q][b] = "x"
        b += 1
    # X out all spots diagonally down to the left
    b = board_column - 1
    for q in range(board_row + 1, len(chess_board)):
        if b < 0:
            break
        chess_board[q][b] = "x"
        b -= 1


def recursive_solve(chess_board, board_row, queens, solutions):
    """Recursively solve an N-queens puzzle.

    Args:
        chess_board (list): The current working chessboard.
        board_row (int): The current working board_row.
        queens (int): The current number of placed queens.
        solutions (list): A list of lists of solutions.
    Returns:
        solutions
    """
    if queens == len(chess_board):
        solutions.append(get_solution(chess_board))
        return (solutions)

    for b in range(len(chess_board)):
        if chess_board[board_row][b] == " ":
            tmp_board = board_deepcopy(chess_board)
            tmp_board[board_row][b] = "Q"
            xout(tmp_board, board_row, b)
            solutions = recursive_solve(tmp_board, board_row + 1,
                                        queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    chess_board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(chess_board, 0, 0, [])
    for ans in solutions:
        print(ans)
