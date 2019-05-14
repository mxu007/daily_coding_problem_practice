# remove edge to create even trees(make even forest)

# you are given a tree with an even number of nodes. Consider each connections between a parent and child node to be an "Edge". You would like to remove some of these edges, such that the disconnected subtrees that remain each have an even number of nodes.

# write a function that returns the Maximum number of eges you can remove while still satisfying this requirement

# If a node has an odd number of descendants, we can cut off the link between that node and its parent in order to create an even-sized subtree. Each time we do this, we are left with another even-sized group, to which we can apply the same procedure

# we can identify all the nodes with an odd number of descendants (expect root where we could not cut)
# and increment a counter for each
# first perform a DFS traversal through this graph to populate a dicitonary which stores the number of descendants per node. Once it is done, we simply count up how many of thse values are odd and return this total


# To do this, the idea is to use Depth First Search to traverse the tree. Implement DFS function in such a manner that it will return number of nodes in the subtree whose root is node on which DFS is performed. If the number of nodes is even then remove the edge, else ignore.


# dfs uses a set to store nodes visited
# O(V+E) time where V is no.of verticies and E is no.of edges
# O(V) space
def DFS(graph, start, visited = set()):
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            DFS(graph, neighbor, visited)
    return visisted

class Graph(): 
    def __init__(self,vertices): 
        self.graph = defaultdict(list) 
        self.V = vertices 
  
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
        if v not in self.graph:
            self.graph[v] = []

from collections import defaultdict

# dfs traverse returns no.of nodess for each subtree
# O(V+E) time and space
def traverse(graph, curr, result):
    descendants = 0

    for child in graph[curr]:
        # number of nodes is no.of descendants from this specific child
        # result gets update the dictionary for this child
        num_nodes, result = traverse(graph, child, result)
        result[child] += num_nodes - 1
        descendants += num_nodes

    return descendants+1, result

def max_edges(graph):
    # get the first node, list() on a dictionary returns a list of keys for the dictionary
    start = list(graph)[0]
    vertices = defaultdict(int)

    # descendants is a dictionary stores the number of nodes in each subtree
    _, descendants = traverse(graph, start, vertices)

    return len([val for val in descendants.values() if val % 2 == 1])


# Return the number of nodes of   
# subtree having node as a root.  
# save the space complexity since we don't store the descendants into any dictionary
# we only track no.of nodes with even descendants
# O(V+E) time
def dfs(graph, visit, ans, node):
    # variables for two layers here, recursive in nature
    # num stores total number of descendant for this given node
    num = 0
    # descendants stores the no.of descendant for a specific child of current given node
    descendants = 0

    visit.add(node)
    for child in graph[node]:
        if child not in visit:
            # no.of descendant for a child
            descendants = dfs(graph, visit, ans, child)
            # if no.of nodes are not even for this child, we sum to total nodes given current node
            if descendants % 2:
                num += descendants
            # as long as current child has even number of nodes (including the child itself), we will split of this child since we want to maximize no.of even trees
            else:
                ans[0] += 1

    return num + 1

def max_edges_2(graph, n): 
    visit = set()  
    # make ans a single element list for it to be mutable
    ans = [0] 
    # dfs function modifies the value of ans
    dfs(graph, visit, ans, 1)  
    return ans[0] 


if __name__ == "__main__":
    g = Graph(8) 
    g.addEdge(1, 2) 
    g.addEdge(1, 3) 
    g.addEdge(3, 4) 
    g.addEdge(3, 5) 
    g.addEdge(4, 6) 
    g.addEdge(4, 7)
    g.addEdge(4, 8)

    print(max_edges(g.graph))
    print("-----------------")

    g = Graph(10) 
    g.addEdge(1, 3) 
    g.addEdge(1, 6) 
    g.addEdge(1, 2) 
    g.addEdge(3, 4)
    g.addEdge(6, 8)
    g.addEdge(2, 7)
    g.addEdge(2, 5)
    g.addEdge(4, 9)
    g.addEdge(4, 10)

    print(max_edges(g.graph))
    print(max_edges_2(g.graph,2))
