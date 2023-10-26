class Stack():
    def __init__(self):
        self.stack = []
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()            
        else:
            raise IndexError("Cnnot pop from empty stack")  
    
    def push(self, *items):
        for item in items:
            self.stack.append(item)
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("Cnnot peek from empty stack")  
        
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
if __name__ == "__main__":
    s = Stack()
    
    print(f"Size {s.size()}")
    values_to_push = list(range(0, 10))
    s.push(*values_to_push)
    
    print(f"Size {s.size()}")
    print(f"Last element {s.peek()}")
    print(f"Pop {s.pop()}")
    print(f"Size {s.size()}")
    
    