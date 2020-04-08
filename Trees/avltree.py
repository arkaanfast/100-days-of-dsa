from traversals import preorder_traversal


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

        # self.check_balance(node)


    def add_node(self, data):

        node = AvlNode(data)
        if self.root is None:

            self.root = node
        
        else:
            self.add(self.root, node)


# Driver program 

avl_tree = AvlTree()

n = int(input("Enter the number of nodes "))

for _ in range(n):

    avl_tree.add_node(int(input()))

preorder_traversal(avl_tree.root)

    