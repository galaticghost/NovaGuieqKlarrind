# eu odeio esse código

class Queue:

    def __init__(self,size):
        self.size = size

        self.queue = [None for i in range(size)]
        self.front = self.rear = -1

    # favor refazer esse código intero
    def enqueue(self,item):
        if self.front == self.rear - 1:
            print("Fila cheia")
        self.rear += 1
        if self.rear == self.size:
            self.rear = 0   
        if self.front == -1:
            self.front = 0
        self.queue[self.rear] = item
    
    #isso também
    def dequeue(self):
        if self.front == -1:
            print("Fila vazia")
        else:
            self.queue[self.front] = None
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front += 1
                if self.front == self.size:
                    self.front = 0
    
    def peek(self):
        if self.front == -1:
            return "Fila vazia"
        else:
            return self.queue[self.front]
    
    def is_empty(self):
        if self.front == -1:
            return True
        else:
            return False
        
    def is_full(self):
        if (self.front == self.rear + 1) :
            return True
        else:
            return False
        
queue = Queue(3)
queue.enqueue(1)
queue.enqueue(2)
print(queue.peek())
queue.enqueue(2)
print(queue.queue)
queue.dequeue()
print(queue.queue)
queue.enqueue(4)
