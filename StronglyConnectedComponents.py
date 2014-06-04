# The file contains the edges of a directed graph.
# Vertices are labeled as positive integers from 1 to 875714.
# Every row indicates an edge, the vertex label in first column is the tail
# and the vertex label in second column is the head (recall the graph
# is directed, and the edges are directed from the first column vertex to
# the second column vertex). So for example, the 11th row looks
# likes : "2 47646". This just means that the vertex with label 2 has
# an outgoing edge to the vertex with label 47646.
# Your task is to code up the algorithm from the video lectures for
# computing strongly connected components (SCCs), and to run this algorithm
# on the given graph. 
# Output Format: You should output the sizes of the 5 largest
# SCCs in the given graph, in decreasing order of sizes, separated by commas
# (avoid any spaces). So if your algorithm computes the sizes of the five
# largest SCCs to be 500, 400, 300, 200 and 100, then your answer
# should be "500,400,300,200,100". If your algorithm finds less than 5 SCCs,
# then write 0 for the remaining terms. Thus, if your algorithm computes
# only 3 SCCs whose sizes are 400, 300, and 100, then your answer should be
# "400,300,100,0,0".

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
