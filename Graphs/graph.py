class Graph:

    def __init__(self):

        self.nodes = []

class Graph_Node:

    def __init__(self, data):

        self.data = data
        self.children = []
        self.is_visited = False

    def print_children(self):


        for child in self.children:

            if len(self.children) > 1:
                print(f"{self.data} having neighbour {child.data}")
            
            else:
                print(f"{self.data} having neighbour {child.data}", end=" ")



graph = Graph()

node1 = Graph_Node(1)
node2 = Graph_Node(2)
node1.children.append(node2)
node3 = Graph_Node(3)
node2.children.append(node3)
node4 = Graph_Node(4)
node2.children.append(node4)
node5 = Graph_Node(5)
node1.children.append(node5)

graph.nodes = [node1, node2, node3, node4, node5]

for node in graph.nodes:

    node.print_children()


