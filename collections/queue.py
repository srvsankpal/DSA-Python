class Queue:
    def __init__(self, head=None):
        self.storage = []
        if head!=None:
            self.storage.append(head)

    def enqueue(self, new_element):
        self.storage.append(new_element)

    def peek(self):
        try:
            return self.storage[0]
        except:
            raise

    def dequeue(self):
        try:
            return self.storage.pop(0)
        except:
            raise
