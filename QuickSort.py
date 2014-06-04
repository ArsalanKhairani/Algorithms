################################################################################
##                  Copyright(c) Arsalan Khairani, 2014                       ##
##                              Quick Sort                                    ##
##                                                                            ##
## Sort an array of integers using quick sort algorithm.                      ##
################################################################################

# Function: Given an array with its left and right indices returns the position
#           of pivot
def Partition(arr, left, right):

    pivot = arr[left]           # Make the first element from left the pivot
    i = left + 1

    # This loop compare each entry with pivot
    for j in range(left + 1, right + 1):
        if arr[j] < pivot:
            temp   = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
            i += 1
        print (arr)
            
    arr[left] = arr[i - 1]
    arr[i - 1] = pivot

    # Returns the position of the pivot
    return i - 1
    
# Function: Sort an array around the pivot
def QuickSort(arr, start, end):

    # base case
    if (end - start) <= 1:
        return

    # Choosing pivot method - Here
    
    # partition sub routine
    pivot = Partition(arr, start, end)
    
    # Call recursion
    QuickSort(arr, start, pivot - 1)
    QuickSort(arr, pivot + 1, end)

    return (arr)
