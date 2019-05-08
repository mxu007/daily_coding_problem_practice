# A unival tree (universal value) is a tree where all nodes under it have the same value

# Given the root to a binary tree, count the number of unival subtrees
# Note that single node can be counted as a unival tree

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        

# unival_helper takes O(N) time, where N is no.of nodes
# unival_helper function check whether root and its left/right subtrees form a unival tree
def unival_helper(root, val):
    # empty tree is a unival tree
    if root is None:
        return True
    # check if the root equal to val and the two subtrees are unival with the same val
    if root.val == val:
        return unival_helper(root.left,val) and unival_helper(root.right,val)

    return False

# count_unival_subtrees O(N) times, each time call unival_helper
# overall O(N^2) time complexity
def count_unival_subtrees(root):
    if root is None:
        return 0
    left = count_unival_subtrees(root.left)
    right = count_unival_subtrees(root.right)

    return 1 + left + right if unival_helper(root,root.val) else left + right


# improved more efficient solutions, O(N) time complexity, worst case just visit each node once
# kind of merge the unival_helper and count_unival_subtrees functions above
def count_unival_subtrees_2(root):
    count, _ = helper(root)
    return count

def helper(root):
    # empty node is a unival tree
    if root is None:
        return 0, True
    
    # top-down approach, get the sum of unival trees from left/right children 
    left_count, is_left_unival = helper(root.left)
    right_count, is_right_unival = helper(root.right)
    total_count = left_count + right_count

    if is_left_unival and is_right_unival:
        # check left subtree
        if root.left is not None and root.val != root.left.val:
            return total_count, False
        # check right subtree
        if root.right is not None and root.val != root.right.val:
            return total_count, False
        # checks passed, the left subtree, right subtree and root have the same value, it is an additional unival tree with the current root
        return total_count + 1 , True

    return total_count, False



if __name__ == "__main__":
    node_1 = Node(0)
    node_2 = Node(1)
    node_3 = Node(0)
    node_4 = Node(1)
    node_5 = Node(0)
    node_6 = Node(1)
    node_7 = Node(1)
    
    node_1.left, node_1.right = node_2, node_3
    node_3.left, node_3.right = node_4, node_5
    node_4.left, node_4.right = node_6, node_7

    print(count_unival_subtrees(node_1))

    print(count_unival_subtrees_2(node_1))
        




