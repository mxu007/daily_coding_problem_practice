# Graph is represented by either adjacency list (dictionary mapping) of each vertext to the other verticies betwee which there is an edge
# or adjacency matrix, each vertex is associated with a row and column of NxN  matrix

# adjacency list representation is more space efficient if there are not that many edges (sparse graph), where an adjacency matrix has faster lookup times to check if a given edge exists but uses more space

# dfs uses a set to store nodes visited
# O(V+E) time where V is no.of verticies and E is no.of edges
# O(V) space
# https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/
def DFS(graph, start, visited = set()):
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            DFS(graph, neighbor, visited)
    return visisted

# bfs uses a queue. For each item we pop off the queue, we find its unvisited neighbors and add them to the end of the queue
# O(V+E) time where V is no.of verticies and E is no.of edges
# O(V) space
# https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
from collections import deque
def BFS(graph, start, visited = set()):
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        visited.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
    return neighbor