from rotations import *
from traversals import preorder_traversal

class AvlNode:

    def __init__(self, data):

        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class AvlTree:

    def insert(self, root, data):

        if root is None:
            return AvlNode(data)

        elif root.data < data:

            root.right = self.insert(root.right, data)

        else:
            root.left = self.insert(root.left, data)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        # there is imbalance in the left side:
        if balance > 1:
            if data < root.left.data:
                # imbalance is of type left left 
                new_root = right_rotate(root)
                new_root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
                root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
                return new_root
            elif data > root.left.data:
                # imbalance is of type left right 
                new_root = leftright_rotate(root)
                new_root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
                root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
                return new_root
        
        # there is imbalance in the right sife:
        if balance < -1:
            if data > root.right.data:
                # imbalance is of right right 
                new_root = left_rotation(root)
                new_root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
                root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
                return new_root 

            elif data < root.right.data:
                # imbalance is of type right left
                new_root = rightleft_rotate(root)
                new_root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
                root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
                return new_root
        return root

    def get_height(self, root):

        if root is None:
            return 0

        else:
            return root.height

    def get_balance(self, root):

        if root is None:
            return 0
        else:
            return self.get_height(root.left) - self.get_height(root.right)


# driver program


avl_tree = AvlTree()

n = int(input("Enter the number of nodes "))
new_root = None
for _ in range(n):

    root = avl_tree.insert(new_root, int(input().rstrip()))
    new_root = root

preorder_traversal(root)


