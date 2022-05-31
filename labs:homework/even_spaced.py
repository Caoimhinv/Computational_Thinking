def even_spaced(a,b,c):
    arr = [a,b,c]
    hi = max(arr)
    lo = min(arr)
    arr.remove(hi)
    arr.remove(lo)
    if (hi - arr[0]) == (arr[0] - lo):
        print ("True")
    else:
        print ("False")
    return


even_spaced (12, 3, 6)
# x = 1
# y = 2
# z = 3

# arr = [x,y,z]
# arr.remove(x)
# # print (min(arr))
# print (arr)
