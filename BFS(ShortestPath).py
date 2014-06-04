################################################################################
##                  Copyright(c) Arsalan Khairani, 2014                       ##
##                          Breadth First Search                              ##
##                            Shortest Path                                   ##
##                                                                            ##
## Computes shortest path from one point to another using BFS. Built-in Queue ##
## is used                                                                    ##
################################################################################

from queue import *

# Function: Print shortest path of the graph given the starting vertex s.
def BFS(graph, s):
    explored = { i:False for i in graph.keys() }
    explored[s] = True
    distance = { i : -1 for i in graph.keys() }
    Q = Queue(maxsize = 0)
    Q.put(s)
    while not Q.empty():
        v = Q.get()
        if s == v:
            distance[v] = 0 
        for w in graph[v]:
            if not explored[w]:
                explored[w] = True
                distance[w] = distance[v] + 1
                Q.put(w)

    print (distance)
    

file = open("graph.txt")
graph = {}
for line in file:
    Array = line.split()
    node = int(Array[0])
    edges = []
    edges = [int(i) for i in Array[1:]]
    graph[node] = edges

BFS(graph, 1)
