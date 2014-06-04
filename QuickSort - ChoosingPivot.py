################################################################################
##                  Copyright(c) Arsalan Khairani, 2014                       ##
##                   Quick sort using different pivots                        ##
##                                                                            ##
## This implementation shows the impact due to different pivots in quick sort ##
## on no. of comparisions. Pivots chossen are left, right and median          ##
################################################################################

# records no of comparisions
comparisions = 0

# Function: Given an array with its left and right indices returns the position
#           of pivot
# First as pivot 162085
# Last as pivot 164123
# Median as pivot 138382
def Partition(arr, left, right):

    # For making left entry as pivot do nothing
    # For making right entry as pivot uncomment next line:
    #RightPivot(arr, left, right)
    # For making medain as pivot uncomment next line:
    MedianPivot(arr, left, right)
    pivot = arr[left]
    i = left + 1
    
    # This loop compare each entry with pivot
    for j in range(left + 1, right + 1):
        if arr[j] < pivot:
            temp   = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
            i += 1
            
    arr[left]  = arr[i - 1]
    arr[i - 1] = pivot

    # Returns the position of the pivot
    return i - 1
    
# Function: Sort an array around the pivot
def QuickSort(arr, start, end):

    global comparisions

    # base case
    if (end - start) < 1:
        return

    # Choosing pivot method - Here
    
    # partition sub routine
    pivot = Partition(arr, start, end)
    comparisions += (end - start)
    
    # Call recursion
    QuickSort(arr, start, pivot - 1)
    QuickSort(arr, pivot + 1, end)

    return

def RightPivot(arr, left, right):
    temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp

def MedianPivot (arr, left, right):
    a = [0, 0, 0]
    a[0] = arr[left]             # Median of the three pivot
    a[1] = arr[right]
    mid = int ((right - left)/2) + left
    a[2] = arr[mid]
 

    for i in range(3):
        for j in range (i + 1, 3):
            if a[i] > a[j]:
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
    
    if (arr[mid] == a[1]):
        temp   = arr[mid]
        arr[mid] = arr[left]
        arr[left] = temp

    elif (arr[right] == a[1]):
        temp   = arr[right]
        arr[right] = arr[left]
        arr[left] = temp

# Main
file = open("QuickSort.txt")
Array = []
for line in file:
    Array.append(int(line.strip('\n')))

QuickSort(Array, 0, 9999)
print (comparisions)
