# max-heap: parent node's value is always greater than or equal to its child nodes
# min-heap: parent node's value is always smaller than or queal to its child nodes

# Whenever you are asked to find the top k or minimum k values, a heap should be the first thing that comes to mind. Heaps are closesly tied to the heapsort sorting algorithm, priority queue implementations and graph algorithms such as Dijkstra's algorithm

# insert(heap, x): add an element x to the heap, O(logn)
# delete-min(heap): remove the lowest node, O(logm)
# heapify(array): convert an array into a heap by repeated insertions, O(nlog(n))

# Python's heapq module.
# heapq is a binary heap, with O(log n) push and O(log n) pop
# heapq.heappush(heap,x)
# heapq.heapop(heap)
# heapq.heapify(array)