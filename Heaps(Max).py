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
def Insert(heap, element):
    heap.append( element )
    n = len(heap) - 1

    while ( n > 1 and heap[n] > heap[math.floor(n/2)] ):
        temp = heap[math.floor(n/2)]
        heap[math.floor(n/2)] = heap[n]
        heap[n] = temp
        n = math.floor(n/2)

    return heap

def ExtractMax(heap):
    minimum = heap[1]
    n = len(heap) - 1
    heap[1] = heap[n]
    heap.pop()
    i = 1
    while ( (2*i) + 1 < n  and
            (heap[i] < heap[2*i] or heap [i] < heap[(2*i) + 1])):
        if ( heap[2*i] > heap[(2*i) + 1] ):
            temp = heap[i]
            heap[i] = heap[2*i]
            heap[2*i] = temp
            i = 2*i
        else:
            temp = heap[i]
            heap[i] = heap[(2*i) + 1]
            heap[(2*i) + 1] = temp
            i = (2*i) + 1

    return minimum
