# Generate regular numbers
# A regular number in mathematics is defined as one which evenly divies some power of 60. Equivalently, we can say that a regular number is one whose only prime divisors are 2,3, and 5

# Given an integer n, write a program that generates, in order ,the first n regular numbers

# O(n^3) time for constructing the solutions set
# O(n^3log(n)) for the sorted function
def regular_nums(n):
    twos = [2 ** i for i in range(n)]
    threes = [3 ** i for i in range(n)]
    fives = [5 ** i for i in range(n)]

    solutions = set()

    for two in twos:
        for three in threes:
            for five in fives:
                solutions.add(two * three * five)
    
    return sorted(solutions)[:n]

# track the smallest N multiples, use heap
# for a regular number , it must be 2x, 3x or 5x of some other regular number
# start with a min heap with value 1, each time pop a value x from the heap, then push 2x, 3x and 5x onto the heap. We can continue the process until we have generate N integers
# number 6 will be pushe to the heap twice, once for being a multiple of two and once for being a multiple of three. To avoid duplicate. and only process a value if it is greater than this variable
import heapq
# each heappop and heappush takes O(log(n)) time where n is no.of elements 
# overal time complexity of (nlog(n))
def regular_nums_1(n):
    solutions = [1]
    last, count = 0, 0

    while count < n:
        x = heapq.heappop(solutions)
        if x > last:
            # https://www.geeksforgeeks.org/use-yield-keyword-instead-return-keyword-python/
            yield x
            last = x
            count += 1
            heapq.heappush(solutions, 2*x)
            heapq.heappush(solutions, 3*x)
            heapq.heappush(solutions, 5*x)

import time
if __name__ == "__main__":
    n = 100
    
    start = time.time()
    print(list(regular_nums_1(n)))
    print(time.time()-start)
    
    print("----------------------")
    
    start = time.time()
    print(regular_nums(n))
    print(time.time()-start)