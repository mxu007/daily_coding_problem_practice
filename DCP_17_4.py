# Find nth sevenish number
# Let's define a sevenish number to be one which is either a power of 7 or the sum of unique powers of 7
# The first few sevenish numbers are 1, 7, 8, 47 and so on
# Create an algorithm to find the nth sevenish number

# brute force, O(2^n) time and space where the totals keep getting join with possible x+p
def get_sevenish_numbers(n):
    # get powers of 7
    powers = [7 ** i for i in range(n)] # powers = [0, 7, 49...]
    totals = {0}

    for p in powers:
        # add elements from another set, make sure it is unique set
        # totals are not sorted
        totals |= {x+p for x in totals}
    # get total list of sevenish number up to 7^n
    return totals
# O(n) time to iterate i one by one
def nth_sevenish_numbers(n):
    # get the list of sevenish numbers
    sevenish_numbers = get_sevenish_numbers(n)
    print(sevenish_numbers)

    i = 1
    count, last_sevenish_numbers = 0, 0
    # get the n-th number by
    while count < n:
        # increment i by 1 each time, not very efficient
        if i in sevenish_numbers:
            count += 1
            last_sevenish_numbers = i
        i += 1

    return last_sevenish_numbers

# go through each bit of n, from least to most siginificant and check if it is set. If so we add 7th place to our total. Once we bitshift through the entire number, we can return the total
# imagine each bit represent power of 7 instead of power of 2
# nth sevenish number will be the nth binary number, transloated into powers of 7 instead of 2

# 001 -- 1 (n=1)
# 010 -- 1 * y^1 = 7 (n=2)
# 011 -- 1 * y&1 + 1 * y^0 (n=3)
# 100 -- 1 * 7^2 = 49 (n=4)
def nth_sevenish_numbers_1(n):
    ans = 0
    bit_place = 0

    while n:
        if n & 1:
            # the answer is a sevenish number so has to be incremented with powers of 7
            ans += 7 ** bit_place
        # perform shift on the binary to get the index (nth sevenish number)
        n >>= 1
        bit_place += 1

    return ans



if __name__ == "__main__":
    n = 4
    print(nth_sevenish_numbers(n))
    print("--------------------")
    print(nth_sevenish_numbers_1(n))