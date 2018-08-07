import sys
class Stack():
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.isEmpty():
            print("Stack underflow exception")
            exit(1)
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)

class Queue():
    def __init__(self):
        self.items = []
    
    def dequeue(self):
        if self.isEmpty():
            print("Queue underflow exception")
            exit(1)
        item, self.items = self.items[0], self.items[1:]
        return item
    
    def enqueue(self, item):
        self.items.append(item)
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)


# Question 3.1
# Divide the array into 3 slots and modify the push, pop, peek methods to take in a specific stack requirement

# Question 3.2
# Create a variable inside the stack to hold the min that is initially set to MAXINT, then upon pushing you would compare
# the value you're pushing to the current min value
class StackMin():
    def __init__(self):
        self.items = []
        self.smallest = sys.maxint 

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        if item < self.smallest:
            self.smallest = item
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            print("Stack underflow exception")
            exit(1)
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def lowest(self):
        return self.smallest
# Question 3.3
class SetOfStacks():
    def __init__(self):
        self.stackSet = []
        self.stackSet.append(Stack())
        self.curIdx = 0
        self.limit = 10
        self.currentStack = self.stackSet[self.curIdx]

    def size(self):
        return len(self.currentStack)

    def isEmpty(self):
        return self.currentStack == [] or self.stackSet == []

    def push(self, item):
        if len(self.currentStack) == self.limit:
            self.stackSet.append(Stack())
            self.curIdx += 1
            self.currentStack = self.stackSet[self.curIdx]
        self.currentStack.append(item)

    def pop(self):
        if self.isEmpty() and self.curIdx == 0:
            print("Stack underflow exception")
            exit(1)
        elif self.isEmpty():
            self.stackSet = self.stackSet[:self.curIdx]
            self.curIdx -= 1
            self.currentStack = self.stackSet[self.curIdx]
        return self.currentStack.pop()

    def peek(self):
        return self.currentStack[len(self.currentStack)-1]

# Question 3.4
class QueueStack():
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def isEmpty(self):
        return self.stack1.isEmpty()
    
    def enqueue(self, item):
        self.stack1.push(item)
    
    def dequeue(self, item):
        if self.isEmpty():
            print("Underflow exception")
            exit(1)
        while not self.isEmpty():
            self.stack2.push(self.stack1.pop())
        value = self.stack2.pop
        while not self.stack2.isEmpty():
            self.stack1.push(self.stack2.pop())
        return value
    
    def size(self):
        return self.stack1.size()

# Question 3.5
def stackSort(stack):
    tempStack = Stack()
    while not stack.isEmpty():
        temp  = stack.pop()
        while not tempStack.isEmpty() and tempStack.peek() > temp:
            stack.push(tempStack.pop())
        tempStack.push(temp)
    return tempStack

def printStack(stack):
    while not stack.isEmpty():
        print(stack.pop())

stack = Stack()
stack.push(1)
stack.push(5)
stack.push(4)
stack.push(3)

sorted = stackSort(stack)
printStack(sorted)
