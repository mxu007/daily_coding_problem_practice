# Given a sorted array, convert it into a height-balanced binary search tree
# As asked for a height-balanced tree, we have to pick the middle value in the sorted array to be the root


class Node:
    def __init__(self, data, left=None, right =None):
        self.data = data
        self.left = left
        self.right = right


# O(N) time and space where N is no.of elements in the list  
# As we have to make node for each element in the list
def make_BST(lst):
    if not lst:
        return None
    
    # python 3 integer division
    mid = len(lst) // 2
    root = Node(lst[mid])
    
    # recursive call
    root.left = make_BST(lst[0:mid])
    root.right = make_BST(lst[mid+1:])

    return root

if __name__ == "__main__":
    lst = [3,5,6,7,8,9,10]
    root = make_BST(lst)
    print(root.data, root.left.data, root.right.data, root.right.left.data)