# A sampl program for a left and right roation (also rightleftrotation and leftrightrotaion) on the bst to make it balanced :)
from traversals import inorder_traversal


def left_rotation(root):

    temp = root.right
    root.right = temp.left
    temp.left = root
    return temp

# Right rotate :)
def right_rotate(root):

    temp = root.left
    root.left = temp.right
    temp.right = root
    return temp


def rightleft_rotate(root):

    root.right = right_rotate(root.right)
    return left_rotation(root)

def leftright_rotate(root):

    root.left = left_rotation(root.left)
    return right_rotate(root)
