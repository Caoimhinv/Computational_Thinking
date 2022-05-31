# write a function to check if string is a palindrome using recursion

# def isPalindrome(x):
#    leng = len(x)
#    if leng <= 1:
#        return True
#    if x[0] != x[-1]:
#        return False
#    return isPalindrome(x[1:leng-1])

# x = "tattarrattat"
# print(isPalindrome(x))

def isPalindrome(x):
   if len(x) < 2:
       return True
   else:
       return x[0] == x[-1] and isPalindrome(x[1:-1])

print(isPalindrome("hello"))
print(isPalindrome("madam"))
print(isPalindrome("tattarrattat"))