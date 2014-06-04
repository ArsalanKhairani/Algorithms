################################################################################
##                  Copyright(c) Arsalan Khairani, 2014                       ##
##                      Recursive Depth First Search                          ##
##                                                                            ##
## Depth first graph searching algorithm. Built-in List is used as stack      ##
################################################################################

# Function: Search all the nodes of the graph given the starting vertex s.
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
