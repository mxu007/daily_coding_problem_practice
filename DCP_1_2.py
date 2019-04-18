# Given an array of integers that are out of order, dtermine the bounds of the smallest window that must be sorted in order for the entire array to be sorted.

# Example Input: [3,7,5,6,9], Sorted Input: [3,5,6,7,9]
# Output: (1,3)

# Example Input: [1,5,2,3,8,6,7,9]
# Output: (1, 6)

# use python built-in sort function, then just loop through to trace left,right index where values are different to the sorted list
# O(NlogN) time complexity -- from the python sorted function
# O(NlogN) space complexity -- from the copied and sorted array/list
def smallest_window_to_sort_1(nums):
    # use sorted for copy of sorted nums
    sorted_nums = sorted(nums)
    left, right = None, None
    for i in range(len(nums)):
        if nums[i] != sorted_nums[i]:
            if left is None:
                left = i
            right = i
    
    return left,right


# loop from left to right, compare running max with current value, if current value smaller than running max, update right flag
# loop from right to left, compare running min with current value, if currentv value is greater than running small, update left flag
# 2-pass O(N) time, O(1) space
def smallest_window_to_sort_2(nums):
    left, right = None, None
    running_max, running_min = nums[0], nums[-1]
    for i in range(1,len(nums)):
        if nums[i] < running_max:
            right = i
        
        running_max = nums[i] if nums[i] > running_max else running_max

    for j in range(len(nums)-1,-1,-1):
        if nums[j] > running_min:
            left = j
        
        running_min = nums[j] if nums[j] < running_min else running_min
    
    return left,right


# solution from the book
def smallest_window_to_sort_3(array):
    left, right = None, None
    n = len(array)
    max_seen, min_seen = -float("inf"), float("inf")

    for i in range(n):
        max_seen = max(max_seen, array[i])
        if array[i] < max_seen:
            right = i
    
    for i in range(n-1, -1, -1):
        min_seen = min(min_seen,array[i])
        if array[i] > min_seen:
            left = i
    
    return left,right
