# Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of +, - * or /
# Given the root to such a tree, write a function to evaluate it

# E.g. Input:
#         *
#     +       +
#    3  2    4  5 

# Output, (3+2) * (4+5) = 45

# Need post-order traversal... why? cause we need to know the leaf nodes first them apply the arithematic operation based on the value of parents

class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


# O(N) time, worst-case scenario to visit all the nodes
def evaluate(root):
    if root.val == "*":
        return evaluate(root.left) * evaluate(root.right)
    elif root.val == "+":
        return evaluate(root.left) + evaluate(root.right)
    elif root.val == "-":
        return evaluate(root.left) - evaluate(root.right)

    elif root.val == "/":
        return evaluate(root.left) / evaluate(root.right)
    else:
        return root.val


if __name__ == "__main__":

    node_1 = Node('*')
    node_2 = Node('+')
    node_3 = Node('+')
    node_4 = Node(3)
    node_5 = Node(2)
    node_6 = Node(4)
    node_7 = Node(5)

    node_1.left, node_1.right = node_2, node_3
    node_2.left, node_2.right = node_4, node_5
    node_3.left, node_3.right = node_6, node_7

    print(evaluate(node_1))
