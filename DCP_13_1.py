# Number of ways to clib a staircase
# There exists a staircase with n steps which you can climb up either 1 or 2 steps at a time. 
# Given n, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

# E.g. Input, n=4, 
# Output: 5 unique ways
# 1, 1, 1, 1
# 2, 1, 1
# 1, 2, 1
# 1, 1, 2,
# 2, 2

# what if, instead of being able to climb 1 or 2 steps at a time, you could clibb any number from a set of positive integers X. For example, if X =1,3,5
# In the worst case the recursive tree of the algorithm has height of SS and the algorithm solves only S subproblems because it caches precalculated solutions in a table. Each subproblem is computed with nn iterations, one by coin denomination. Therefore there is O(S*n)O(S∗n) time complexity.


# f(n) = f(n-1) + f(n-2)
from collections import defaultdict

# top-down approach with memorization
# O(S) space where S is the target step
# O(S*n) where n is the number of possible steps taken at each iteration/increment
def staircase(n, cache = defaultdict(int)):
    cache[0] = 1
    
    if n in cache:
        return cache[n]

    elif n < 0:
        return 0
    
    else:
        return staircase(n-1,cache) + staircase(n-2, cache)

# bottom-up approach, O(S*n) time where S is the target steps, n is the number of possible steps taken at each iteration/increment
# O(S) space for the dictionary
def staircase_1(n, cache = defaultdict(int)):
    cache[0] = 1
    for i in range(1, n+1):
        cache[i] = cache[i-1] + cache[i-2]
    return cache[n]

# top-down appraoch generalize to set X as posible steps taken at single increment
# repeat a lot of calculation
# O(S^n) time complexity
def staircase_2(n, X):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return sum(staircase_2(n-step, X) for step in X)

# O(S*n) time complexity as for each 1 increment of step, we need to query the cache dictionary n times
# O(S) space complexity
def staircase_3(n, X):
    cache = defaultdict(int)
    cache[0] = 1

    for i in range(1,n+1):
        cache[i] = sum(cache[i-step] for step in X if i-step >= 0)

    return cache


if __name__ == "__main__":
    print(staircase(4))
    print(staircase_1(4))
    print(staircase_2(4, [1,2]))
    print(staircase_3(4, [1,2]))


