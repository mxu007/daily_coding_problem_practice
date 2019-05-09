# Given an integer n, construct all possible binary search trees with n nodes where all values from [1,...n] are used 

class Node:
    def __init__(self, data, left=None, right =None):
        self.data = data
        self.left = left
        self.right = right

# let the range of values that nodes in a tree can take be bounded by low and high
# O(N) to make single tree
# catalan numbers
# O(N) space and O(N*2^N) space
# https://www.geeksforgeeks.org/construct-all-possible-bsts-for-keys-1-to-n/

# The idea is to maintain a list of roots of all BSTs. Recursively construct all possible left and right subtrees. Create a tree for every pair of left and right subtree and add the tree to list. Below is detailed algorithm.

# due to the recursive nature of make_trees... many instance of list trees will be created
def make_trees(low,high):
    # trees is a list which stores the root of all BST trees
    trees = []

    if low > high:
        trees.append(None)
        return trees

    for i in range(low, high+1):
        # due to the bst properties. All left subtree has value smaller than current i
        # left is a list of tree roots belong to the left subtree of current i
        left = make_trees(low, i-1)
        
        # due to the bst properties. All right subtree has value greater than current i
        # right is a list of tree roots belong to the right subtree of current i
        right = make_trees(i+1,high)

        # create permutation of left and right subtrees
        # one possible left tree, one possible right tree and current i form a final tree
        # remember l and r are the possible roots for left subtrees and right subtrees of current i
        for l in left:
            for r in right:
                node = Node(i, left=l, right=r)
                trees.append(node)
    print(trees)
    return trees

# print out the tree
def preorder(root):
    result = []
    # preorder traversal: root-left-right
    if root:
        result.append(root.data)
        result += preorder(root.left)
        result += preorder(root.right)

    return result

def construct_trees(N):
    trees = make_trees(1,N)
    #print(trees)
    for tree in trees:
        print(preorder(tree))

if __name__ == "__main__":
    construct_trees(3)
