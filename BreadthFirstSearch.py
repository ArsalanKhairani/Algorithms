################################################################################
##                  Copyright(c) Arsalan Khairani, 2014                       ##
##                          Breadth First Search                              ##
##                                                                            ##
## Breadth first graph searching algorithm. Built-in Queue is used            ##
################################################################################
from queue import *

# Function: Search all the nodes of the graph given the starting vertex s.
def BFS(graph, s):
    explored = { i:False for i in graph.keys()}
    explored[s] = True
    Q = Queue(maxsize = 0)
    Q.put(s)
    while not Q.empty():
        v = Q.get()
        for w in graph[v]:
            print (str(v), str(w))
            if not explored[w]:
                explored[w] = True
                Q.put(w)
    

file = open("graph3.txt")
graph = {}
for line in file:
    Array = line.split()
    node = int(Array[0])
    edges = []
    edges = [int(i) for i in Array[1:]]
    graph[node] = edges

BFS(graph, 1)

