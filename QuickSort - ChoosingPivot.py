# This is the programming question to find the total no of comparisions

comparisions = 0

def Partition(arr, left, right):

    #pivot = arr[left]           # Make the first element from left the pivot

    #pivot = arr[right]          # Make the last element the pivot
    #temp = arr[left]            # Exchange first element to the last element
    #arr[left] = arr[right]
    #arr[right] = temp

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


# Main
file = open("QuickSort.txt")
Array = []
for line in file:
    Array.append(int(line.strip('\n')))

QuickSort(Array, 0, 9999)
print (comparisions)

# first as pivot 162085
# last as pivot 164123
# Median as pivot 138382
