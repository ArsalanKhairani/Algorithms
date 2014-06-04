################################################################################
##                  Copyright(c) Arsalan Khairani, 2014                       ##
##                           Karger's Min Cut                                 ##
##                                                                            ##
## Randomized contraction algorithm to find minimum cut of a graph.           ##
## File Input: The file contains the adjacency list representation of a       ##
##             simple undirected graph. There are 200 vertices.               ##
################################################################################
import random
import copy

cuts = []

# Function: Returns the minimum cut given the graph as input
def karger(graph):
    while len(graph) > 2:
        random.seed()
        
        u = random.choice(list(graph.keys()))
        v = random.choice(graph[u])

        # remove self loops
        for edge in graph[v]:
            if edge != u:
                graph[u].append(edge)

        for edge in graph[v]:
            graph[edge].remove(v)
            if edge != u:
                graph[edge].append(u)

        del graph[v]

    mincut = len(graph[list(graph.keys())[0]])
    cuts.append(mincut)

file = open("kargerMinCut.txt")
graph = {}
for line in file:
    Array = line.split()
    node = int(Array[0])
    edges = []
    edges = [int(i) for i in Array[1:]]
    graph[node] = edges

for i in range(1,801):
    graph1 = copy.deepcopy(graph)
    karger(graph1)
print ("Mincut is", min(cuts))
