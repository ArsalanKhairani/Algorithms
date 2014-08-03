def main():
    file = open("cl.txt")
    totalNodes = int(file.readline().rstrip())

    graph = []

    for l in file:
        line = l.rstrip().split(" ")
        graph.append((int(line[2]), int(line[0]), int(line[1])))

    graph = sorted(graph)
    k = totalNodes
    clusters = [[i] for i in range(1, totalNodes + 1)]

    i = 0
    while k != 4:
        

if __name__ == "__main__":
    main()
