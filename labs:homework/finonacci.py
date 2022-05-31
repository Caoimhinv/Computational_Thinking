# write a function to calculate Nth number in fibonacci sequence

def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return fib(n-1) + fib(n-2)

x = 10
print(fib(x))