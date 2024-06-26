# BFS: Queue: FIFO

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    # Function to do BFS
    def BFS(self, s):
        visited = [False] *len(self.graph)
        queue = []

        queue.append(s)
        visited[s] = True
        while queue:
            # Dequeue a node from queu and print
            s = queue.pop(0)
            print(s, end = ' ')

            for i in self.graph[s]:
                print(visited[i])
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

g = Graph()
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,2)
g.add_edge(2,0)
g.add_edge(2,3)
g.add_edge(3,3)
g.BFS(2)
