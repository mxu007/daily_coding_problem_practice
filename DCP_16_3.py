# Floyd Warshall
# Transitive closure, find out if a vertex j is reacable FROM another vertex i for all vertex pairs(i,j)
# reachable means that there is a path from vertex i to j. The reachability matrix is called transitive closure of a graph


# O(V^3) time complexity for the nested for loops
# O(V^2) to store the output
def closure(graph):
    # graph represented as a dictionary(adjacency list)
    n = len(graph)
    reachable = [[0 for _ in range(n)] for _ in range(n)]

    # from edge update the direct linkage to the reachable dictionary
    for key, lst in graph.items():
        #print(key,lst)
        for neighbor in lst:
            reachable[key][neighbor] = 1
        reachable[key][key] = 1

    # see if we can reach from i to j through intermediate k
    for k in range(n):
        for i in range(n):
            for j in range(n):
                reachable[i][j]  = reachable[i][j] | (reachable[i][k] and reachable[k][j])

    return reachable

if __name__ == "__main__":
    graph = {
        0:[1,3],
        1:[2],
        2:[],
        3:[]
    }
    print(closure(graph))
    

