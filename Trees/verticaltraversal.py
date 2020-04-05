from tree import Tree_Node

def vertical_traversal(root, hd, hm):

    if root is None:
        return 
    try:
        hm[hd].append(root.data)
    except:
        hm[hd] = [root.data]

    vertical_traversal(root.left, hd - 1, hm)
    vertical_traversal(root.right, hd + 1, hm)

    return hm
    
root_node = Tree_Node(4)
root_node.left = Tree_Node(2)
root_node.right = Tree_Node(5)
root_node.left.left = Tree_Node(10)
hm = vertical_traversal(root_node, 0, {})
for key in sorted(hm):

    print(hm[key])
