# number of ways to decode a string
# given the mapping a=1, b=2, ... z=26, and an encoded msg, count the number of ways it can be decoded
# for example, "111" should be 3 since it can be decoded as "aaa", "ka" and "ak"

# assume the message are always decodable

# when the string is at least two digits, resursive/induction step
# the first letter is encoded alone
# the first two digits form a number k <= 26, and are encoded as a pair

# input digits as a string
# not efficient solution, repeatively compute a lot of the intermediate results
# every num_encodings incur additional 2 calls and we decrement by size 1 each time only
# O(2^n) time complexity and O(1) space
def num_encodings(s, total=0):
    # no letter starts with 0, no such mapping
    if s.startswith('0'):
        return 0

    # single combination for empty string or single digit string
    elif len(s) <= 1:
        return 1
    
    # first digit translate to single letter
    total += num_encodings(s[1:],total)
    # first two digits form a number k <= 26
    if int(s[:2]) <= 26:
        total += num_encodings(s[2:],total)

    return total

# start from base case and build up the solution. maintain a cache that stores the number of ways to encode any substring s[i:]
# for each index from n-1 down to 0, we compute the number of possible solutions tarting at that index and store the result to use in later calculation
# iterate from right to left
# O(n) time and space, iterate from right to left to build from base cases
# the dictionary takes O(n) space
from collections import defaultdict
def num_encodings_1(s):
    cache = defaultdict(int)
    cache[len(s)] = 1

    for i in reversed(range(len(s))):
        if s[i].startswith('0'):
            cache[i] = 0
        # last element from the list
        elif i == len(s)-1:
            cache[i] = 1
        else:
            # single digit mapped to single letter
            # e.g. cache["11"] = cache["1"]
            cache[i] += cache[i+1]
            # double digits mapped to single letter
            if int(s[i:i+2]) <= 26:
                cache[i] += cache[i+2]
        print(i, cache)
    return cache[0]

if __name__ == "__main__":
    s = "111"
    print(num_encodings(s))
    print("-------------------")
    print(num_encodings_1(s))
