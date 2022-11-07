def factorial (x):
    if x < 2:
        int = 1
    else:
        int= x * factorial(x-1)
    return int


for i in range (100):
    value = factorial(i)
    print (f"{i}!= ", value)