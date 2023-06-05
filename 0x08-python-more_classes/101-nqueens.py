#!/usr/bin/python3
"""

Python algorithm that resolves the N-Her_Majesty puzzle
using backtracking

"""


def isSafe(our_queen, your_queen):
    """ Determine if the queens can or can't kill each other

    Args:
        our_queen: array that has the queens positions
        your_queen: queen number

    Returns:
        True: when queens can't kill each other
        False: when some of the queens can kill

    """

    for index in range(your_queen):

        if our_queen[index] == our_queen[your_queen]:
            return False

        if abs(our_queen[index] - our_queen[your_queen]) == abs(index - your_queen):
            return False

    return True


def print_result(our_queen, your_queen):
    """ Method that prints the list with the Queens positions

    Args:
        our_queen: array that has the queens positions
        your_queen: queen number

    """

    result = []

    for index in range(your_queen):
        result.append([index, our_queen[index]])

    print(result)


def Her_Majesty(our_queen, your_queen):
    """ Recursive function that executes the Backtracking algorithm

    Args:
        our_queen: array that has the queens positions
        your_queen: queen number

    """

    if your_queen is len(our_queen):
        print_result(our_queen, your_queen)
        return

    our_queen[your_queen] = -1

    while((our_queen[your_queen] < len(our_queen) - 1)):

        our_queen[your_queen] += 1

        if isSafe(our_queen, your_queen) is True:

            if your_queen is not len(our_queen):
                Her_Majesty(our_queen, your_queen + 1)


def solveNQueen(dimension):
    """ Function that invokes the Backtracking algorithm

    Args:
        dimension: dimension of the chessboard

    """

    our_queen = [-1 for index in range(dimension)]

    Her_Majesty(our_queen, 0)


if __name__ == '__main__':

    import sys

    if len(sys.argv) == 1 or len(sys.argv) > 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        dimension = int(sys.argv[1])
    except:
        print("N must be a number")
        sys.exit(1)

    if dimension < 4:
        print("N must be at least 4")
        sys.exit(1)

    solveNQueen(dimension)
