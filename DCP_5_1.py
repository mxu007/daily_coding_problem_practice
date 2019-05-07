# Implement an LRU (least Recently Used) cache. The cache should be able to be initialized with cache size n, and provide the following methods

# set(key,value): set key to value. If there are already n items in the cache and we are adding a new item, also remove the least recently used item
# get(key): get the value at key. If nosuch key exists, return null

class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

# Doubled Linked List
class LinkedList:
    def __init__(self):
        self.head = Node(None, "head")
        self.tail = Node(None, "tail")

        self.head.next = self.tail
        self.tail.prev = self.head

    def get_head(self):
        return self.head.next

    def get_tail(self):
        return self.tail.prev


    def add(self,node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def remove(self,node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

# all operation runs on O(1) TIME
class LRUCache:
    def __init__(self,n):
        self.n = n
        self.dict = {}
        self.list = LinkedList()

    def set(self,key,val):
        if key in self.dict:
            self.dict[key].delete()

        n = Node(key,val)
        self.list.add(n)
        self.dict[key] = n

        if len(self.dict) > self.n:
            head = self.list.get_head()
            self.list.remove(head)
            del self.dict[head.key]
    
    def get(self,key):
        if key in self.dict:
            n = self.dict[key]

            self.list.remove(n)
            self.list.add(n)

            return n.val


