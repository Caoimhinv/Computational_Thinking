# def score_diff(arr):
#     new_list = []
#     for x in arr:
#         if 


arr = [2,4,6]
arr2 = [12,13,15,17,21,30]
arr3 = []
for x in reversed(arr2):
    arr3.append(x)
print (arr3)
arr4 = []
# for i in range(len(arr3)):
#     arr3[i] = arr3[i] - (i[i+1])
# print(arr3)
# print (reversed(arr))
# score_diff(arr)

def reverseArray(x):
    new = []
    if len(x) == 0:
        return []   
    else:
        new.append([x[0]] - reverseArray(x[1]))
        print(new)

x = [12,13,15,17,21,30]
print(reverseArray(x))