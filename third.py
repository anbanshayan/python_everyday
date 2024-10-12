txt = "welcome"


count = 0


for i in range(len(txt)):
    if txt[i] in 'aeiou':
        count = count + 1

print(count)
