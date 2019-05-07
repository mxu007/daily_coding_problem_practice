# Reconstruct array using +/- signs
# The sequence [0, 1, ..., N] has been jumbled, and the lonly clue you have for this order is an array representing whether each nmber is larger or smaler than the last. Given this information, reconstruct an array that is consistent with it.

# E.g. Input: [None, +, +, -, +]
# Output: [0, 1, 3, 2, 4]

# E.g. Input: [None, +. -. -. -]
# Output: [0, 1, 4, 3, 2]


# O(N) time and O(N) space
# total number of items pop off from the stack is bounded by the size of the array
def reconstruct_array(lst):
    ans = []
    stack = []

    # iterate through the whole list, if observing a minus sign next, current index gonna push into stack
    # as candidate for reverse, e.g. the negative sign (corresponding to 2) needs to be added into the stack
    for i in range(len(lst)-1):
        if lst[i+1] == '-':
            stack.append(i)
        # if next sign is + sign, just append current index/value into answer list
        # + sign after sequences of - signs means the boundary/end of out-of-sequence numbers
        # so we pop all numbers in the stack with LIFO to reverse the orders
        else:
            ans.append(i)
            while stack:
                ans.append(stack.pop())
    
    # append the last element
    stack.append(len(lst)-1)
    # pop all remaining numbers in the stack
    while stack:
        ans.append(stack.pop())
    
    return ans



if __name__ == "__main__":

    #lst = [None, "+", "+", "-", "+"]
    lst = [None, "+", "-", "-", "-", "+"]
    print(reconstruct_array(lst))

    