#But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking"

fruits=("apple","banana","grapes","papaw")

(green,yellow,pink,red) = fruits

print(green)
print(yellow)
print(red)
print(pink)

vegetables = ("brinjal","tomato","potato","pumpkin","bitter guard","beetroot")

(green,red,*tropic,pink) = vegetables

print(green)
print(red)
print(tropic)
print(pink)