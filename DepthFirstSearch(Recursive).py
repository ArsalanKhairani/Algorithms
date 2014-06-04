from queue import *

def DFS(graph, s):
    global explored
    explored[s] = True
    for v in graph[s]:
        print (str(s), str(v))
        if not explored[v]:
            DFS(graph, v)
    

file = open("graph3.txt")
graph = {}
for line in file:
    Array = line.split()
    node = int(Array[0])
    edges = []
    edges = [int(i) for i in Array[1:]]
    graph[node] = edges

explored = { i:False for i in graph.keys() }
DFS(graph, 1)
