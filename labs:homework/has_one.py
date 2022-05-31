# def has_one(x):
#     list1 = [int(i) for i in list(x)]
#     print(list1)

# has_one(123456)    
# list1 = [int(i) for i in list(s)]
# print(list1)

# L = [1]
# j = 0
# nL = [0, 0, 0, 0, 0, 0, 0, 0, 0]
# n = 12345 #number
# while n:
#     i = n%5
#     nL[i] = 1
#     n //= 10

# x = 234958439
# print(x%10)
# print(x//10)

def countDigit(n):
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return count

def has_one(n):
    # if countDigit(n) == 0:
        # print ("False")
        # return ""
    if n % 10 == 1:
        print ("True")
    else:
        while n >= 10:
            n = n / 10
            has_one(n)

n = 3232781771
has_one(n)
# 
# 
# 
# n = 123456
# print(countDigit(n))
