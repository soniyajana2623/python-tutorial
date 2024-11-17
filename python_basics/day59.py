# DECORATORS(TO MODIFY THE FUCNTION) 
# function that takes another function as an argument and return a function
def decorate(func):
    def fx(*args,**kwargs):
        print("Good Morning")  #Start
        func(*args,**kwargs)
        print("Thanks for using this function")  #end
    return fx
@decorate
def hello():    #original function
    print("Hello world")

@decorate
def add(a,b):     #original function
    print(a+b)

hello()
add(2,1)   

