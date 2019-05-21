# Given a table of currency exchange rates, represented as a 2-D array, determine whether there is a possible arbitrage opportunity

#  Bellman–Ford algorithm is an algorithm that computes shortest paths from a single source vertex to all of the other vertices in a weighted digraph.[

# e.g. graph = 
# {
#     'USD': {'GBP':0.77, 'INR':71.71, 'EUR':0.87},
#     'GBP': {'USD':1.30, 'INR':93.55, 'EUR':1.14},
#     'INR': {'USD':0.014, 'GBP':0.011, 'EUR':0.012},
#     'EUR': {'USD':1.14, 'GBP':0.88, 'INR':81.95}
# }

# Find out if there is some sequence of trades you can make, starting with some amount X of any currency, so that you can end up with some amount greater than X of that currentcy

# model the currencies and exchange rates as a graph, where nodes are currencies and edges are the exchange ratess between each currencies

# we must determine if it is possible to find a cycle whose edge weight product is greater than 1
# log(ab) = log(a) + log(b)
# take log and negate, the problem becomes finding a negative sum cycle
# O(n^3) time where n is no.of currencies
from math import log
def arbitrage(table):
    transformed_graph =  {}
    for key in graph:
        transformed_graph[key] = {}
        for subkey, edge in graph[key].items():
            transformed_graph[key][subkey] = -log(edge)

    print(transformed_graph)
    #transformed_graph = [[-log(edge) for _, edge in graph[key].items()] for key in graph]
    # fixing source node
    source = 'USD'
    n = len(transformed_graph)
    keys = ['USD', 'GBP', 'INR', 'EUR']
    # set init distance to all other nodes to be infinity
    min_dist = {key:float("inf") for key in keys}
    min_dist[source] = 0
    print(min_dist)
    
    # iterate remaining nodes, udpate the distance
    for i in keys[1:]:
        for v in keys:
            for w in keys:
                #print(i,v,w)
                if v != w:
                    if min_dist[w] > min_dist[v] + transformed_graph[v][w]:
                        min_dist[w] = min_dist[v] + transformed_graph[v][w]
    
    print(min_dist)

    # if we could still relax edges, then we have a negative cycle
    # any graph with V vertices, longest path can have at most |V|-1 edges
    # if after |V|-1 iterations, we can still find a smaller path, there must be a negative cycle in the graph
    for v in keys:
        for w in keys:
            if v != w:
                if min_dist[w] > min_dist[v] + transformed_graph[v][w]:
                    print(w, min_dist[w], v, min_dist[v], transformed_graph[v][w])
                    return True
    return False

if __name__ == "__main__":
    graph = {
        'USD': {'GBP':0.77, 'INR':71.71, 'EUR':0.87},
        'GBP': {'USD':1.30, 'INR':93.55, 'EUR':1.14},
        'INR': {'USD':0.014, 'GBP':0.011, 'EUR':0.012},
        'EUR': {'USD':1.14, 'GBP':0.88, 'INR':81.95}
        }
    # for key in graph:
    #     for subkey, edge in graph[key].items():
    #         print(subkey,edge)

    print(arbitrage(graph))
