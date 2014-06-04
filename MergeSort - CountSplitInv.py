################################################################################
##                  Copyright(c) Arsalan Khairani, 2014                       ##
##                              Merge Sort                                    ##
##                                                                            ##
## Divide and Conquer merge sort algorithm. Integer to store inversions.      ##
## File Input: Unordered Integer 1 to 10000                                   ##
################################################################################

def MergeSort(left, right, arr):
    
    # Base case
    if left == right:
        a = []
        a.append(arr[left])
        return [a, 0]
        
    # Call of left half
    half = int((left + right)/2)
    leftTreeAndInversions = MergeSort (left, half, arr)
    
    # Call on right half
    rightTreeAndInversions = MergeSort (half + 1, right, arr)

    # Call Merge
    sortAndSplitInv = Merge_CountSplitInv(leftTreeAndInversions[0], rightTreeAndInversions[0])

    # Add inversions
    sortAndSplitInv[1] += leftTreeAndInversions[1] + rightTreeAndInversions[1]
    
    return sortAndSplitInv

def Merge_CountSplitInv(leftTree, rightTree):
    i = 0
    j = 0
    arr = []
    splitInversions = 0
    for k in range(len(leftTree)+len(rightTree)):

        # In case of any one array is fully copied
        if i == len(leftTree):
            arr.append(rightTree[j])
            j += 1

        elif j == len(rightTree):
            arr.append(leftTree[i])
            i+= 1

        # In case both have elements then copy the greatest
        elif leftTree[i] > rightTree[j]:
            arr.append(rightTree[j])

            # Counting split inversion
            splitInversions += (len(leftTree) - i)
            
            j+= 1
            
        else:
            arr.append(leftTree[i])
            i+= 1
            
    return [arr, splitInversions]

file = open("IntegerArray.txt")
Array = []
for line in file:
    Array.append(int(line.strip('\n')))
s = MergeSort (0, 99999, Array)
print (s[1])
