a=5   #global variable
print(a)

def hello():
    a=10  #local variable
    print(f"The local a is {a}")   #"local" means function ke andar wala variable, can not be used outside the function
    print("hello world")           # "Global" means function ke bahar wala variable, jo function ke and bhi use kar sakte hai


print(f"The global1 a is {a}")
hello()
print(f"The global a is {a}")
