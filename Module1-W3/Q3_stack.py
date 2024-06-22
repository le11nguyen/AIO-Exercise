class MyStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.capacity

    def push(self, value):
        if self.is_full == True:
            print("Stack is full, can't push more")
        return self.stack.append(value)

    def pop(self):
        if self.is_empty == True:
            print("There is nothing to pop")
        return self.stack.pop()

    def top(self):
        if self.is_empty == True:
            print("There is nothing in stack")
        return self.stack[-1]


# Example
stack1 = MyStack(capacity=5)

stack1.push(1)
stack1.push(2)

print(stack1.is_full())

print(stack1.top())
print(stack1.pop())
print(stack1.top())
print(stack1.pop())

print(stack1.is_empty())
