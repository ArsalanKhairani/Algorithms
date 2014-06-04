################################################################################
##                  Copyright(c) Arsalan Khairani, 2014                       ##
##                          Breadth First Search                              ##
##                         Undirected Connectivity                            ##
## Application of BFS to compute undirected connectivity of the graph         ##
################################################################################
from queue import *

# Function: Find all the connected components from the all the nodes
def connectedComponents(G):
    global explored
    count = 0
    for i in explored.keys():
        if explored[i] == False:
            BFS(G, i)
            count += 1
    print (count)

# Function: Search all the nodes of the graph given the starting vertex s.
def BFS(graph, s):
    global explored
    explored[s] = True
    Q = Queue(maxsize = 0)
    Q.put(s)
    while not Q.empty():
        v = Q.get()
        for w in graph[v]:
            if not explored[w]:
                explored[w] = True
                Q.put(w)

file = open("graph2.txt")
graph = {}
for line in file:
    Array = line.split()
    node = int(Array[0])
    edges = []
    edges = [int(i) for i in Array[1:]]
    graph[node] = edges

explored = { i:False for i in graph.keys()}
connectedComponents(graph)


