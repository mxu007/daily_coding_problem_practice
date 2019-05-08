# Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree

# E.g. input pre-order: [a, b, d, e, c, f, g]
# in-order: [d, b, e, a, f, c, g]
# output:
#         a 
#     b       c
# d     e    f   g

# Recall this is a binary tree problem


class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
# bear in mind, a tree represented by preorder or inorder lists, the two lists must have same number of elements
def reconstruct(preorder, inorder):
    # base case
    # empty preorder/inorder list
    if len(preorder) == 0 or len(inorder) == 0:
        return None
    # single element
    # single-element preorder/inorder list
    if len(preorder) == 1 and len(inorder) == 1:
        return preorder[0]
    
    root = preorder[0]
    idx = inorder.index(root)

    root.left = reconstruct(preorder[1:idx+1], inorder[0:idx])
    root.right = reconstruct(preorder[idx+1:],inorder[idx+1:])

    return root

# https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
# https://stackoverflow.com/questions/49063499/inorder-traversal-of-tree-in-python-returning-a-list
def inorder_traversal(root):
    if root is None:
        return []
    
    left_lst = preorder_traversal(root.left)
    right_lst = preorder_traversal(root.right)
    return left_lst + [root] + right_lst

def preorder_traversal(root):
    if root is None:
        return []
    
    left_lst = preorder_traversal(root.left)
    right_lst = preorder_traversal(root.right)
    return [root] + left_lst + right_lst



if __name__ == "__main__":
    node_1 = Node('a')
    node_2 = Node('b')
    node_3 = Node('c')
    node_4 = Node('d')
    node_5 = Node('e')
    node_6 = Node('f')
    node_7 = Node('g')

    node_1.left, node_1.right = node_2, node_3
    node_2.left, node_2.right = node_4, node_5
    node_3.left, node_3.right = node_6, node_7


    print(preorder_traversal(node_1))

    preorder = preorder_traversal(node_1)
    inorder = inorder_traversal(node_1)

    print(preorder)
    print(inorder)

    root = reconstruct(preorder,inorder)
    print(root.val, root.left.val, root.right.val)


    