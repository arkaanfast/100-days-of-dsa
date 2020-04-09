from traversals import preorder_traversal
from rotations import *

class AvlNode:

    def __init__(self, data):

        self.data = data
        self.left = None
        self.right = None
        self.parent = None


class AvlTree:

    def __init__(self):

        self.root = None
        self.current_size = 0

    # Rebalance if tree is out of balance
    def rebalance(self, node, data):
        if self.height(node.left) - self.height(node.right) > 1:
            if self.height(node.left.left) > self.height(node.left.right):
                if data > node.parent.data:
                    node.parent.right = right_rotate(node)
                else:
                    node.parent.left = right_rotate(node)
            else:
                if data > node.parent.data:
                    node.parent.right = leftright_rotate(node)
                else:
                    node.parent.left = leftright_rotate(node)

        else:
            if self.height(node.right.right) > self.height(node.right.left):
                if data > node.parent.data:
                    node.parent.right = left_rotation(node)
                else:
                    node.parent.left = left_rotation(node) 
            else:
                if data > node.parent.data:
                    node.parent.right = rightleft_rotate(node)
                else:
                    node.parent.left = rightleft_rotate(node)
        


    # Returs the max height
    def height(self, node):

            if node is None:
                return 0

            return max(self.height(node.left), self.height(node.right)) + 1
        

    # Checks if tree is balanced or not 
    def check_balance(self, node):

        if self.height(node.left) - self.height(node.right) > 1 or self.height(node.left) - self.height(node.right) < -1:

            self.rebalance(node, node.data)
        
        if node.parent is None:
            return 
        
        self.check_balance(node.parent)

    # recusrsive add of nodes other than root 
    def add(self, root, node):

        if root.data > node.data:
            if root.left is None:
                root.left = node
                node.parent = root
                self.current_size += 1
            else:
                self.add(root.left, node)
        else:
            if root.right is None:
                root.right = node
                node.parent = root
                self.current_size += 1
            else:
                self.add(root.right, node)

        self.check_balance(node)

    # adding the root
    def add_node(self, data):

        node = AvlNode(data)
        if self.root is None:

            self.root = node
            self.current_size += 1
        
        else:
            self.add(self.root, node)


# Driver program 

avl_tree = AvlTree()

n = int(input("Enter the number of nodes "))

for _ in range(n):

    avl_tree.add_node(int(input()))

preorder_traversal(avl_tree.root)

    