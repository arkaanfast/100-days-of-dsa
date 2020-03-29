# In breadth first search, starting at the root node, visits all of its neighbours
# after visiting a nodes neighbours, it then goes to the roots neighbour and then visits **its neighbours**

# This will be implemented using a Queue, visited nodes will added in the Queue

from graph import *
from queue import Queue

def bfs(node):

    # Initializing a queue with ifinite size;
    q = Queue(maxsize = 0)  
    q.put(node)

    while not q.empty():

        n = q.get()
        print(n.data)

        for child in n.children:

            q.put(child)

print()
print("BREADTH FIRST SEARCH")
bfs(node1)

