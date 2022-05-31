# write a function to compute result of a given number raised to a 
# given power using recursion

def powerOf(x, y):
    if(y == 1):
        return(x)
    if(y != 1):
        return(x * powerOf(x, y-1))
x = 3
y = 4
print(powerOf(x, y))