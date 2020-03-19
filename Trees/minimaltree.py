from tree import Tree_Node
from traversals import preorder_traversal

# Create a minimal binary search tree:-
# What is it ?
# Well its a binary search tree having left side and the right side with almost the same level
# Input will be a sorted arrray in increasing order;
# Method i will be using will a recursive one , I will devide the array into two subarays and will keep
# on deviding it until i get one last element then I will return that node. And print the Tree by calling
# The Pre-order traversal method I had created earlier


def createMinimalTree(arr):
    # this method takes an array

    # if the array is empty (arr[0:0] returns an empty array)
    if not arr:
        return

    mid = len(arr) // 2
    root = Tree_Node(arr[mid])
    # First fill up the left part of the tree
    root.left = createMinimalTree(arr[:mid])
    # Then fill the right part of the tree
    # the root will be the mid point of the subarrays.
    root.right = createMinimalTree(arr[mid + 1:])
    return root


arr = [1, 2, 3, 4, 5, 6, 7, 8]

root = createMinimalTree(arr)
# This method will create a minimal BST
# The resulted tree will be as:-
"""  
                        4

                2              6 

            1       3      5       7

"""


preorder_traversal(root)
