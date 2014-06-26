################################################################################
##                  Copyright(c) Arsalan Khairani, 2014                       ##
##                              2 Sum Problem                                 ##
##                                                                            ##
## Algorithm for a hashtable application of 2 Sum                             ##
################################################################################

def sum2 (hashTable):
    count = 0
    for x in hashTable.keys():
        for t in range(-10000, 10001):
            if t - x in hashTable.keys() and (t - x) > x:
                count += 1
    return count

file = open("algo1-programming_prob-2sum.txt")
Hashtable = {}
for line in file:
    entry = int(line.strip('\n'))
    Hashtable[entry] = entry

print (sum2(Hashtable))
