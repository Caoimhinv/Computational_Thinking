# write a function to check if element is in array using recursion

def elemIn(list, num):
  if len(list) == 0:
    return False
  if list[0] == num:
    return True
  return elemIn(list[1:], num)
  
arr1 = [42, 12, 21, 30]
arr2 = [12, 30, 45]
print(elemIn(arr1, arr2))


a = [1, 2, 3]
b = [2, 7]
result = []
for x in a:
   result.append(x in b)
print result

# def linear_search(arr, target, index):
#   if arr[index] == target:
#     return True
#   elif index == 0:
#     return False
#   else:
#     return linear_search(arr, target, index-1)

# def search(arr, target):
#   return linear_search(arr, target, len(arr)-1)

# print(search([1,2,3,4], 2))
# print(search([1,2,3,4], 199))
# print(search([1,2,3,4], 1))
