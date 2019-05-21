# Compute the longest consecutive string of ones in binary
# Given an integer n, return the length of the longest consecutive run of ones in its binary representation

# E.g. Input: 156 -- 10011100 in binary, 
# Output: 3

# O(n) time complexity where n is no.of digits in the input
def find_length(n):
    # bin function returns the 0x... string representation
    n = bin(n)[2:]
    print(n)
    max_length = current_length = 0

    for bit in n:
        if bit == '1':
            current_length += 1
            max_length = max(current_length, max_length)
        else:
            current_length = 0

    return max_length

# if we perform the operations x & x << 1, the longest consecutive run of ones must decrease by one. This is because all but one of the set bits in the original number will correspond to the set bits in the shift number
# decrement one bit at a time, the longest consecutive ones will last the longest
def find_length_1(n):
    max_length = 0
    while n:
        n = n & (n <<1)
        max_length += 1
    
    return max_length


if __name__ == "__main__":
    print(find_length(156))
    print("---------------")
    print(find_length_1(156))