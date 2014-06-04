# The file contains the adjacency list representation of a simple undirected
# graph. There are 200 vertices labeled 1 to 200. The first column in the
# file represents the vertex label, and the particular row (other entries
# except the first column) tells all the vertices that the vertex is adjacent
# to. So for example, the 6th row looks like
# : "6	155	56	52	120	......".
# This just means that the vertex with label 6 is adjacent to
#(i.e., shares an edge with) the vertices with labels 155,56,52,120,......,etc
# Your task is to code up and run the randomized contraction algorithm for the
# min cut problem and use it on the above graph to compute the min cut.
# (HINT: Note that you'll have to figure out an implementation of edge contractions.
# Initially, you might want to do this naively, creating a new graph from the
# old every time there's an edge contraction. But you should also think about more
# efficient implementations.) (WARNING: As per the video lectures, please make
# sure to run the algorithm many times with different random seeds, and remember
# the smallest cut that you ever find.) Write your numeric answer in the space
# provided. So e.g., if your answer is 5, just type 5 in the space provided.

import random
import copy

cuts = []

def karger(graph):
    while len(graph) > 2:
        random.seed()
        
        u = random.choice(list(graph.keys()))
        v = random.choice(graph[u])

        # remove self loops
        for edge in graph[v]:
            if edge != u:
                graph[u].append(edge)

        for edge in graph[v]:
            graph[edge].remove(v)
            if edge != u:
                graph[edge].append(u)

        del graph[v]

    mincut = len(graph[list(graph.keys())[0]])
    cuts.append(mincut)

file = open("kargerMinCut.txt")
graph = {}
for line in file:
    Array = line.split()
    node = int(Array[0])
    edges = []
    edges = [int(i) for i in Array[1:]]
    graph[node] = edges

for i in range(1,801):
    graph1 = copy.deepcopy(graph)
    karger(graph1)
print ("Mincut is", min(cuts))

