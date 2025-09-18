class Node:

    def __init__(self, key:any):
        self.key = key
        self.left: Node = None
        self.right: Node = None
        self.parent: Node = None
        self.height = 1

class AVLTree:

    def __init__(self, key: any):
        self.root: Node = None



    def insert(self, node: Node, key:any):

        if node is None:
            return Node(key)

        if self.root is None:
            self.root = node
            return self.root


        if node.key > key:
            node.left = self.insert(node.left, key)
            node.left.parent = node
        elif self.root.key < node.key:
            node.right = self.insert(node.right, key)
            node.right.parent = node
        else:
            return node

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    def get_height(self, node: Node) -> int:
        return node.height if node else 0

    def get_balance(self, node: Node):
        return self.get_height(node.right) - self.get_height(node.left)

    def right_rotate(self, node:Node) -> Node:
        x = node.left
        T2 = x.right

        x.right = node
        node.left = T2

        if T2:
            T2.parent = node
        x.parent = node.parent
        node.parent = x

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return  x

    def left_rotate(self, node: Node) -> Node:
        y = node.right
        T2 = y.left

        if T2:
            T2.parent = node

        y.parent = node.parent
        node.parent = y

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def insert_key(self, key: any):
        self.root = self.insert(self.root, key)








