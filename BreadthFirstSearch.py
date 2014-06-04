from queue import *

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

