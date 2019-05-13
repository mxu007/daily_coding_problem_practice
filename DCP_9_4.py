# Build a huffman tree
# Huffman coding is a method of encoding characters based on their frequence. Each letter is assigned a variable-length binary string such as 0101 or 111110, where shorter lengths  correspond to more common letters. To accomplish this, a binary tree is built such that path from the root to any leaf unqiuely maps to a character

# when traversing the path, descending to a left child corresponds to a 0 in the prefix, while descending right corresponds to 1

# each letter is represented with variable-length string, shorter length string means more commom


# Given a dictionary of character frequencie, build a huffman tree and use it to determine a mapping between characters and their encoded binary string


# regardless of how we build the tree, we would like each leaf node to represent a character
class Node:
    def __init__(self, char, left=None, right=None):
        self.char = char
        self.left = left
        self.right = right

# when building the tree, we would try to ensure that less frequent characters end up further aways from the root
# repeatedly pop the two least common letters, create a combined node and ush that node back onto the queue

import heapq
# reason of using heapq is the pop returns the smallest value
# heappop and heappush takes O(log(n)) time where n is no.of charactesr
def build_tree(frequencies):
    nodes = []
    for char, frequency in frequencies.items():
        heapq.heappush(nodes, (frequency, Node(char)))
    
    while len(nodes) > 1:
        f1, n1 = heapq.heappop(nodes)
        f2, n2 = heapq.heappop(nodes)
        # "*" means aggregated node
        node = Node('*', left = n1, right = n2)
        heapq.heappush(nodes, (f1+f2, node))

    root = nodes[0][1]
    return root


# create encoding
# O(log(n)) time to traverse the path where n is no.of characters
# O(mlog(n)) overall time complexity where m is length of string
def encode(root, string='', mapping ={}):
    if not root:
        return
    # leaf node
    if not root.left and not root.right:
        mapping[root.char] = string
    
    encode(root.left, string + '0', mapping)
    encode(root.right, string + '1', mapping)

    return mapping


if __name__ == "__main__":
    frequencies = {"a":3, "c":6, "e":8, "f":2}
    print(frequencies)
    root = build_tree(frequencies)
    print(encode(root))
