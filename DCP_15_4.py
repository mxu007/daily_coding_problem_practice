# Find minimum element in rotated sorted array
# A sorted array of integers has been rotated an unknown number of times
# Given this array, find the index of an element in the array in faster than linear time

# E.g. Input: [13, 18, 25, 2, 8, 10], element 8
# Output: 4
# assume all the integers in the array are unique

# We can find the rotation point using binary search. Initially, our low and high indices will be the start and end of array
# At each step we compare the midpoint of our array to the first element
# If the midpoint is larger, the pivot must come after it, we lset low to be the midpoint
# If the midpoint is smaller, the pivot must come before it, so we set high to be the midpoint
# With each iteration, we cut the search space in half to find the index at which the original list was rotated
# Once we have this rotation point, we can do binary search as usuall by remembering to offset by the correct amount

# first pivot search using binar search takes O(log(n)) time, second search after pivot located is also O(log(n)) time, hence overall time complexity is still O(log(n))
import math
def shifted_array_search(lst, num):
    # i is the pivot index we want to find
    i = len(lst) // 2
    # some error in the DCP book, need to use 
    dist = math.ceil(i/2)
    # after the while loop, i is the pivot point
    while True:
        #print("dist:", dist, ", i:", i)
        # if first element is greater than i-th element, and i-1 element greater than i-th element
        # then i is the pivot index
        if lst[0] > lst[i] and lst[i-1] > lst[i]:
            break
        # reduced the search window
        elif dist == 0:
            break
        # mid point is larger, the pivot must come after it, add to update the mid(i)
        elif lst[0] <= lst[i]:
            i = i + dist
        # i-th element is larger than i-1 element, meaning the pivot must before i, subtract to update i
        elif lst[i-1] <= lst[i]:
            i = i - dist
        else:
            break
        # reduce window
        dist = math.ceil(dist/2)

    #print("pivot index:", i, dist)
    
    # directly find the target
    if lst[i] == num:
        return i

    low, high = i, i -1
    dist = math.ceil(len(lst)/2)
    while True:
        # zero window zero, not able to find, return None
        if dist == 0:
            return None
        # the % len(lst) computes the offset index of mid point
        guess_ind = (low+dist) % len(lst)
        guess = lst[guess_ind]

        # match found
        if guess == num:
            return guess_ind
        # offset midpoint smaller than num, update low to mid point
        elif guess < num:
            low = guess_ind
        # offset midpoint is slaer than num, update high to mid point
        else:
            high = (len(lst) + high - dist) % len(lst)
        
        dist = math.ceil(dist/2)


# another more traidtional binary search implementation
def find_pivot(arr, low, high):
    if high < low:
        return -1
    if high == low:
        return low
    
    mid = (low+high) // 2
    # mid is the last element (largest element) in original sorted list
    if mid < high and arr[mid] > arr[mid+1]:
        return mid
    # mid-1 is the largest element in original sorted list
    if mid > low and arr[mid] < arr[mid-1]:
        return mid -1 
    # the pivot point is after low before mid
    if arr[low] >= arr[mid]:
        return find_pivot(arr,low, mid-1)
    # the pivot point is after mid before high
    return find_pivot(arr, mid+1, high)

def binary_search(arr, low, high, key):
    #print(low, high)
    if high < low:
        return -1

    mid = (low+high) // 2
    if arr[mid] == key:
        return mid
    # target after mid before high
    elif arr[mid] < key:
        return binary_search(arr, mid+1, high, key)
    # target before mid after low
    else:
        return binary_search(arr, low, mid-1, key)

def pivot_binary_search(arr,n,key):
    pivot = find_pivot(arr, 0, n-1)
    #print("pivot:", pivot)
    # no pivot found, means no rotation has been applied
    if pivot == -1:
        return binary_search(arr, 0, n-1, key)

    # pivot just to be the target
    if arr[pivot] == key:
        return pivot
    # target value after low before pivot
    if arr[0] <= key:
        return binary_search(arr,0,pivot-1, key)
    else:
        return binary_search(arr, pivot, n-1, key)


if __name__ == "__main__":
    lst = [13, 18, 25, 2, 8, 10]
    num = 8
    print(shifted_array_search(lst, num))
    print(pivot_binary_search(lst, len(lst), num))

    print("--------------------")
    lst = [25, 2, 8, 10, 13, 18]
    num = 8
    print(shifted_array_search(lst, num))
    print(pivot_binary_search(lst, len(lst), num))

    print("--------------------")
    lst = [25, 2, 8, 10, 13, 18]
    num = 25
    print(shifted_array_search(lst, num))
    print(pivot_binary_search(lst, len(lst), num))

    print("--------------------")
    lst = [8, 10, 13, 18, 25, 2]
    num = 2
    print(shifted_array_search(lst, num))
    print(pivot_binary_search(lst, len(lst), num))
