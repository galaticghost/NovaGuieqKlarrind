from random import randint

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
    
    def __str__(self):
        return f"{self.data}"

class BinaryTree:
    root: TreeNode

    def __init__(self,data):
        self.root = TreeNode(data)

    def bfs(self):
        queue = []
        queue.append(self.root)

        while queue:
            current_value = queue.pop(0)
            print (current_value.data, end = " ")

            if current_value.left not in queue and current_value.left is not None:
                queue.append(current_value.left)
            if current_value.right not in queue and current_value.right is not None:
                queue.append(current_value.right)
        print("")

    def preOrderTraversal(self):
        self.__pot(self.root)
        print("")

    def __pot(self,node):
        if node is None:
            return
        print(node.data, end=" ")
        self.__pot(node.left)
        self.__pot(node.right)

    def inOrderTraversal(self):
        self.__iot(self.root)
        print("")

    def __iot(self,node):
        if node is None:
            return
        self.__iot(node.left)
        print(node.data, end=" ")
        self.__iot(node.right)

    def postOrderTraversal(self):
        self.__postot(self.root)
        print("")

    def __postot(self,node):
        if node is None:
            return
        self.__postot(node.left)
        self.__postot(node.right)
        print(node.data, end=" ")

    def insert(self,data,current_node = None):
        if current_node is None:
            current_node = self.root

        if data > current_node.data:
            if current_node.right is None:
                current_node.right = TreeNode(data)
                return
            self.insert(data,current_node.right)
        elif data < current_node.data:
            if current_node.left is None:
                current_node.left = TreeNode(data)
                return
            self.insert(data,current_node.left)

    def search(self,data):
        return self.__search_rec(self.root,data)

    def __search_rec(self,node,data):
        if node == None:
            return False
        print(node.data)
        if node.data == data:
            return True
        elif node.data > data:
            return self.__search_rec(node.left,data)
        else:
            return self.__search_rec(node.right,data)

nodes_values = [] * 500

for _ in range(0,500):
    nodes_values.append(randint(1,9999))

root = BinaryTree(nodes_values[0])

for x in nodes_values[1:]:
    root.insert(x)

print(root.search(50))
