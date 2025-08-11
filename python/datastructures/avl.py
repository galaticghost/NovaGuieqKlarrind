from binaryTree import BinaryTree
from random import randint

class AVLTreeNode():
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
        self.height = 1

    def __str__(self):
        return f"{self.data}"

class AVLTree(BinaryTree):
    root: AVLTreeNode

    def __init__(self):
        self.root = None

    def getHeight(self, node: AVLTreeNode) -> int:
        if not node:
            return 0
        return node.height
    
    def getBalance(self,node: AVLTreeNode) -> int:
        if not node:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)
    
    def insert(self,value:int):
        self.root = self.__insert_recursive(self.root,value)

    def __insert_recursive(self,parent: AVLTreeNode | None,value: int) -> AVLTreeNode | None:
        if not parent:
            return AVLTreeNode(value)
        elif value < parent.data:
            parent.left = self.__insert_recursive(parent.left,value)
        else:
            parent.right = self.__insert_recursive(parent.right,value)

        parent.height = 1 + max(self.getHeight(parent.left),self.getHeight(parent.right))

        balance_factor = self.getBalance(parent)
        if balance_factor > 1:
            if value < parent.left.data:
                return self.right_rotation(parent)
            else:
                parent.left = self.left_rotation(parent.left)
                return self.right_rotation(parent)
        
        if balance_factor < -1:
            if value > parent.right.data:
                return self.left_rotation(parent)
            else:
                parent.right = self.right_rotation(parent.right)
                return self.left_rotation(parent)
        
        return parent
    
    def delete(self,value: int):
        self.root = self.__delete_recursive(self.root,value)
    
    def __delete_recursive(self,parent: AVLTreeNode, value: int) -> AVLTreeNode | None:
        if not parent:
            return parent     
        elif parent.data < value:
            parent.right = self.__delete_recursive(parent.right,value)
        elif parent.data > value:
            parent.left = self.__delete_recursive(parent.left,value)
        else:
            if not parent.left:
                temp = parent.right
                parent = None
                return temp
            elif not parent.right:
                temp = parent.left
                parent = None
                return temp
            parent.data = self._minValueNode(parent.right).data
            parent.right = self.__delete_recursive(parent.right,parent.data)

        if parent is None:
            return parent
        
        parent.height = 1 + max(self.getHeight(parent.left),self.getHeight(parent.right))

        balance_factor = self.getBalance(parent)

        if balance_factor > 1:
            if self.getBalance(parent.left) >= 0:
                return self.right_rotation(parent)
            else:
                parent.left = self.left_rotation(parent.left)
                return self.right_rotation(parent)
        
        if balance_factor < -1:
            if self.getBalance(parent.right) <= 0:
                return self.left_rotation(parent)
            else:
                parent.right = self.right_rotation(parent.right)
                return self.left_rotation(parent)
        
        return parent
        
    def left_rotation(self,node: AVLTreeNode) -> AVLTreeNode:
        y = node.right
        x = y.left
        y.left = node
        node.right = x

        node.height = 1 + max(self.getHeight(node.left),self.getHeight(node.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))

        return y
    
    def right_rotation(self,node: AVLTreeNode) -> AVLTreeNode:
        y = node.left
        x = y.right
        y.right = node
        node.left = x
        
        node.height = 1 + max(self.getHeight(node.left),self.getHeight(node.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))

        return y

if __name__ == "__main__":
    x = [randint(1,999) for _ in range(1,7)]

    tree = AVLTree()
    tree.insert(532)
    
    for x in x:
        tree.bfs()
        tree.insert(x)
    
    tree.bfs()
    tree.delete(532)
    tree.insert(825)
    tree.bfs()
    x = tree.search(825)
    print(x)