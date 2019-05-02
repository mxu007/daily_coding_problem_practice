# Given a linked list, rearrange the node values such that they appear in alteranting low --> high --> low --> high --> form

# Example, Input: 1 --> 2 --> 3 --> 4 --> 5
# Output: 1 --> 3 --> 2 --> 5 --> 4

class Node:
    def __init__(self,data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
    
    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next

# O(N) time complxity, O(1) space
# based on odd or even index
# odd index number has to be smaller than neighboring even index number
# so for odd index number, if it is greater than the right-neiboring number, swap
# so for even index number, if it is smaller than the right-neightboring number, swap
# starting from the head, always perform the check with neightbor on the right (next)
def alternate_high_low(node):
    head = node
    counter = 1
    while node.next is not None:
        if (node.data > node.next.data and counter % 2 == 1) or (node.data < node.next.data and counter % 2 == 0) :
            temp = node.data
            node.data = node.next.data
            node.next.data = temp       

        node = node.next
        counter += 1
    return head

# save the use of temp
def alternate_high_low_2(node):
    head = node
    counter = 1
    while node.next is not None:
        if (node.data > node.next.data and counter % 2 == 1) or (node.data < node.next.data and counter % 2 == 0) :
            node.data, node.next.data = node.next.data, node.data
        node = node.next
        counter += 1
    return head

# instead of using a counter to track even or odd, we use two pointers left and right to track
# left has to be smaller than right, right has to be greater than right.next
# O(N) time and O(1) space
def alternate_high_low_3(node):
    head = node
    left, right = node, node.next
    while right:
        if left.data > right.data:
            left.data, right.data = right.data, left.data

        # break, reached the tail of the linked list
        if right.next is None:
            break
        
        if right.data < right.next.data:
            right.data, right.next.data = right.next.data, right.data

        # need to move two indices, otherwise it revert to original linked list
        left = right.next
        right = right.next.next

    return head
        

if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)

    llist.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    llist.printList()
    
    print("Output")
    alternated_llist = LinkedList()
    alternated_llist.head = alternate_high_low(llist.head)
    alternated_llist.printList()

    print("Output")
    alternated_llist = LinkedList()
    alternated_llist.head = alternate_high_low_2(llist.head)
    alternated_llist.printList()

    print("Output")
    alternated_llist = LinkedList()
    alternated_llist.head = alternate_high_low_3(llist.head)
    alternated_llist.printList()