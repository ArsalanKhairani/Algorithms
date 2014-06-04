from queue import *

# count will show how many pieces are there in the graph
def connectedComponents(G):
    global explored
    count = 0
    for i in explored.keys():
        if explored[i] == False:
            BFS(G, i)
            count += 1
    print (count)


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


