# benefit of backtracking is that when it is properly implemented, we are guaranteed to find a solution, if one exists further, the solution will be more efficient than a brute-force exploration, since we weed out paths that are knowen to be invalid, a process known as pruning.

# backtracking cannot guarantee we will find an optimal solution and it often leads to factorial or exponential time complexity if we are required to choose one of M paths at each of N steps

# can you construct a partial solution?
# can you verify if the partial solution is invalid
# can you verify if the solution is complete

# queens puzzle.
# find number of ways N queens can be placed on the board withouth threatening each other. No two queens are allowed to share the same row, column or diagnal

# represent the board as a one-dimensional array of integers from 1 to n, where the value at index i represents the column the queen on row i.
# reason being each row can place single queen
def n_queens(n, board=[]):
    # return to the upper level call, complete the placement for all rows, a valid solution founds
    if n == len(board):
        print("valid placement for all queens")
        return 1

    count = 0
    for col in range(n):
        # place one one column, check whether it is valid, if yes update count
        board.append(col)
        print("append:", board)
        if is_valid(board):
            print("recursive call")
            count += n_queens(n, board)
            print("count", count)
        # prune the branch if it is invalid    
        board.pop()
        print("no valid, pop off", board)
    # return to the call function
    return count

# function to check whether the board is valid
def is_valid(board):
    # evaluate the latest row, the last element of board array stores the column info of the queen we are evaluating
    current_queen_row, current_queen_col = len(board) - 1, board[-1]

    for row, col in enumerate(board[:-1]):
        # check column difference with every placed queen, make sure no two queens in the same column
        diff = abs(current_queen_col - col)
        # diff == current_queen_row - row eliminates cases where two queens are in diagonal 
        if diff == 0 or diff == current_queen_row - row:
            return False

    return True

if __name__ == "__main__":
    print(n_queens(4))