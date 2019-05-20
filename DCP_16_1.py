# Dijkstra's algorithm -- find the shortest path
# You are given a list of edges (a,b,t) describe the time t in seconds it takes fr a message to be sent from node a to node b. Whenever a node receives a message, it immediately passses the message on toa neighboring node if possible.
# Assuming all nods are connected, determine how long it will take for every node to receive a message that begin at node 0

# list of weighted edges(u,v,weight)
# [
#     (0,1,5),
#     (0,2,3),
#     (0,5,4),
#     (1,3,8),
#     (2,3,1),
#     (3,5,10),
#     (3,4,5)
# ]

# think of the network nodes as vertices on a graph, each connection as an edge
class Network:
    def __init__(self, N, edges):
        self.vertices = range(N+1)
        self.edges = edges
    
    # graph represented as adjacency list, the list of tuples where each tuple has (node,cost) info
    def make_graph(self):
        graph = {v:[] for v in self.vertices}

        for u,v,w in network.edges:
            # each graph[u] has a list of tuples
            graph[u].append((v,w))
        return graph

# Dijkstra's algorithm computes the shortest path between two vertices of a graph with assumption that all edges have nonnegative weight.
# It works by repeatedly traveling to the cloest vertex whic has not yet been reached
# O(n^2 time complexity). The outer loop takes O(n) and inner loop takes O(n) too
# O(m) space where m stands for number of edges, since all edge info has been stored in graph and times
def propagate(network):
    graph = network.make_graph()
    # set the time(distance) to be inf
    times = {node:float('inf') for node in graph}
    # begin node is 0
    times[0] = 0
    
    # get list of nodes in graph
    q = list(graph)
    print(q)
    while q:
        # https://stackoverflow.com/questions/18296755/python-max-function-using-key-and-lambda-expression
        # get the source node (u) with minimum weight
        # lambda function on variable x: apply times[x]
        # find the new node with minimum cost to travel to, this expands the path
        u = min(q, key=lambda x: times[x])
        print("u",u)
        # remove node u from graph list q
        q.remove(u)
        # iterate the graph represented by adjacency list
        # update the shortest distance to v
        for v,time in graph[u]:
            times[v] = min(times[v], times[u]+time)
            print("times when evaluating", u, "to reach",  v, "is", times[v])
    # the largest value in the dictionary will represent the time it will take for the last node to get the msg
    print(times)
    return max(times.values())


# for sparse graph, using heapq (priority queue)
# starting from 0, each time we encounter a new neighbor, we add it to the queue, with value eqaul to the sum of time from node zero to the current node and ffrom the current node the neighbor. Whenever we pop a node off the queue that does not exisit in our times dictionary, we add a new key with the corresponding values
# O(logV) time for pop or push an element from the heap, where V is no.of verticies
# O(Vlog(V)) for the inner heapq.heappush
import heapq
def propagate_1(network):
    graph = network.make_graph()
    times = {}
    # q is a priority queue of tuples, where each tuple has (cost,node) info
    q = [(0,0)]

    while q:
        # heapque pop the smallest element
        u, node = heapq.heappop(q)
        # node not in times meaning node has not been visited
        if node not in times:
            times[node] = u
            # find all neightbors (which connects to current node) and associated cost
            # Heap elements can be tuples. This is useful for assigning comparison values (such as task priorities) alongside the main record being tracked:
            # you can use tuples, and it will sort by the first element of the tuple:
            for neighbor, v in graph[node]:
                heapq.heappush(q, (u+v, neighbor))
    return max(times.values())




if __name__ == "__main__":
    
    edges = [
            (0,1,5),
            (0,2,3),
            (0,5,4),
            (1,3,8),
            (2,3,1),
            (3,5,10),
            (3,4,5)
            ]
    network = Network(5, edges)
    #print(network.edges)
    print(propagate(network))
    print("------------------")

    print(propagate_1(network))