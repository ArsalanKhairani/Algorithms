################################################################################
##                  Copyright(c) Arsalan Khairani, 2014                       ##
##                           Insertion Sort                                   ##
##                                                                            ##
## Sort an array of numbers using Insertion sort.                             ##
## Ref: Page 18 Introduction to Algorithms 3rd Edition                        ##
##      by T.H Cormen, C. E LEISERSON, R.L Rivest, C Stein                    ##
################################################################################

# Function: Given an unsorted array returns a sorted array
def Sort(array):
    n = len(array)
    
    for i in range(1, n):
        key = array[i]
        j = i - 1
        
        while j > 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key

    return array

a = [1, 6, 3, 54, 7, 8, 23, 7323, 6, 3 ,7344, 12346]
print (Sort(a))
