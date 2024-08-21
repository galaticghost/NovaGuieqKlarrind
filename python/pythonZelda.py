# kokokokookkokokokokokokko paiton45

class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return self.data

class LinkedList:
    
    def __init__(self):
        self.head = None

    def add_first(self,node):
        node.next = self.head
        self.head = node
            
    def add_last(self,data):
        node = self.head
        if node == None:
            self.head = data
        else:
            while node.next is not None:
                node = node.next
            node.next = data

    def add_node(self,data,position):
        if position == 1:
            data.next = self.head
            self.head = data
        else:
            self
            pointer = 2
            while pointer != position:
                node = node.next
                pointer += 1
            data.next = node.next
            node.next = data

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            node.data = str(node.data) 
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
        
linked_list = LinkedList()
linked_list.add_last(Node(2))
linked_list.add_last(Node(3))
linked_list.add_first(Node(1))
linked_list.add_node(Node(1.5),2)
print(linked_list)