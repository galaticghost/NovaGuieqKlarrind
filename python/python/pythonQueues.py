class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue:
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __str__(self):
        if self.is_empty():
            return f"The stack is empty"
        valores = []
        current = self.head
        while current:
            valores.append(str(current.value))
            current = current.next
        return " -> ".join(valores)
    
    def is_empty(self):
        return self.head is None
    
    def enqueue(self,value,priority = None):
        node = Node(value)
        
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
    
queue = Queue()

queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(5)
queue.enqueue(5)
queue.dequeue()
queue.enqueue(56,9)

print(queue)
        