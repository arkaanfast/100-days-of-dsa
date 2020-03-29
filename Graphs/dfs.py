from graph import *

# In depth first seach, starting from the root node, the root node is first vistied marked as vist
# then the neighbour of the root node is visited marked as visit then all its neighbours are visited
# When last of the neighbours of the neighbour node are visited, again we come at the root node, and then the process repeats
# taking the next neighbour of the root node
# So basically each node in a branhc is visited, then the net branch is taken for visiting :)

def dfs(root_node):

    print(root_node.data)
    root_node.is_visited = True
    for node in root_node.children:

        if node.is_visited == False:
            dfs(node)




print()
print("THE DEPTH FIRST SEARCH")
dfs(node1)