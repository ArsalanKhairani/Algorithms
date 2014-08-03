################################################################################
##                  Copyright(c) Arsalan Khairani, 2014                       ##
##                          Median Maintenance                                ##
##                                                                            ##
## Algorithm for a heap application of median maintenance                     ##
################################################################################

# Using two heaps a max and a min
# Import these two libraries from Data structures folder
from Heaps import HeapMin
from HeapsMax import HeapMax

file = open("Median.txt")
Hlow = HeapMax()
Hhigh = HeapMin()
#median = []
s = 0

for line in file:
    entry = int(line.strip('\n'))

    # put the entry according to its value
    if entry <= Hhigh.GetMinimum():
        # Then place it in Hlow
        Hlow.Insert(entry)
    else:
        Hhigh.Insert(entry)

    # Now check for size of both heaps
    while Hlow.GetSize() > Hhigh.GetSize() + 1:
        Hhigh.Insert(Hlow.ExtractMax())
        
    while Hhigh.GetSize() > Hlow.GetSize() + 1:
        Hlow.Insert(Hhigh.ExtractMin())

    if Hlow.GetSize() > Hhigh.GetSize():
        #median.append(Hlow.GetMaximum())
        s += Hlow.GetMaximum()

    elif Hhigh.GetSize() > Hlow.GetSize():
        #median.append(Hhigh.GetMinimum())
        s += Hhigh.GetMinimum()

    else:
        # if even no of elements
        #median.append(Hlow.GetMaximum())
        s += Hlow.GetMaximum()

print ("SUM = ", s)
print ("MODULO by 10000 = ", s % 10000)
