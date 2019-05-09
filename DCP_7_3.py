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
def make_trees(low,high):
    trees = []

    if low > high:
        trees.append(None)
        return trees

    for i in range(low, high+1):
        print("i:",i)
        left = make_trees(low, i-1)
        print("left:", left)
        right = make_trees(i+1,high)
        print("right:",right)

        for l in left:
            for r in right:
                node = Node(i, left=l, right=r)
                trees.append(node)
                print(l, r, len(trees))
    return trees


# print out the tree
def preorder(root):
    result = []

    if root:
        result.append(root.data)
        result += preorder(root.left)
        result += preorder(root.right)

    return result

def construct_trees(N):
    trees = make_trees(1,N)
    for tree in trees:
        print(preorder(tree))


if __name__ == "__main__":
    construct_trees(3)