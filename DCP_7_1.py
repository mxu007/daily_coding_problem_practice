# Given a binary search tree, find the floor and ceiling a given integer. The floor is the highest element in the tree less than or equal to an integer
# while the ceiling is the lowest element in the tree greater than or equal to an integer

# The question is equivalently asking whether an element exists in a binary search tree
# If either value does not exist return None

# If value < node.data, we know the ceiling cannot be greater than node.data
# If value > node.data, we know the floor cannot be smaller than node.data

class Node:
    def __init__(self,data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def insert(self, x):
        if not self.root:
            self.root = Node(x)

        else:
            self._insert(x, self.root)
    
    def _insert(self, x, root):
        if x < root.data:
            if not root.left:
                root.left = Node(x)
            else:
                self._insert(x, root.left)

        else:
            if not root.right:
                root.right = Node(x)
            else:
                self._insert(x, root.right)
    
    def find(self, x):
        if not self.root:
            return False
        else:
            return self._find(x, self.root)
    
    def _find(self, x, root):
        if not root:
            return False
        elif x == root.data:
            return True
        elif x < root.data:
            return self._find(x, root.left)
        else:
            return self._find(x, root.right)

# O(h) time complexity where h is the height of the tree
def get_bounds(root, x, floor=None, ceiling=None):
    print(floor,ceiling)
    # finally no exact match
    if not root:
        return floor, ceiling
    
    print(root.data, floor,ceiling)

    # finally exact match, floor = ceiling = matched data
    if x == root.data:
        return x, x

    # If value < node.data, we know the ceiling cannot be greater than node.data
    elif x < root.data:
        return get_bounds(root.left, x, floor, root.data)
    # If value > node.data, we know the floor cannot be smaller than node.data
    else:
        return get_bounds(root.right, x, root.data, ceiling)


if __name__ == "__main__":
    BST_Tree = BST()
    BST_Tree.insert(10)
    BST_Tree.insert(4)
    BST_Tree.insert(3)
    BST_Tree.insert(1)
    BST_Tree.insert(6)
    BST_Tree.insert(8)
    BST_Tree.insert(11)

    print(get_bounds(BST_Tree.root, 10))
    print("__")
    print(get_bounds(BST_Tree.root, 3))
    print("__")
    print(get_bounds(BST_Tree.root, 2))
    print("__")
    print(get_bounds(BST_Tree.root, 13))


