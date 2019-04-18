# Given an array of integers, return a new array where each element in the new array is the number of smaller elements to the right of that element in the original input

# For example, Input: [3,4,9,6,1]
# Output: [1,1,2,1,0]
# As for 3, there is only 1 element -- 1 that is smaller and on the right of 3
# As of 6, there are 2 elements -- 6 and 1 are smaller and on the right of 6

# brute-force, O(N^2) time complexity, O(N) space
def smaller_count_to_the_right(nums):
    result = []
    for i in range(len(nums)):
        count = 0
        for j in range(i+1,len(nums)):
            if nums[i] > nums[j]:
                count += 1
        
        result.append(count)

    return result

# book solution, use python bisect module
# O(NlogN) time complexity due to the sorting in bisect, O(N) space to store results
# bisect uses binary search, which has time complexity of O(NlogN) 
# https://docs.python.org/3/library/bisect.html
# https://stackoverflow.com/questions/12022249/what-is-the-complexity-of-bisect-algorithm
# requires loop from right to left -- why, because we are counting number of smaller element to the right
# by maintaining a list of visited element, we make such list sorted, everytime a new number, its insertion index is the number of elements that are smaller than it and on its right
# because we iterate from right to left, before return, we have to revert it back

def smaller_count_to_the_right_2(nums):
    import bisect
    result = []
    seen = []

    for num in reversed(nums):
        i = bisect.bisect_left(seen, num)
        result.append(i)
        bisect.insort_left(seen, num)
    
    #print(seen)
    #print(result)
    # reversed returns an iterator
    return list(reversed(result))
