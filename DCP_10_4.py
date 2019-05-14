# best snakes and ladders
# 10x10 board, the goal of which is get from square 1 to square 100. On each turn players will roll a six-sided die and move forward a number of spaces equal to the result. If they land on square that represents a snake or ladder, they will be transported ahead or behind, respectively to a new square.

# Find the smallest number of turns it takes to play snakes and ladders
# 
# snakes = {17:13, 52:29, 57:40, 62:22, 88:18, 95:51, 97:79}
# ladders = {3:21, 8:30, 28:84, 58:77, 75:86, 80:100, 90:91}

# efficient method of using bfs
# maintain a queue of tuples representing the current square and the number of turns taken so far, starting with (0,0)
# For ech item popped from the que, we examine the moves that can be made from it. If a move crosses the finish line, we've found a solution. Otherwise, if a move takes us to a square we have not already visited, we add that square to the queue

# key point is that squares will only be put in the queue on the earliest turn they can be reached. number of turns asscoiated with each square will be minimal

# O(N) time and space where N is no.of squares in the grid
from collections import deque 
def minimum_turns(snakes, ladders):
    # map both snakes and ladders to single dicitonary
    board = {square: square for square in range(1,101)}
    for start, end in snakes.items():
        board[start] = end
    
    for start, end in ladders.items():
        board[start] = end

    start, end = 0, 100
    turns = 0

    # path stores the tuple of (current_square, no_of_turns_taken)
    path = deque([(start, turns)])
    visited = set()

    # dfs of using deque
    while path:
        square, turns = path.popleft()

        # roll dice for 1 to 6
        for move in range(square+1, square+7):
            if move >= end:
                print(path)
                return turns + 1
            
            # checking whether the square has been visited helps to ensure that each square will be checked once for the earliest arrival (with least no.of turns)
            if move not in visited:
                visited.add(move)
                # look up the mappings on potential snake and ladder
                path.append((board[move], turns+1))
                print(path, visited)

if __name__ == "__main__":
    snakes = {17:13, 52:29, 57:40, 62:22, 88:18, 95:51, 97:79}
    ladders = {3:21, 8:30, 28:84, 58:77, 75:86, 80:100, 90:91}
    print(minimum_turns(snakes, ladders))

