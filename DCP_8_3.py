# Find maximum XOR of element pairs
# Given an array of integers, find the maximum XOR of any two elements

# simple brute-force solution, O(n^2) time complexity where n is no.of elements in the list
import sys
def max_xor(lst):
    #print(lst)
    max_result = 0
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            #print(lst[i] ^ lst[j])
            max_result = lst[i] ^ lst[j] if lst[i] ^ lst[j] > max_result else max_result

    return max_result


class Trie:
    # size is defined as no.of maximum no.of bits
    def __init__(self,k):
        self._trie = {}
        self.size = k
    
    # O(k) time complexity for insert since it iterates through all the bits of a specific list element
    def insert(self,item):
        trie = self._trie

        for i in range(self.size, -1, -1):
            # extract the bit from left to right and construct the list
            bit = bool(item & (1 << i))
            if bit not in trie:
                trie[bit] = {}
            trie = trie[bit]

    # O(k) time complexity, compare a specific element with all element of lists represented in the trie
    def find_max_xor(self,item):
        trie = self._trie
        xor = 0
        for i in range(self.size, -1, -1):
            bit = bool(item & (1 << i))
            if (1-bit) in trie:
                # OR operation and set the specific bit to be one if (1-bit) is in the tri
                xor |= (1 << i)
                # go further down the trie
                trie = trie[1-bit]
            else:
                trie = trie[bit]
        return xor

# O(nk) time complexity, where n is no.of elements in the list and k is no.of bits
# improvement over O(n^2) where typically n >> k
def max_xor_1(lst):
    # get the maximum no.of bits required, it decides the size parameter of trie
    k = max(lst).bit_length()
    trie = Trie(k)

    for item in lst:
        trie.insert(item)

    xor = 0
    for item in lst:
        xor = max(xor, trie.find_max_xor(item))
    
    return xor

def max_xor_2(lst):
    max_result = 0
    # iterate the bits from rightmost to left
    for i in range(32)[::-1]:
        max_result <<= 1
        # each number right shift i places, get the bits
        # prefixes is a set
        prefixes = {num >> i for num in lst}
        print(prefixes, max_result, max_result^1)
        # So actually this max_result^1^p test two things:
        # find the two elements in nums that constructs the previous answer
        # check this two elements have opposite bits at current position
        max_result += any(max_result^1 ^ p in prefixes for p in prefixes)
    return max_result


if __name__ == "__main__":
    lst = [3, 10, 5, 25, 2, 8]
    print(max_xor(lst))

    print(max_xor_1(lst))

    print(max_xor_2(lst))
