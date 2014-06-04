################################################################################
##                  Copyright(c) Arsalan Khairani, 2014                       ##
##                              Merge Sort                                    ##
##                                                                            ##
## Divide and Conquer merge sort algorithm.                                   ##
################################################################################

# Function: Sort the array in two halfs from the mid
def MergeSort(left, right, arr):
    
    # Base case
    if left == right:
        a = []
        a.append(arr[left])
        return a
        
    # Call of left half
    half = int((left + right)/2)
    leftTree = MergeSort (left, half, arr)
    
    # Call on right half
    rightTree = MergeSort (half + 1, right, arr)

    # Call Merge
    sort = Merge(leftTree, rightTree)
    return sort

# Function: Merge two sub arrays
def Merge(leftTree, rightTree):
    i = 0
    j = 0
    arr = []
    
    for k in range(len(leftTree)+len(rightTree)):

        # In case of any one array is fully copied
        if i == len(leftTree):
            arr.append(rightTree[j])
            j += 1
        elif j == len(rightTree):
            arr.append(leftTree[i])
            i+= 1

        # In case both have elements then copy the greates
        elif leftTree[i] > rightTree[j]:
            arr.append(rightTree[j])
            j+= 1
        else:
            arr.append(leftTree[i])
            i+= 1
    return arr

print (MergeSort (0, 4, [3, 4, 5, 6, 1]))
