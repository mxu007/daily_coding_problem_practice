# Tree
# in-order : left, root, right
# pre-order: root, left, right
# post-order: left, right, root


class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
