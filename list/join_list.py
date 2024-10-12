#joining list
num1=[78,85,96,35,72,41,32,14,89,96]
num2=[45,85,96,12]

num3=num1+num2
print(num3)

num1.extend(num2)
print(num1)

for x in num2:
    num1.append(x)

print(num1)