# overlapping subproblems: there is a way to partition the problem into smaller modular components
# optimal substructure: modular components can be efficiently put together to obtain a solution

# in particular, such subproblem should only be solved once, after which the solution should be cached and reused whenever that state is reached again

# find number of ways to lay pennies (1) and nickels (5) in a line on a table such that they sum to a dollar
# f(n) = f(n-5) + f(n+1)


from collections import defaultdict

# top-down with memorization using recursive call
# O(S*n) where S is the amount and n is the denomination count, n=2 in this case
# O(S) space where S=100 in this case
def coin_ways(n, cache= defaultdict(int)):
    cache[0] = 1

    if n in cache:
        return cache[n]

    if n < 0:
        return 0
    
    cache[n] = coin_ways(n-1) + coin_ways(n-5)

    return cache[n]

# bottom-up, O(S) time where n is value where we want to sum up to
# O(S) space where used in the dictionary mapping
def coin_ways_1(n, cache= defaultdict(int)):
    cache[0] = 1
    for i in range(1, n+1):
        cache[i] = cache.get(i-1, 0) + cache.get(i-5, 0)

    return cache[n]


if __name__ == "__main__":
    print(coin_ways(100))
    print(coin_ways_1(100))