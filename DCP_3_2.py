# represent an integer in a linked list format by having each node represent a digit in the number
# nodes are connected in the reverse order (from left to right)
# such that 54321 is represented by 1 --> 2 --> 3 --> 4 --> 5
# Given two linked list in this format, return their sum

# example, Input: 9 --> 9 
#                 5 --> 2
# Output:         4 --> 2 --> 1


# Linked Lists
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

# recursive call actually goes through the longer linked list of two inputs
# O(m+n) time complexity where m, n are the length of two linked list
# O(m+n) space for the new output linked list
def add(node_0, node_1, carry=0):
    #print(node_0, node_1, carry)
    # return None only if two input nodes are None and there is no carry
    if node_0 is None and node_1 is None and not carry:
        return None
    
    # sum data of two nodes with the carry
    node_0_val = node_0.data if node_0 else 0
    node_1_val = node_1.data if node_1 else 0
    sum_nodes = node_0_val + node_1_val + carry
    carry_next = 1 if sum_nodes >= 10 else 0
    print(node_0_val, node_1_val, sum_nodes, carry_next, sum_nodes%10)

    # to avoid None.next error
    node_0_next = node_0.next if node_0 else None
    node_1_next = node_1.next if node_1 else None

    return Node(sum_nodes%10, add(node_0_next, node_1_next, carry_next)) 

if __name__ == '__main__':
    # first input linked list: 9 --> 9 
    llist_0 = LinkedList()
    llist_0.head = Node(9)
    second = Node(9)
    llist_0.head.next = second

    # second input linked list: 5 --> 2
    llist_1 = LinkedList()
    llist_1.head = Node(5)
    second = Node(2)
    llist_1.head.next = second

    llist_0.printList()
    llist_1.printList()

    llist_result = LinkedList()
    llist_result.head = add(llist_0.head, llist_1.head)

    llist_result.printList()
    

# Sample outputs from the implementation

# Mings-MBP:Daily_Coding_Problem minghanxu$ python DCP_3_2.py
# 9
# 9
# 5
# 2
# 9 5 14 1 4
# 9 2 12 1 2
# 0 0 1 0 1
# 4
# 2
# 1