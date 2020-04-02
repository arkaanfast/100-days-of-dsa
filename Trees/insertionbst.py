from binarysearchtree import *
from traversals import inorder_traversal

# Insert a value into the binary tree:

# The main insertion function begins here :)

def insert_into_bst(root_node, data):

    if root_node is None:
        node = TreeNode(data)
        return node

    if root_node.data < data:
        root_node.right = insert_into_bst(root_node.right, data)
    

    else:
        root_node.left = insert_into_bst(root_node.left, data)

    return root_node
    

        


# Sample input for bst
# Creating a bst with the following values :)
list_of_numbers = [1, 2, 3, 5, 6, 7, 8]

root = convert_to_bst(list_of_numbers)

# Print in pre order mode:
print("Befor insertion")
inorder_traversal(root)

# Insertion starts from here :)

# Sample data input
data = 4

insert_into_bst(root, data)
print()
print("After insertion")
inorder_traversal(root)
