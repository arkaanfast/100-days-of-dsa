from binarysearchtree import * 
from traversals import inorder_traversal

def min_node_value(root):

    while root.left is not None:
        root = root.left

    return root

def delete_from_bst(root, data):

    if root is None:
        return root

    if root.data < data:
        root.right = delete_from_bst(root.right, data)

    if root.data > data:
        root.left = delete_from_bst(root.left, data)

    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        
        if root.right is None:
            temp = root.left
            root = None
            return temp

        elif root.right is not None:
             temp = min_node_value(root.right)
             root.data = temp.data
             root.right = delete_from_bst(root.right, temp.data)
    return root

# Sample inputs 

# Creating a bst 

list_of_data = [1, 2, 3, 4, 5, 6, 7, 8]
root = convert_to_bst(list_of_data)

# Sample input to delete a node from tree:)

data = 2

root = delete_from_bst(root, data)
print(f"After deleting {data} ")
inorder_traversal(root)