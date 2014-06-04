################################################################################
### Not working properly :(
################################################################################
##                  Copyright(c) Arsalan Khairani, 2014                       ##
##                          Depth First Search                                ##
##                   Strongly Connected Components                            ##
##                                                                            ##
## Computes strongly connected components of the graph using DFS.             ##
## File Input: The file contains the edges of a directed graph. Vertices are  ##
##             labeled as positive integers from 1 to 875714.                 ##
################################################################################

# 
s = 0
leader = {}
f = {}
t = 0
SCC = []
SCCcount = 0

def DFS_Loop(G):
    global t, s, explored
    t = 0
    for i in reversed(list(G.keys())):
        print (i)
        if not explored[i]:
            s = i
            DFS(G, i)

def DFS_Loop2(G):
    global t, s, explored, f, SCCcount
    t = 0
    for i in f.keys():
        i = f[i]
        print (i)
        if not explored[i]:
            SCCcount = 0
            s = i
            DFS2(G, i)
            SCC.append(SCCcount)

def DFS2(G, i):
    global explored, leader, f, t, s, SCCcount
    explored[i] = True
    leader[i] = s
    SCCcount += 1
    for j in G[i]:
        if not explored[j]:
            DFS2(G, j)

    t+=1

def DFS(G, i):
    global explored, leader, f, t, s
    explored[i] = True
    for j in G[i]:
        if not explored[j]:
            DFS(G, j)

    t+=1
    f[i] = t
            
file = open("directedGraph.txt")
graph = {}
graphRev = {}
for line in file:
    Array = line.split()
    node = int(Array[0])
    nodeRev = int(Array[1])
    if node not in graph.keys():
        graph[node] = []
    
    graph[node].append(int(Array[1]))

    if nodeRev not in graphRev.keys():
        graphRev[nodeRev] = []
    
    graphRev[nodeRev].append(int(Array[0]))

explored = { i: False for i in graphRev.keys() }
DFS_Loop(graphRev)
print (f)
explored = { i: False for i in graphRev.keys() }
DFS_Loop2(graph)
print (SCC)
