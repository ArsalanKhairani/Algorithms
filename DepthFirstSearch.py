from queue import *

def DFS(graph, s):
    explored = { i:False for i in graph.keys()}
    explored[s] = True
    stack = []
    stack.append(s)
    while not len(stack) == 0:
        v = stack.pop()
        for w in graph[v]:
            print (str(v), str(w))
            if not explored[w]:
                explored[w] = True
                stack.append(w)
    

file = open("graph3.txt")
graph = {}
for line in file:
    Array = line.split()
    node = int(Array[0])
    edges = []
    edges = [int(i) for i in Array[1:]]
    graph[node] = edges

DFS(graph, 1)
