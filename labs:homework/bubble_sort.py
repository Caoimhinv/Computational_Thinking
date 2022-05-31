# def bubbleSort(arr):
#     n = len(arr)
 
#     # Traverse through all array elements
#     for i in range(n-1):
#     # range(n) also work but outer loop will
#     # repeat one time more than needed.
 
#         # Last i elements are already in place
#         for j in range(0, n-i-1):
 
#             # traverse the array from 0 to n-i-1
#             # Swap if the element found is greater
#             # than the next element
#             if arr[j] > arr[j + 1] :
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
 
# # Driver code to test above
# arr = [64, 34, 25, 12, 22, 11, 90]
 
# bubbleSort(arr)
 
# print ("Sorted array is:")
# for i in range(len(arr)):
#     print ("% d" % arr[i],end=" ")

# def bubblesort(elements):
#   # Looping from size of array from last index[-1] to index [0]
#   for n in range(len(elements)-1, 0, -1):
#     for i in range(n):
#       if elements[i] > elements[i + 1]:
#         # swapping data if the element is less than next element in the array
#         elements[i], elements[i + 1] = elements[i + 1], elements[i]
# elements = [64, 34, 25, 12, 22, 11, 90]
  
# print("Unsorted list is,") 
# print( elements)
# bubblesort(elements)
# print("Sorted Array is, ")
# print(elements)

# Bubble sort in Python

def sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr


data = [64, 34, 11, 456, 12, 11, -10]
data2 = [64, 34, 25, 12, 22, 11, 90]
data3 = [8,6,4,345,7676,1,3]

print(sort(data2))

# print('Sorted Array in Ascending Order:')
# print(data)