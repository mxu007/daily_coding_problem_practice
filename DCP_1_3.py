# Given an array of numbers, find the maximum sum of any contiguous subarray of the array

# Example Input [34, -50, 42, 14, -5, 86]
# Output 137
# 42 + 14 - 5 + 86 = 137

# brute force and no wrapping around is allowed
# O(N^3) time complexity due to the double-lay for loops, the sum function takes another O(N) time
# O(1) time complexity
def max_subarray_sum_1(nums):
    max_sum = 0
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            #print(nums[i:j+1], sum(nums[i:j+1]))
            max_sum = sum(nums[i:j+1]) if max_sum < sum(nums[i:j+1]) else max_sum

    return max_sum

# O(N) time, just iterate through the array onece
# like a dp approach
# two variables, max_so_far stores the global max, max_ending_here stores the contiguous sum till the current element
# Kadane’s algorithm
def max_subarray_sum_2(nums):
    max_so_far = 0
    max_ending_here = 0
    
    for i in range(len(nums)):
        max_ending_here = max_ending_here + nums[i]
        max_ending_here = 0 if max_ending_here < 0 else max_ending_here

        max_so_far = max_ending_here if max_ending_here > max_so_far else max_so_far
        
    return max_so_far

# When wrapping is allowed

# Example Input [8, -1, 3, 4]
# Output 15
# 3 + 4 + 8 = 15

# wrapping of contributing elements impleies non wrapping of non contributing elements.
# to maximize sum of wrapping circular array, we need to find the non-wrapping/contiguous subarray with the mininmum sum (or most negative)
# 3-pass, first pass computes maximum subarray sum, second pass reverse the sign of the input array, third pass computes smallest subarray sum by calling the same function with the reversed sign input array
# as after reversing the sign, finding the max subarray is equivalent as finding the min continous subarray
# then reverse back the sign of max subarray of the reversed input array and add to total sum of input array, this gives the largest sum of wrapping circular array
# compare non-wrapping max and wrapping max

def max_subarray_sum_3(nums):

    def max_subarray_sum_2(nums):
        max_so_far = 0
        max_ending_here = 0
        
        for i in range(len(nums)):
            max_ending_here = max_ending_here + nums[i]
            max_ending_here = 0 if max_ending_here < 0 else max_ending_here

            max_so_far = max_ending_here if max_ending_here > max_so_far else max_so_far
            
        return max_so_far

    reverse_nums = [-x for x in nums]

    print(max_subarray_sum_2(nums), max_subarray_sum_2(reverse_nums), sum(nums))
    return max(max_subarray_sum_2(nums), sum(nums) + max_subarray_sum_2(reverse_nums))


# solution from the book, max_subarray_sum and min_subarray_sum are essentially the same algo
# can be implemented as above
def maximum_circular_subarray(nums):
    max_subarray_sum_wraparound = sum(nums) - min_subarray_sum(nums)

    return max(max_subarray_sum(nums), max_subarray_sum_wraparound)

def max_subarray_sum(nums):
    max_ending_here, max_so_far = 0, 0

    for x in nums:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far

def min_subarray_sum(nums):
    min_ending_here, min_so_far = 0, 0 

    for x in nums:
        min_ending_here = min(x, min_ending_here+x)
        min_so_far = min(min_so_far, min_ending_here)

    return min_so_far
