from traversals import preorder_traversal

class TreeNode:


    def __init__(self, data):

        self.data = data
        self.left = None
        self.right = None


class Tree:

    def __init__(self):

        self.root = None

    
    def add(self, root, node):

        if root.data > node.data:

            if root.left is None:
                root.left = node
            else:
                self.add(root.left, node)

        else: 
            if root.right is None:
                root.right = node
            else:
                self.add(root.right, node)

    
    def add_root(self, data):

        node = TreeNode(data)

        if self.root is None:

            self.root = node

        else:

            self.add(self.root, node)
