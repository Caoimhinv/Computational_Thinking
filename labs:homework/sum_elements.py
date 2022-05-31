# write a function to calculate sum of elements in array using recursion

def sumElem(array):
   if len(array) == 1:
        return array[0]
   else:
        return array[0] - sumElem(array[1:])

x = [1,2,3,4,5,6]
print(sumElem(x))