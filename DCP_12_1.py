# Tower of Hanoi
# Goal of the puzzle is to move all the disk from furst rod to the last rod while folloing the rules:
# you can only move one disk at a time
# a move consists of taking the uppermost disk from one of the stacks and placing it on top of another stack
# you cannot place a larger disk on top of a smaller disk

# 1st rod being 1, 2nd rod being 2, last rod (goal) being 3
# the goal of the tower of hanoi is to get all n disks from the source peg to the target peg, using a spare peg and abiding all constriants.
# why recursion? series of moves get closer to the solution. we can think of this sequence of states as subproblems to be solved

# 0 disk do nothing
# 1 disk, we move it directly from source peg to target peg

# if there is more than 1 disk
# recursively move n-1 disks from source stack to the spare stack
# move the last (biggest) disk from source stack to the target stack
# recursively move all n-1 disk from the spare stack to the target stack

# O(2^n) time, since each call we call ourselves twice, we recursively do n such call
# O(n) space for the call stack
def tower_of_hanoi(n, a='1', b='2', c='3'):
    if n >= 1:
        # recursively move n-1 disks from source stack to the spare stack
        tower_of_hanoi(n-1, a, c, b)
        print('move {} to {}'.format(a,c))
        # recursively move n-1 disks from spare stack to the target stack
        tower_of_hanoi(n-1,b, a, c)

if __name__ == "__main__":
    tower_of_hanoi(3)