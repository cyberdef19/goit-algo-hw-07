class Node:

    def __init__(self, key:any):
        self.key = key
        self.left: Node = None
        self.right: Node = None
        self.parent: Node = None
        self.height = 1

class AVLTree:

    def __init__(self):
        self.root: Node = None

    def insert_key(self, key:int):
        self.root = self.insert(self.root, key)

    def min_value(self):
        if self.root is None:
            print("Дерево порожнє")
            return None

        return self.search_min_value(self.root)


    def search_min_value(self, node: Node) -> int:
        if node.left is None:
            return node.key

        return self.search_min_value(node.left)

    def sum_values(self):
        values = []
        if self.root is None:
            print("Дерево порожнє")
            return None

        self.search_elements(self.root, values)
        return sum(values)

    def search_elements(self, node: Node, lst: list):
        if node is None:
            return

        self.search_elements(node.left, lst)
        lst.append(node.key)
        self.search_elements(node.right, lst)

    def search_left(self, node: Node, lst: list):
        if node is None:
            return

        if node.left is None or node.right is None:
            lst.append(node.key)
            return


        self.search_left(node.left, lst)
        #lst.append(node.key)
        self.search_right(node.right, lst)
        #lst.append(node.key)

    def search_right(self, node: Node, lst: list):
        if node is None:
            return
        if node.right is None:
            lst.append(node.key)
            return

        self.search_right(node.right, lst)
        lst.append(node.key)


    def insert(self, node: Node, key: int) -> Node:

        if node is None:
            return Node(key)


        if node.key > key:
            node.left = self.insert(node.left, key)
            node.left.parent = node
        elif node.key < key:
            node.right = self.insert(node.right, key)
            node.right.parent = node
        else:
            return node

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)

        # 4. Балансування (ротації)
        # LL
        if balance > 1 and node.left and key < node.left.key:
            return self.right_rotate(node)

        # RR
        if balance < -1 and node.right and key > node.right.key:
            return self.left_rotate(node)

        # LR
        if balance > 1 and node.left and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # RL
        if balance < -1 and node.right and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def get_height(self, node: Node) -> int:
        return node.height if node else 0

    def get_balance(self, node: Node):
        return self.get_height(node.right) - self.get_height(node.left)

    def right_rotate(self, node: Node) -> Node:
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

        y.left = node
        node.right = T2

        if T2:
            T2.parent = node

        y.parent = node.parent
        node.parent = y

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def print_tree(self, node: Node = None, level=0, label="root"):
        if node is None:
            node = self.root
            if node is None:
                print("Дерево порожнє")
                return

        print("    " * level + f"{label}: {node.key} (h={node.height})")

        if node.left:
            self.print_tree(node.left, level + 1, label="L")
        if node.right:
            self.print_tree(node.right, level + 1, label="R")


tree = AVLTree()
tree.insert_key(50)
tree.insert_key(30)
tree.insert_key(70)
tree.insert_key(20)
tree.insert_key(40)
tree.insert_key(60)
tree.insert_key(90)
tree.insert_key(35)
tree.insert_key(15)
tree.print_tree()

print(f"Мінімальне значення в дереві по лівій гілці: {tree.min_value()}")
print(f"Сумма всіх значень в дереві {tree.sum_values()}")








