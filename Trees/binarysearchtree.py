from traversals import preorder_traversal

class TreeNode:


    def __init__(self, data):

        self.data = data
        self.left = None
        self.right = None



def convert_to_bst(numbers):

    if not numbers:
        return None

    mid = (len(numbers)) // 2
    node = TreeNode(numbers[mid])
    node.left = convert_to_bst(numbers[:mid])
    node.right = convert_to_bst(numbers[mid + 1:]) 
    return node




# print("Create your binary search tree ")
# print("****Type in the Data values for your nodes****")
# list_of_data = list(map(int, input().split()))
# list_of_data.sort()

# root_node = convert_to_bst(list_of_data)

# preorder_traversal(root_node)
