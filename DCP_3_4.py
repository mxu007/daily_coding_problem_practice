# Given two singly linked lists that intersect at some point, find the intersecting node. 
# Assume the lists are non-clyclical

# Example A = 3 --> 7 --> 8 --> 10
# B = 99 --> 1 --> 8 -->10
# Output: return node with value 8

# Do this is O(m+n) time where m and n are the lengths of the list and constant space

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

# O(m+n) time complexity, O(m) space, use a dictionary to store the data/value for one linked list
def find_intersection(node_0, node_1):
    ll_dict = {}
    while node_0:
        #print(node_0.data, ll_dict)
        if node_0 not in ll_dict:
            ll_dict[node_0] = node_0.data
        node_0 = node_0.next
    
    while node_1:
        if node_1 in ll_dict:
            return node_1
        node_1 = node_1.next
    return None


def get_length(node):
    length = 0
    while node:
        length += 1
        node = node.next
    
    return length


# take note on the definition of intersection. the intersection does not mean two linked lists have the same values on wards from a node
# but literally two linked lists share the same node with the same address
# that's why this offseting index approach works
# O(m+n) time to iterate the two linked list, O(1) space since only two pointers are used
def find_intersection_2(node_0, node_1):
    len_0, len_1 = get_length(node_0), get_length(node_1)
    ptr_0, ptr_1 = node_0, node_1

    #print(len_0, len_1)
    #print(ptr_0.data, ptr_1.data)
    if len_0 > len_1:
        for _ in range(len_0-len_1):
            ptr_0 = ptr_0.next
    elif len_1 > len_0:
        for _ in range(len_1-len_0):
            ptr_1 = ptr_1.next
    
    while ptr_0 != ptr_1:
        #print(ptr_0.data, ptr_1.data)
        ptr_0, ptr_1 = ptr_0.next, ptr_1.next
    
    return ptr_0



if __name__ == '__main__':
    llist_1 = LinkedList()
    llist_1.head = Node(3)
    second = Node(7)
    third = Node(8)
    fourth = Node(10)
    llist_1.head.next = second
    second.next = third
    third.next = fourth

    
    llist_2 = LinkedList()
    llist_2.head = Node(99)
    second = Node(1)
    # linked list intersect at 8
    # third = Node(8)
    # fourth = Node(10)
    llist_2.head.next = second
    second.next = third
    third.next = fourth


    if find_intersection(llist_1.head, llist_2.head) is not None:
        print(find_intersection(llist_1.head, llist_2.head).data)
    else:
        print("No intersection")

    # method 2
    print("Method 2")

    if find_intersection_2(llist_1.head, llist_2.head) is not None:
        print(find_intersection_2(llist_1.head, llist_2.head).data)
    else:
        print("No intersection")
