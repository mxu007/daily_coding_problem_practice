# solve sudoku
# the objective is to fill the grid subject to the constraint that every row, column and box (3x3 subgrid) must contain all of the digits from 0 to 9
# implement an fficient sudoku solver

# brute force take really long time, we need to try every permutation of the numbers 1-9 for all the non-empty squares

# can you construct a partial solution? -- yes, partial of the board
# can you verify if the partial solution is invalid -- check the board so far to make sure no rows, columns or squares that contain the same digit
# can you verify if the solution is complete -- solution is complete when board has been filled up

# try filling cell one by one and backtrack once we hit an invalid state
# need a function to check validity of current board: valid_so_far by checking all the rows, columns and sqauers

EMPTY = '.'
# is_complete function in worst case will be 
def sudoku(board):
    if is_complete(board):
        return board
    
    r, c = find_first_empty(board)

    for i in range(1,10):
        board[r][c] = str(i)
        if valid_so_far(board):
            result = sudoku(board)
            # 
            if is_complete(result):
                return result
        board[r][c] = EMPTY
    
    # return None
    return board

# no cell equals zero
def is_complete(board):
    return all(all(val is not EMPTY for val in row) for row in board)

def find_first_empty(board):
    for i, row in enumerate(board):
        for j, val in enumerate(row):
            if val == EMPTY:
                return i,j
    
    return False

def valid_so_far(board):
    if not rows_valid(board):
        return False

    if not cols_valid(board):
        return False

    if not blocks_valid(board):
        return False
    
    return True

def rows_valid(board):
    for row in board:
        if duplicates(row):
            return False

    return True

def cols_valid(board):
    for j in range(len(board[0])):
        if duplicates(board[i][j] for i in range(len(board))):
            return False
    return True

def blocks_valid(board):
    # shift windows on rows
    for i in range(0,9,3):
        # shift window on columns
        for j in range(0,9,3):
            # build block on-the-fly
            block = []
            for k in range(3):
                for l in range(3):
                    block.append(board[i+k][j+l])
                # check whether there is duplicate in the block
            if duplicates(block):
                return False
        
    return True

# use dictionary to track duplicate value
def duplicates(arr):
    c = {}
    for val in arr:
        if val in c and val is not EMPTY:
            return True
        c[val] = True
    return False


if __name__ == "__main__":
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

    print(sudoku(board))


                
