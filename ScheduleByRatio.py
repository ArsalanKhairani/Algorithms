################################################################################
##                  Copyright(c) Arsalan Khairani, 2014                       ##
##                        Scheduling Application                              ##
##                                                                            ##
## Example of Greedy algorithm that determines sequence of task over shared   ##
## resources                                                                  ##
################################################################################

def getscore(a, b):
    # ration is optimal however you can also do difference
    # return a - b
    return a / b

def main():
    file = open("jobs.txt")
    count = int(file.readline())
    i = 0
    res = []

    while i < count:
        li = [int(j) for j in file.readline().strip().split(" ")]
        res.append((getscore(li[0], li[1]), li[0], li[1]))
        i += 1
    final = sorted(res, reverse = True)
    
    minimum = 0
    completionTime = 0
    for entry in final:
        completionTime += entry[2]
        minimum += ( entry[1] * completionTime )

    print (minimum)
        
if __name__ == "__main__":
    main()
