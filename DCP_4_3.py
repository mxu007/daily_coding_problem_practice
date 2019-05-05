# Given an array of integers and a number k, where 1 <= k <= array length, computes the maximum values of each subarray of length k

# Example, Input: [10, 5, 2, 7, 8, 7] and k = 3
# Output [10, 7, 8, 8]

# subarrays max(10,5,2) = 10
# max(5,2,7) = 7
# max(2,7,8) = 8
# max(7,8,7) = 8

# Do this in O(N) time and O(k) space, you can modify the input arrray in-place and you do not need to store the results
# You can simply print them out as you compute them


# simplest solution
# O(mk) time complexity, as we iterate all possible continuou subarray, which is O(m)
# the max operation takes O(k) each time, so O(mk) time complexity
def subarray_max(lst, k):
    for i in range(0, len(lst)-k+1):
        print (max(lst[i:i+k]))

#  Single pass without using the max function
# O(m) time and O(k) space
from collections import deque
def subarray_max_2(lst,k):
    q = deque()
    for i in range(k):
        while q and lst[i] >= lst[q[-1]]:
            q.pop()
        q.append(i)

    for i in range(k,len(lst)):
        print(lst[q[0]])
        while q and q[0] <= i -k:
            q.popleft()
        while q and lst[i] >= lst[q[-1]]:
            q.pop()
        q.append(i)
    
    print(lst[q[0]])

if __name__ == '__main__':
    lst = [10, 5, 2, 7, 8, 7]
    k = 3

    subarray_max(lst,k)
    subarray_max_2(lst,k)

