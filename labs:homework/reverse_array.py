# write a function to reverse an array using recursion

def reverseArray(x):
    if len(x) == 0:
        return []   
    else:
        return [x[-1]] + reverseArray(x[:-1])

x = (1,3,5,7,9)
print(reverseArray(x))

 
