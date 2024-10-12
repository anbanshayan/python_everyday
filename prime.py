#Finding prime number

i=int(input("Enter a number : "))

count = 0

for j in range(1,i+1):
    if i % j ==0:
        count = count+1

if count == 2:
    print("Prime number")
else:
    print("Not a prime number")

