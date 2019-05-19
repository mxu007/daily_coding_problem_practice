# Play Nim
# The game of nim, starting with tree heaps, each containing a variable number of items, two players take turns removing one or more items from a single pile, the player who eventually is forced to take the last stone loses

# take ONE or more stone but from SINGLE pile, have to take at least one

# Given a list of non-zero starting values [a,b,c, and assuming optimal play, determine whether the first player has forced win

# minimax is a recursive algorithm that involves evaluting all possible opponent moves and choosing the one that minimizes the maximum value the opponent can receive.
# the value of a given move to player one is equivalent to the value of the best response to player two

# list of possible moves can be generated by taking between one and all items from each pile. 
# recursive algorithm that enumerates all possible moves, and return True if any of them prevent the opponent from making an optimal move

# update the number of items in a single move
def update(heaps, pile, items):
    # reason to change to list is because tuple is not mutable
    heaps = list(heaps)
    heaps[pile] -= items
    return tuple(heaps)

# exhaust all moves based on available items in each pile
def get_moves(heaps):
    moves = []
    for pile, count in enumerate(heaps):
        for i in range(1, count+1):
            moves.append(update(heaps, pile, i))
            #print(moves)
    
    # we only want unique set of moves, so return with set 
    return set(moves)

# recursive calls to getting moves, reduce to smaller problems and check whether able to reach to (0,0,0) which is a win
# O(n!) as each recursive call only brings down the size of 1 (in the get_moves inner for loop i)
def nim(heaps):
    # return True if any of heaps prevent the opponent from making an optimal move
    if heaps == (0,0,0):
        return True
    
    # get possible moves 
    moves = get_moves(heaps)
    #print(moves, len(moves))
    #print("recursive call to nim")
    # reduce the problem size
    return any([nim(move)!= True for move in moves])


# bitwise solution, losing state (0,0,0) has an XOR/nim-sum product of 0
# for any given state, it is possible a move turn this xor product from zero to non-zero and vice versa. Therefore we  can use the nim-sum after each pair of moves as an invariant
# nim-sum ==0 meaning the losing state
# this is the math approach, O(1) time only
def nim_1(heaps):
    a, b, c = heaps
    if a == b == c == 1:
        return False

    # XOR product / nim-sum
    return a ^ b ^ c != 0

if __name__ == "__main__":
    heaps = [1,1,1]
    print(nim(heaps))
    print(nim_1(heaps))