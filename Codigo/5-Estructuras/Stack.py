class Stack:

    def __init__(self):
        self.stack = []
    
    def add(self,data):
        if not data in self.stack:
            self.stack.append(data)
            return True
        else:
            return False

    def remove(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return False
            
    def printStack(self):
        return self.stack

example = Stack()
example.add(5)
example.add(2)
example.add(1)
print(example.remove())
print( example.printStack() )
example.add(10)
example.add(10)
example.add(11)
print( example.printStack() )