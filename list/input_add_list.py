#Enter names

name_list=[]

n=int(input("No of studenrs"))

for i in range(n):
    name=input("Enter the name :")
    name_list.append(name)

print(name_list)
if "shayan" in name_list:
    print("He is there!!")
else:
    print("He's not there!!")