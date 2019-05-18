# paiting house
# a builder is looking to build a row of n houses that can be of k different colors, he has a goal of minimizing cost while ensuring that no two neighboring hoseus have the same colors

# given a n by k matrix where the entry at the ith row the jth column represent the cost to build the ith houes with the jith color, return the minimum cost required to achieve this goal

# brute force, generate all possible combinations of houses and colors, filter out invalid ocmbination and keep track of the lowest cost O(n^k) time complexity

# dynamic programming approach: a matrix cache where entry[i][j] represents the minimum cost of pating house i the color j, as well as paiting every house before i (become a cumulative cost)

# O(n*k^2) time where n is no.of house and k is no.of colors
# outer look n times, inner loop k times, further k times for the min function call
# O(n*k) space, where it could optimzied as we only need to keep most recent two rows of costs
def build_houses(matrix):
    # no.of houses
    n = len(matrix)
    # no.of colors
    k = len(matrix[0])
    # base of solution matrix where we maintain
    solution_matrix = [[0]*k]

    # iterate hose
    for r, row in enumerate(matrix):
        row_cost = []
        # iterate color
        for c, val in enumerate(row):
            # the total cost till house c is the minimum of sum of all previous costs (before hosue c) plus the cost of using different color to paint house c
            # i != c ensure different colors for adjacent hoses
            # solution_matrix[r][i] stores total cost prior house r using color i
            row_cost.append(min(solution_matrix[r][i] for i in range(k) if i != c) + val)
        # append the cost for using different colors paiting hosue r
        solution_matrix.append(row_cost)

    return min(solution_matrix[-1])

# improved version to space the space
# O(k) space only
def build_houses_2(matrix):
    # no.of colors
    k = len(matrix[0])
    # base of solution matrix where we maintain
    solution_row = [0] * k

    # iterate hose
    for r, row in enumerate(matrix):
        new_row_cost = []
        # iterate color
        for c, val in enumerate(row):
            # the total cost till house c is the minimum of sum of all previous costs (before hosue c) plus the cost of using different color to paint house c
            # i != c ensure different colors for adjacent hoses
            # solution_matrix[r][i] stores total cost prior house r using color i
            new_row_cost.append(min(solution_matrix[r][i] for i in range(k) if i != c) + val)
        # append the cost for using different colors paiting hosue r
        solution_row = new_row_cost

    return min(solution_row)




