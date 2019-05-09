# Binary Search Tree (BST)

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


if __name__ == "__main__":
    BST_Tree = BST()
    BST_Tree.insert(10)
    BST_Tree.insert(4)
    BST_Tree.insert(3)
    BST_Tree.insert(1)
    BST_Tree.insert(6)
    BST_Tree.insert(8)
    BST_Tree.insert(11)

    print(BST_Tree.root.data)
    print(BST_Tree.root.left.data)
    print(BST_Tree.root.right.data)

    print(BST_Tree.find(5))
    print(BST_Tree.find(11))
    print(BST_Tree.find(12))

