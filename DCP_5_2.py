# Cut the brick wall 
# A wall consistes of several rows of bricks of various integer lengths and uniform height.
# You goal is to find avertical line going from the top to the bottom of the wall that cuts through the fewest number of bricks. If athe line goes throught the edge between two bricks, this does not count as a cut

# E.g. Input: 
# [[3,5,1,1],
# [2,3,3,2],
# [5,5],
# [4,4,2],
# [1,3,3,3],
# [1,1,6,1,1]]

# Output: 2, draw a line after the eighth brick, which require cutting through the bricks in the third and fifth row

# use a dictionary to store the no.of cuts required for each possible length
# O(mn) time complexity where m is length of the wall and n is the total number of bricks
# O(m) space
from itertools import combinations
from collections import defaultdict
def cut_wall(lst):
    wall_len = sum(lst[0])
    cuts = defaultdict(int)
    for cut_len in range(1, wall_len):
        for height in range(0,len(lst)):
            widths = [sum(lst[height][0:i]) for i in range(1,len(lst[height]))]
            if cut_len not in widths:
                cuts[cut_len] += 1
    return min(cuts.values())

# improved version of the above solution
# do not need to test each possible length using the in command, but directly update the dictionary
# the maximum number of common cumulative length correspond to minimum number of cuts
# O(n) time where n is no.of bricks
# O(m) space for the list to store possible widths
def cut_wall_2(lst):
    cuts = defaultdict(int)
    for height in range(0,len(lst)):
        widths = [sum(lst[height][0:i]) for i in range(1,len(lst[height]))]
        for width in widths:
            cuts[width] +=1 
    return len(lst) - max(cuts.values())

# further optimization
def cut_wall_3(lst):
    cuts = defaultdict(int)
    for height in range(0,len(lst)):
        cum = 0
        for brick in lst[height][:-1]:
            cum += brick
            cuts[cum] +=1 
    return len(lst) - max(cuts.values())

if __name__ == "__main__":
    lst = [[3,5,1,1],
    [2,3,3,2],
    [5,5],
    [4,4,2],
    [1,3,3,3],
    [1,1,6,1,1]]

    print(cut_wall(lst))
    print(cut_wall_2(lst))
    print(cut_wall_3(lst))
