# write a function to reverse a string using recursion

# def reverseString(x):
#     if len(x) == 0:
#         return x   
#     else:
#         return reverseString(x[1:]) + x[0]

# x = "how's she cutting?"
# print(reverseString(x))
# print(x[1:])
# print(x[0])

def reverse(str):
    if len(str) == 1 or str == "":
        return str   
    else:
        return reverse(str[1:]) + "|" + str[0]

print(reverse("dominic"))
print(reverse("GMIT"))
print(reverse("recursion is hard"))

