# Python 23

class Queue:
    
    def __init__(self):
        self.queue = []

    def enqueue(self,item):
        self.queue.append(item)

    def dequeue(self):
        if self.queue == []:
            print("Fila vazia")
        else:
            self.queue.pop(0)

    def is_empty(self):
        if self.queue == []:
            return True
        else:
            return False

    def peek(self):
        if self.queue == []:
            return "Fila vazia"
        else:
            return self.queue[0]
    
fila = Queue()
print(fila.peek())
fila.enqueue("China")
print(fila.is_empty())
print(fila.peek())
fila.enqueue("Brasil")
fila.enqueue("Etiópia")
fila.dequeue()
print(fila.peek())  
print(fila.queue)
