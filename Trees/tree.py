# Implementing tree (not taking the user input)


class Tree_Node:

    def __init__(self, data):

        # self.name = name
        self.data = data
        self.left = None
        self.right = None

    # def __str(self):

    #     return self.name


# root_node = Tree_Node(4, "node " + str(1))
# root_node.left = Tree_Node(2, "node " + str(2))
# root_node.right = Tree_Node(5, "node " + str(3))
# root_node.left.left = Tree_Node(10, "node " + str(4))
# print(" " * 20, root_node.data)
# print()
# print(" " * 10, root_node.left.data, end=(" " * 20))
# print(root_node.right.data)
# print()
# print(" " * 5, root_node.left.left.data)
