# Implement a max stck
# push(val): push val onto the stack
# pop: pop off and return the topmost element of the stack. If there are no elements in the stack, throw an error
# max: return the maximum value in the stack currently. If there are no elements in the stack, throw an error

# Each method should run in constant time
# stack -- most recent item examinzed is the most important, a stack is frequently a good choice. Feature in DFS, backtracking and syntax parsing

class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_val = float("-inf")

    def push(self, x):
        self.stack.append(x)
        self.max_val = x if x > self.max_val else self.max_val


    def pop(self):
        try:
            return self.stack.pop()
        except IndexError:
            print("Pop from empty stack")


    def peep(self):
        return self.stack[-1]

    def get_max(self):
        if len(self.stack) == 0:
            print("Max from empty stack")
        else:
            return self.max_val

    def print_stack(self):
        print(self.stack)


if __name__ == '__main__':
    print("MaxStack")
    stack_1 = MaxStack()
    stack_1.push(4)
    stack_1.push(2)
    print(stack_1.pop())
    print(stack_1.pop())
    print(stack_1.pop())
    stack_1.print_stack()

    stack_1.push(1)
    print(stack_1.peep())
    stack_1.print_stack()

    print(stack_1.get_max())
    stack_1.pop()
    stack_1.pop()
    print(stack_1.get_max())

