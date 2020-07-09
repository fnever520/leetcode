# DFS: stack - LIFO

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def DFSUtil(self, v, visited):
        # Mark the current node as visited
        visited[v] = True
        print(v, end=' ')
        print(visited)

        # Recur for all nodes adjacent to this node
        for i in self.graph[v]:
            if not visited[i]:
                self.DFSUtil(i, visited)

    # This function do DFS traversal.
    def DFS(self, v):
        # Mark all the nodes as not visited
        visited = [False] * len(self.graph)
        self.DFSUtil(v, visited)

g = Graph()
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,2)
g.add_edge(2,0)
g.add_edge(2,3)
g.add_edge(3,3)
g.DFS(2)
