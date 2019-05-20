# Eficiently sort a million integers
# Given an array of a million integers between zero and a billion, out of order, how would you sort it efficiently with respect to time and space
# 
# quicksort or merge sort would give us time complexity of O(nlogn). we could take advantage of the fact that input is bounded and only consists of integers to do even better
# radix sort
# 
# E.g. [4, 100, 54, 537, 2, 89]
# order by the ones' place
# [100, 2, 4, 54, 537, 89]
# then order by the tens' place
# [100, 2, 4, 537, 54, 89]
# then order by the hundreds' place
# [2,4,54,89,100, 537]
# if a given number doesn't have a tens' or hundreds' place, we assign that place value zero


# Each of these sorts is performed using counting sort 
# https://www.geeksforgeeks.org/counting-sort/
# counting_sort takes (m+n) time, where n is length of input and m is the number of buckets
# n >> m, so dominantly O(n)
def counting_sort(arr, digit, base=10):
    # counts stores the numbers as sublists based on current digit evaluating and the index allocated
    counts = [[] for _ in range(base)]

    # O(n) to iterate all numbers in arr
    for num in arr:
        # floor division
        # https://stackoverflow.com/questions/39644638/how-to-take-the-nth-digit-of-a-number-in-python
        d = (num // (base ** digit)) % base
        #print(num, d)
        # each digit associated with a list
        counts[d].append(num)
    print(counts)

    result = []
    # the extend will ignore the empty lists in counts
    # O(m) to extend each bucket
    for bucket in counts:
        result.extend(bucket)

    return result

# https://www.geeksforgeeks.org/radix-sort/
# Overall O(nk) where k is the number of digits the largest number has
def radix_sort(arr, digits):
    # build the digt from right to left -- ones, tens, hundreds...
    for digit in range(digits):
        print("digit, ", digit)
        arr = counting_sort(arr, digit)
        print(" ")
    return arr

if __name__ == "__main__":
    arr = [4, 100, 54, 55, 537, 2, 89]
    k = 7
    print(radix_sort(arr, k))