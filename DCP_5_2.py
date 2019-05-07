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

def cut_wall(lst):
    wall_len = sum(lst[0])
    cuts = []
    for cut_len in range(1, wall_len):
        for height in range(0,len(lst)):
            cut = 
