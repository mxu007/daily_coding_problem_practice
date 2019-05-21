# Given an array of integers where every integer occur three times except for one integer, which only occur once, find and return the non-duplicated integer

# E.g. Input: [6, 1, 3, 3, 3, 6, 6]
# Output: 1

# Input: [13, 19, 13, 13]
# Output: 19

# Do this in O(N) time and O(!) space

# O(N) time and O(N) space if using the dictionary to trac occurency

# we can find the unique number in an array of two duplicates by XORing all the numbers in the array. It cancels out all the bits that have even number of 1s, leaving only the unique odd bits out

# the idea is, for a specific bit, the sum of set bits for numbers that appear 3 times will have modulus 3 qeual 0
# for number that apprear once shall results in a bit to have modulus 3 equal 1
def find_unique(arr):
    result_arr = [0] * 32
    for num in arr:
        for i in range(32):
            bit = num >> i & 1
            result_arr[i] += bit
    
    result = 0

    for i, bit in enumerate(result_arr):
        if bit % 3 != 0:
            # reconstruct number from bits
            result += 2**i

    return result

if __name__ == "__main__":
    arr = [6, 1, 3, 3, 3, 6, 6]
    print(find_unique(arr))
    print("-----------------")
    
    arr = [13, 19, 13, 13]
    print(find_unique(arr))
