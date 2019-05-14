# Determine if a cycle exists
# Given an UNDIRECTED graph, determine if it contains a cycle

# implement the solution using depth-first search. For each vertex in the graph, if it has not already been visited. we call our search function on it. This function will recursively traverse unvisited neighbors of the vertex and return True if we come accross the cycle.

from collections import defaultdict 
  
class Graph(): 
    def __init__(self,vertices): 
        self.graph = defaultdict(list) 
        self.V = vertices 
  
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
        if v not in self.graph:
            self.graph[v] = []

# O(V+E) time complexity where V is no.of verticies and E is no.of edges
# O(V) for visiting each vertice, E for adding each edge connected to the vertice currently visiting

def search(graph, vertex, visited, parent):
    visited[vertex] = True

    # graph is an adjacency list
    # for neighbor iterate all possible edges
    for neighbor in graph[vertex]:
        # recursive call, but this is searching on the same level
        if not visited[neighbor]:
            # recursive call explore each possible verticies
            if search(graph, neighbor, visited, vertex):
                return True
        # if this neighbor has been visited and this neighbor is not he parent of current vertex
        # it indicates a cycle
        elif parent != neighbor:
            return True

    return False

def has_cycle(graph):
    visited = {v: False for v in graph.keys()}

    for vertex in graph.keys():
        if not visited[vertex]:
            if search(graph, vertex, visited, None):
                return True
    
    return False

if __name__ == "__main__":
    g = Graph(4) 
    g.addEdge(0, 1) 
    g.addEdge(0, 2) 
    #g.addEdge(1, 2) 
    # g.addEdge(2, 0) 
    g.addEdge(2, 3) 
    #g.addEdge(3, 1) 
    print(has_cycle(g.graph))
    
    g = Graph(4) 
    g.addEdge(0, 1) 
    g.addEdge(0, 2) 
    #g.addEdge(1, 2) 
    g.addEdge(2, 3) 
    g.addEdge(3, 1) 
    print(has_cycle(g.graph))

