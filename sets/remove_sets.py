#remove elemnts from set
num = {45,96,85,74,25,16,95}

num2 = {45,96,85,74,25,16,95}

#To remove an item in a set, use the remove(), or the discard() method.

num.remove(16)
print(num)

num.discard(45)
print(num)

#Remove a random item by using the pop() method:
x = num.pop()
print(x)

#The clear() method empties the set:
num.clear()
print(num)