class Stack():
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]

class Queue():
    def __init__(self):
        self.items = []
    
    def dequeue(self):
        item, self.items = self.items[0], self.items[1:]
        return item
    
    def enqueue(self, item):
        self.items.append(item)
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)


