# |-----------------------------|
# |  Sorting Algorithms module  |
# |-----------------------------|

# ===========
# BUBBLE SORT
# ===========
# adapted from https://runestone.academy/ns/books/published/pythonds/SortSearch/TheBubbleSort.html

def bubbleSort(array):
    # loops through the indexes of the array in reverse
    for x in range(len(array) -1, 0, -1):
        # loops through the range of 'passnum'
        for i in range(x):
            # first time around the loop it compares the first 2 elements and so forth
            if array[i] > array[i+1]: # if 1st element is greater,
                # element 1 is assigned to the variable 'temp'
                temp = array[i]
                # we move on to the next element in the list
                array[i] = array[i + 1]
                # alist[i+1] becomes element stored in temp
                array[i + 1] = temp
                # loop continues with these new values


# ==============
# INSERTION SORT
# ==============
# adapted from https://runestone.academy/ns/books/published/pythonds/SortSearch/TheInsertionSort.html

def insertionSort(array):
    # loops through the list index from index[1] to the end
    for i in range(1, len(array)):
        # first key is index[1] and so forth
        key = array[i]
        # first value of position is 1 and so forth
        position = i
        # while position is greater than zero and array(position-1) is greater than key
        while position > 0 and array[position-1] > key:
            # array[position] becomes array[position-1] - i.e. moves to the left
            array[position] = array[position-1]
            # position decreases by 1, and compares that value to the key in the while loop
            # when position gets back to zero, the while loops finishes and we move on to next index in the for loop
            position = position-1
        # next index becomes key and we return through the for loop again
        array[position] = key

# ==========
# MERGE SORT
# ==========

# adapted from https://runestone.academy/ns/books/published/pythonds/SortSearch/TheMergeSort.html

def mergeSort(array):
    # the first section of the code recursively 'splits' the array
    # sets base case (i.e. continues if array has more than 1 value)
    if len(array) > 1:
        # finds out the mid-point of array (or within 1)
        mid = len(array) // 2
        # splits array into 2 using 'mid' as parameter
        lefthalf = array[:mid]
        righthalf = array[mid:]
        # recursively runs function on split arrays
        mergeSort(lefthalf)
        mergeSort(righthalf)
        # creates temp variables for i, j & k
        i=0
        j=0
        k=0
        # Once the list is broken into arrays of !> 1, we begin the merging.
        # loops until variable i or j become great than
        while i < len(lefthalf) and j < len(righthalf):
            # if first element of 'lefthalf' is less than or equal to first element of righthalf
            if lefthalf[i] <= righthalf[j]:
                # it becomes the first element of array
                array[k]=lefthalf[i]
                # i is augemented by 1 and we loop back
                i=i+1
            else:
                # first element of righthalf array becomes first array of final array
                array[k]=righthalf[j]
                # j augmented by 1
                j = j + 1
            k = k + 1
        # only comes into play when there's 1 element in 'lefthalf'
        # and none in other
        while i < len(lefthalf):
            array[k] = lefthalf[i]
            i = i + 1
            k = k + 1
        # only comes into play when there's 1 element in 'righthalf'
        # and none in other
        while j < len(righthalf):
            array[k] = righthalf[j]
            j = j + 1
            k = k + 1

# ==========
# QUICK SORT
# ==========

# adapted from https://runestone.academy/ns/books/published/pythonds/SortSearch/TheQuickSort.html

def quickSort(array):
    # calls quickSortHelper and sends array, 0 and length of array minus 1
   quickSortHelper(array, 0, len(array) - 1)

# function takes in 3 values from quickSort function
def quickSortHelper(array, first, last):
    # sets base case - if zero is less than array minus 1
    if first < last:
        # calls partition function and sends the 3 values
        # saves result as variable 'splitpoint'
        splitpoint = partition(array, first, last)
        # recursively calls the function
        # continues until base case is satisfied
        quickSortHelper(array, first, splitpoint - 1)
        quickSortHelper(array, splitpoint + 1, last)

# function takes in 3 values from quickSortHelper function
def partition(array, first, last):
    # pivot starts as index[0] of array
    pivot = array[first]
    # leftmark variable set initially to 0 + 1
    leftmark = first + 1
    # rightmark variable set initially to value of array length minus 1
    rightmark = last
    done = False
    while not done:
        # loops from leftmark
        while leftmark <= rightmark and array[leftmark] <= pivot:
            leftmark = leftmark + 1
        # loops back from rightmark
        while array[rightmark] >= pivot and rightmark >= leftmark:
            rightmark = rightmark -1
        # continues until rightmnark 'crosses over' leftmark
        if rightmark < leftmark:
            done = True           
        else:  
            # swaps values at leftmark and rightmark indexes         
            temp = array[leftmark]
            array[leftmark] = array[rightmark]
            array[rightmark] = temp
    temp = array[first]
    array[first] = array[rightmark]
    array[rightmark] = temp
    return rightmark

# ===========
# BUCKET SORT
# ===========

# Adapted from https://www.geeksforgeeks.org/bucket-sort-2/

def bucketSort(array):
    # determines the maximum and minimum values in array
    max_ele = max(array)
    min_ele = min(array)
    # defines the number of buckets. This can be changed as appropriate
    buckets = 10 
    # determines range for buckets
    rnge = (max_ele - min_ele) / buckets   
    # create empty array to append to
    temp = [] 
    # create empty buckets (arrays) inside temp array
    for i in range(buckets):
        temp.append([]) 
    # divide the array elements
    # into the correct bucket
    # loops through each element of array
    for i in range(len(array)):
        # element 1 minus the mimumum element divided by rnge
        # minus int version of the same calculation
        diff = (array[i] - min_ele) / rnge - int((array[i] - min_ele) / rnge) 
        # append the boundary elements to the lower array
        # if result of above calculation is equal to zero and
        # array element is not equal to the lowest value,
        # it's appended to the array at last index position. 
        # i.e. this finds the highest value
        if(diff == 0 and array[i] != min_ele):
            temp[int((array[i] - min_ele) / rnge) - 1].append(array[i])
        # otherwise this calculates the appropriate index position for each value
        else:
            temp[int((array[i] - min_ele) / rnge)].append(array[i])
    # Sort each bucket individually using built-in sort() function
    # which is actually timsort. Could equally be any other comparison based sorting algorithm
    for i in range(len(temp)):
        if len(temp[i]) != 0:
            temp[i].sort() 
    # Gather sorted elements
    # to the original array
    k = 0
    for lst in temp:
        if lst:
            for i in lst:
                array[k] = i
                k = k+1