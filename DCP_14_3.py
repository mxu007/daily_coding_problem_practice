# Count Android unlock combination
# One way to unlock an Android phone is by swiping in a specific pattern acroos 1-9 keypad

# For a pattern to be valid, it must satisify the following criteria:
# all of its keys mustant by distinct -- no repeated numbers
# it must not connect two keys by jumping over a third key, unless that key has already be used

# 1  2  3
# 4  5  6
# 7  8  9

# e.g. 4-2-1-7 is a valid pattern, wheras 2-1-7 is not

# Find total number of valid unlock patterns of length n, where 1 <= n <= 9

# no restriction on jumping over keys

# each time visit a number, we mark it as visited, traverse al paths starting with that numbers, and then remove it rom the visited set. Keep a running count of the number of paths seen thus far
# current is the current number we are evaluating whether it is on the path
# O(n!) time complexity, each recursive call we reduce the size by 1 only
# n * (n-1) * (n-2) * (n-3)... * 1
def num_paths(current, visited, n):
    # single element unlock path
    if n == 1:
        return 1

    path = 0
    for number in range(1,10):
        if number not in visited:
            visited.add(number)
            # decrement n as we have add number into the path
            path += num_paths(current, visited, n-1)
            visited.remove(number)
    
    return path

def unlock_combinations(n):
    return 4 * num_paths(1, set([1]),n) + 4 * num_paths(2, set([2]),n) + num_paths(5, set([5]),n)



# account for jumps, use a dictionary mapping pairs of keys to the key they skip over. Before visiting a number, we check to see that either the current and next number do not exist as a pair in this dictionary, or that their values have already been visited
# because symmetry of the keypad, the number of patterns starting from 1 is the same as number of patterns starting from 3, 7, 9. E.g. 1-6-3-8 can be rotated 180 degrees to get 9-4-7-2
# similarly, paths starting with 2,4,6,8 are all rotationally symmetric
# answer can be expressed as 4 * num_paths(1) + 4 * num_paths(2) + 1 * num_paths(5)

# simiar complexity to the simpler case where there is no restriction on jump
# O(n!) time complexity
def num_paths_1(current, jumps, visited, n):
    if n == 1:
        return 1
    
    path = 0
    for number in range(1,10):
        # make sure this new number we are evaluating is not in the path before
        if number not in visited:
            # current,number pair/link not in the jumps defined in the jump dictionary
            # or the number such pair jumps one, e.g. (1,3) jumps on 2, check whether 2 has been visited
            # this ties back to the condition "it must not connect two keys by jumping over a third key, unless that key has already be used"
            if (current, number) not in jumps or jumps[(current,number)] in visited:
                visited.add(number)
                path += num_paths_1(number, jumps, visited, n-1)
                visited.remove(number)
    
    return path

def unlock_combinations_1(n):
    jumps = {(1,3):2, (1,7):4, (1,9):5,
            (2,8):5,
            (3,1):2, (3,7):5, (3,9):6,
            (4,6):5, (6,4):5,
            (7,1):4, (7,3):5, (7,9):8,
            (8,2):5, 
            (9,1):5, (9,3):6, (9,7):8}
    
    return 4 * num_paths_1(1,jumps, set([1]),n) + 4 * num_paths_1(2,jumps, set([2]),n) + num_paths_1(5,jumps, set([5]),n)


if __name__ == "__main__":
    visited = set()
    print(unlock_combinations(2))
    print("---------------------")
    print(unlock_combinations_1(2))