# pwimt

class Queue:

    def __init__(self):
        self.queue = []
        self.front = self.rear = -1
        self.max = 5
    
    def enqueue(self,item):
        if self.front == 0 and self.rear == self.max - 1:
            return "Fila cheia"
        elif self.front == self.rear + 1:
            pass
        else:
            if self.queue == []:
                self.front = 0
            self.rear += 1
            self.queue.insert(self.rear,item)

    def dequeue(self):
        if self.queue == []:
            return "Fila Vazia"
        else:
            self.front += 1

    def is_empty(self):
        if self.queue == []:
            return True
        else:
            return False
        
    def peek(self):
        if self.queue == []:
            return "Fila Vazia"
        else:
            return self.queue[self.front]
        