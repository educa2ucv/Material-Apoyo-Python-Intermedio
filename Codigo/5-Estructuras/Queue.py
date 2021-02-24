class Queue: 

    def __init__(self):
        self.queue = []
    
    def add(self,data):
        if not data in self.queue:
            self.queue.insert(0,data)
            return True
        else:
            return False
    
    def remove(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        else:
            return False
    
    def printQueue(self):
        print(self.queue)


example = Queue()
example.add(1)
example.add(4)
example.add(9)
example.add(10)
example.add(11)
example.add(12)
example.add(100)
example.remove()
example.remove()
example.remove()
example.printQueue()