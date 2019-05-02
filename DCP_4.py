
# stack -- most recent item examinzed is the most important, a stack is frequently a good choice. Feature in DFS, backtracking and syntax parsing
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop()
    
    def peep(self):
        return self.stack[-1]
    
    def print_stack(self):
        print(self.stack)

from collections import deque

if __name__ == '__main__':
    print("Stack")
    stack_1 = Stack()
    stack_1.push(4)
    stack_1.push(2)
    print(stack_1.pop())
    stack_1.print_stack()

    stack_1.push(1)
    print(stack_1.peep())
    stack_1.print_stack()

    print("Queue")
    # queue -- order of the items you are dealing with needs to be preserved
    queue_1 = deque()
    queue_1.append(4)
    queue_1.append(5)
    queue_1.appendleft(6)

    print(queue_1)

    print(queue_1.popleft())
    print(queue_1)

    print(queue_1.pop())
    print(queue_1)

