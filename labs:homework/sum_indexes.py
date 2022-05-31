def sum_indexes(arr, arr2):
    arr3 = []
    for x in arr2:        
        if x in arr:
            arr3.append(arr.index(x))
        else:
            arr3.append(-1)
    return sum(arr3)

arr = [1, 12, 2, 4, 6, 8, 9]
arr2 = [100, 2, 9, 3, 7, 134]
print(sum_indexes(arr,arr2))