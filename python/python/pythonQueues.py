class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue:
    
    def __init__(self,length):
        self.head = None
        self.tail = None
        self.max_length = length
        
    def __str__(self):
        if self.is_empty():
            return f"The queue is empty"
        valores = []
        current = self.head
        while current:
            valores.append(str(current.value))
            current = current.next
        return " -> ".join(valores)
    
    def is_empty(self):
        return self.head is None
    
    def queue_length(self):
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        return length
    
    def enqueue(self,value,priority = None):
        node = Node(value)
        if self.queue_length() == self.max_length:
            print("The queue is full")
            return None
        
        if priority is not None:
            node.next = self.head
            self.head = node
        elif self.is_empty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        
    def dequeue(self):
        if self.is_empty():
            return None
        self.head = self.head.next
        
        if self.head is None:
            self.tail = None
    
    def first_value(self):
        if self.is_empty():
            print("A fila está vazia")
            return None
        return self.head.value
    
queue = Queue(5)

queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(5)
queue.enqueue(5)
queue.dequeue()
queue.enqueue(56,9)
queue.enqueue(5)
queue.enqueue(5)
queue.enqueue(5)

print(queue)
        