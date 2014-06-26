################################################################################
##                  Copyright(c) Arsalan Khairani, 2014                       ##
##                             Max - Heap                                     ##
##                                                                            ##
## Implementation of max heap data structure.                                 ##
## Using Array rather then linked tree.                                       ##
################################################################################

import math

# Function: Insert then "element" in heap
# Please input 1 index based heap array i.e. root is at index 1
class HeapMax:

    heap = []

    def __init__(self, heap = [0]):
        self.heap = heap

    def __str__(self):
        return str(self.heap)

    def Insert(self, element):
        self.heap.append( element )
        n = len(self.heap) - 1

        while ( n > 1 and self.heap[n] > self.heap[math.floor(n/2)] ):
            temp = self.heap[math.floor(n/2)]
            self.heap[math.floor(n/2)] = self.heap[n]
            self.heap[n] = temp
            n = math.floor(n/2)

        return self.heap

    def ExtractMax(self):
        maximum = self.heap[1]
        n = len(self.heap) - 1
        self.heap[1] = self.heap[n]
        self.heap.pop()

        i = 1
        # Incase of both Childs
        while ( (2*i) + 1 < n  and
                (self.heap[i] < self.heap[2*i]
                 or self.heap [i] < self.heap[(2*i) + 1])):
            if ( self.heap[2*i] > self.heap[(2*i) + 1] ):
                temp = self.heap[i]
                self.heap[i] = self.heap[2*i]
                self.heap[2*i] = temp
                i = 2*i
            else:
                temp = self.heap[i]
                self.heap[i] = self.heap[(2*i) + 1]
                self.heap[(2*i) + 1] = temp
                i = (2*i) + 1

        # For only left child
        while ( (2*i) < n and (self.heap[i] < self.heap[2*i])):
            temp = self.heap[i]
            self.heap[i] = self.heap[2*i]
            self.heap[2*i] = temp
            i = 2*i

        # No need for the case of just right child as it cannot occur
        return maximum

    def GetMaximum(self):
        if self.GetSize() > 0:
            maximum = self.heap[1]
            return maximum
        return 0

    def GetSize(self):
        return len(self.heap) - 1
