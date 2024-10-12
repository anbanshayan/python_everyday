x = lambda a,b:a+b
print(x(5,4))

#lambda function
def myFunc(n):
    return lambda a:a*n

myTriple = myFunc(8)
myDouble = myFunc(2)

print(myTriple(3))
print(myDouble(5))