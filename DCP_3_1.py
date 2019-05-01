# Given the head of a singly linked list, reverse it inplace

# __init__ is a special Python method that is automatically called when memory is allocated for a new object. The sole purpose of __init__ is to initialize the values of instance members for the new object. Using __init__ to return a value implies that a program is using __init__ to do something other than initialize the object. This logic should be moved to another instance method and called by the program later, after initialization.

# Linked Lists
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next

# The recursive make N recursive call and reduces to linked list with last two elements
# it then reverse the last two elements and returns to the upper call stack
# O(N) time, call from the head to the tail, and return to the call stack from tail back to ead to finish inplace reverse
# O(N) space because of each recursive call adds to call stack
def reverse(node):
    # recursive base case, no element
    if node is None:
        return None, None
    
    # recursive base case, one element
    if node.next is None:
        return node, node
    
    # head, tail stores the reversed head and tail of node.next
    # we just need to append node to the new tail
    # now the node becomes the new tail so we return it
    head, tail = reverse(node.next)
    node.next = None
    tail.next = node

    return head, node

# https://www.geeksforgeeks.org/reverse-a-linked-list/
# three pointers moves together to rebuild the two links between 3 elements
# init prev (left), curr(right) pointers pointing to Null and node respectively
# move get the next element of node
# curr.next becomes the prev element, reverse the second connection

# This is the iterative appraoch rather than recursive call
# O(N) time complexity and O(1) space since we only needs nxt, curr and prev pointers
def reverse_2(node):
    prev, curr = None, node
    while curr is not None:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    # shall return prev rather than curr coz curr will be None due to the while loop
    return prev


if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second
    second.next = third
    llist.printList() 

    reversed_llist = LinkedList()
    reversed_llist.head, _ = reverse(llist.head)
    reversed_llist.printList()

    print("Done")

    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second
    second.next = third
    llist.printList() 

    reversed_llist_2 = LinkedList()
    reversed_llist_2.head = reverse_2(llist.head)
    reversed_llist_2.printList()


