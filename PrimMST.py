################################################################################
##                  Copyright(c) Arsalan Khairani, 2014                       ##
##                      Recursive Depth First Search                          ##
##                                                                            ##
## Depth first graph searching algorithm. Built-in List is used as stack      ##
################################################################################file = open("graph3.txt")

def getscore(a, b):
    return a / b

def main():
    file = open("edges.txt")
    info = file.readline().split(" ")
    nodes = int(info[0])
    edges = int(info[1])

    graph = []
    allVertices = set() # set
    
    for line in file:
        info = line.split(" ")
        v1 = int(info[0])
        if v1 not in allVertices:
            allVertices.add(v1)
        v2 = int (info[1])
        if v2 not in allVertices:
            allVertices.add(v2)
        l =  int (info[2])
        graph.append((l, v1, v2))

    g = sorted(graph)
        

    X = set({graph[0][1]}) # Just intialization
    T = []
    
    while X != allVertices:
        allEdges = [edge for edge in g if ((edge[1] in X and edge[2] not in X) or (edge[2] in X and edge[1] not in X))]
        sortedEdges = sorted(allEdges)
        e = sortedEdges[0]

        T.append(e[0]) # add span to T
        X.add(e[1] if e[1] not in X else e[2]) # Add a vertex to X

    print (sum(T))
    
if __name__ == "__main__":
    main()
