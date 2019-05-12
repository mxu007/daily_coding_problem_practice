# Compute the running median of a sequence of numbers. That is given a stream of numbers, print out the median of the list so far after each new element

# E.g. Input: [2, 1, 5, 7, 2, 0, 5]
# Output:
# 2
# 1.5
# 2
# 3.5
# 2
# 2
# 2

# Heaps are binary trees for which every parent node has a value less than or equal to any of its children. 
# https://docs.python.org/3/library/heapq.html

# finding minimal and maximal values are great reasons to use heaps.
# a min-heap and a max-heap. keep all elements smaller than the median in the max-heap and all elements larger than the median in the min-heap. As long as we keep these heaps the same size, we can guarantee that the median is either the root of the min-heap or the max-heap

# O(nlog(n)) time where n is no.of elements as we iterate the input list of n elements
# for each heappush and heappop, it takes O(logn) time
# heapq is a binary heap, with O(log n) push and O(log n) pop

# the book has the error of assuming python has max-heap and min-heap implementation. 
# The API below differs from textbook heap algorithms in two aspects: (a) We use zero-based indexing. This makes the relationship between the index for a node and the indexes for its children slightly less obvious, but is more suitable since Python uses zero-based indexing. (b) Our pop method returns the smallest item, not the largest (called a “min heap” in textbooks; a “max heap” is more common in texts because of its suitability for in-place sorting).
# https://docs.python.org/3.7/library/heapq.html

# Hence to apply the logic disccused in the book, we have to revert the sign of numb when we push and pop to max_heap
# by reverting the sign, the smallest number returned through the heappop will be the larest element (essentially) the max heap

import heapq
def get_median(min_heap, max_heap):
    # median is the smallest element of min_heap, all children of median has value smaller or equal than median(root)
    # recall that heappop pops the smallest element from the heap
    # https://docs.python.org/2/library/heapq.html
    if len(min_heap) > len(max_heap):
        min_val = heapq.heappop(min_heap)
        heapq.heappush(min_heap, min_val)
        return min_val
    # median is the root of max_heap, all children of median has value larger or equal than median
    elif len(min_heap) < len(max_heap):
        max_val = heapq.heappop(max_heap)
        heapq.heappush(max_heap, max_val)
        return -max_val
    # equal length, take the mean of two roots of heaps
    else:
        min_val = heapq.heappop(min_heap)
        heapq.heappush(min_heap, min_val)
        max_val = heapq.heappop(max_heap)
        heapq.heappush(max_heap, max_val)
        return (min_val + (-max_val)) / 2

def add(num, min_heap, max_heap):
    # less than two elements have been added to either min_heap or max_heap
    # default goes to max_heap
    if len(min_heap) + len(max_heap) <= 1:
        heapq.heappush(max_heap,-num)
        return 
    
    # get current median
    median = get_median(min_heap, max_heap)
    
    # if the number is greater than median, push to min_heap, we want the smallest number of min_heap as the median (essentially the root of min heap)
    if num > median:
        heapq.heappush(min_heap, num)
    # else push to max_heap, we want the largest number of max_heap as median (essentially the root of max heap)
    else:
        heapq.heappush(max_heap, -num)

# balance the size of the two heaps
def rebalance(min_heap, max_heap):
    if len(min_heap) > len(max_heap) + 1:
        root = heapq.heappop(min_heap)
        heapq.heappush(max_heap, -root)
    elif len(max_heap) > len(min_heap) + 1:
        root = heapq.heappop(max_heap)
        heapq.heappush(min_heap, -root)

def running_median(lst):
    # init the heap, essentially init empty list
    # These two make it possible to view the heap as a regular Python list without surprises: heap[0] is the smallest item, and heap.sort() maintains the heap invariant!
    # To create a heap, use a list initialized to [], or you can transform a populated list into a heap via function heapify().
    min_heap = []
    max_heap = []
    for num in lst:
        add(num, min_heap, max_heap)
        rebalance(min_heap,max_heap)
        print(get_median(min_heap,max_heap))

if __name__ == "__main__":
    lst = [2, 1, 5, 7, 2, 0, 5]
    running_median(lst)