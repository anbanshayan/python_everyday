#global variable

x = "Easy"

def myfunc():
    global x
    x = "fantastic"
    print("Python is "+x)

myfunc()