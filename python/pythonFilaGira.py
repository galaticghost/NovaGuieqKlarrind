# pwimt

class Queue:

    def __init__(self,size):
        self.size = size

        self.queue = [None for _ in range(size)]
        self.front = self.rear = -1