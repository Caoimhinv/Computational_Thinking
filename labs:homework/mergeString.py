# # def merge(string, string2):

# def merge(A, B):
#     if len(A) > 0:
#         return str(A[0]) + str(B[0]) + merge(A[1:], B[1:])
#     else:
#         return ''

# print(merge("dmnc", "oii"))
# print(merge("what is love", "LOL"))

def merge(string, string2, answer=''):
    if not string:
        return answer + string2
    if not string2:
        return answer + string
    return merge(string[1:], string2[1:], answer + string[0] + string2[0])

print(merge("dmnc", "oii"))
print(merge("what is love", "LOL"))