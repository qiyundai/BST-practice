class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BST:
    def __init__(self, root=None):
        self.root = root

    def insert_val(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            self._insert(val, self.root)

    def _insert(self, val, cur_node):
        if val < cur_node.val:
            if cur_node.left == None:
                cur_node.left = Node(val)
            else:
                self._insert(val, cur_node.left)

        elif val > cur_node.val:
            if cur_node.right == None:
                cur_node.right = Node(val)
            else:
                self._insert(val, cur_node.right)

        else:
            print("The value already exists.")

    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node != None:
            self._print_tree(cur_node.left)
            print(str(cur_node.val))
            self._print_tree(cur_node.right)

    def find_val(self, val):
        if val == self.root.val:
            return self.root
        else:
            bst._find_val(self.root, val)
    
    def _find_val(self, cur_node, val):
        if cur_node.val != None:
            if cur_node.val == val:
                return cur_node
            if cur_node.val > val:
                self._find_val(cur_node.left, val)
            if cur_node.val < val:
                self._find_val(cur_node.right, val)
        else:
            return None

    def add_node(self, val):
        pass


n1 = Node(1)
n3 = Node(3)
n4 = Node(4)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)
n10 = Node(10)
n13 = Node(13)
n14 = Node(14)

n8.left = n3
n8.right = n10
n3.left = n1
n3.right = n6
n6.left = n4
n6.right = n7
n8.right = n10
n10.right = n14
n14.left = n13

bst = BST(n8)

bst.print_tree()