from tree import Tree_Node


def inorder_traversal(node):

    if node is None:
        return

    inorder_traversal(node.left)
    print(node.data, end=" ")
    inorder_traversal(node.right)


def preorder_traversal(node):

    if node is None:
        return

    print(node.data, end=" ")
    preorder_traversal(node.left)
    preorder_traversal(node.right)


def postorder_traversal(node):

    if node is None:
        return

    postorder_traversal(node.left)
    postorder_traversal(node.right)
    print(node.data, end=" ")


root_node = Tree_Node(4, "node " + str(1))
root_node.left = Tree_Node(2, "node " + str(2))
root_node.right = Tree_Node(5, "node " + str(3))
root_node.left.left = Tree_Node(10, "node " + str(4))
root_node.left.right = Tree_Node(20, "node " + str(5))
print(" " * 20, root_node.data)
print()
print(" " * 10, root_node.left.data, end=(" " * 18))
print(root_node.right.data)
print()
print(" " * 5, root_node.left.left.data, end=(" " * 7))
print(root_node.left.right.data)

print()
print("Inorder traversal => ", end=" ")
inorder_traversal(root_node)
print()
print("Preorder traversal => ", end=" ")
preorder_traversal(root_node)
print()
print("PostOrder traversal => ", end=" ")
postorder_traversal(root_node)
print()
