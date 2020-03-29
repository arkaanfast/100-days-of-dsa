from collections import defaultdict
from queue import Queue


def bfs(graph):
    q = Queue(maxsize=0)
    first_node = list(graph.keys())[0]
    q.put(first_node)
    while not q.empty():
        node = q.get()
        print(node)
        for child in graph[node]:
            q.put(child)
       


graph = defaultdict(list)

n = int(input("ENTER THE NUBER OF NODES"))

print("Enter u, v where u is the node and v is the the child of u")

for _ in range(n - 1):

    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v] = []

bfs(graph)

