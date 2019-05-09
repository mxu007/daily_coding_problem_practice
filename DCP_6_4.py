# Given a binary tree, return the level of the tree that has the minimum sum. 
# The level of a node is defined as the number of connections required to get to the root. Which the root having level 0 

# E.g. Input
#     1
#   2    3
#       4  5 

# In the tree, level 0 has sum 1, level 1 has sum 5 and level 2 has sum 9, so the level with the minimum sum if 0

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from collections import defaultdict

# O(N) time complexity as the worst-case being traversing the entire tree
def smallest_level(root):
    queue = deque([])
    level_sum = defaultdict(int)

    queue.append((root,0))

    while queue:
        node, level = queue.popleft()
        level_sum[level] += node.val

        if node.left is not None:
            queue.append((node.left, level+1))
        if node.right is not None:
            queue.append((node.right, level+1))
    
    #return min(level_sum.values())
    # https://stackoverflow.com/questions/3282823/get-the-key-corresponding-to-the-minimum-value-within-a-dictionary
    return min(level_sum, key=level_sum.get)

if __name__ == "__main__":
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    node_5 = Node(5)

    node_1.left, node_1.right = node_2, node_3
    node_3.left, node_3.right = node_4, node_5

    print(smallest_level(node_1))