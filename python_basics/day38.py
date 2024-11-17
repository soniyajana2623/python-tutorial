a= int(input("Enter value between 5 and 9:"))
if (a<5 or a>9):
    raise ValueError("The value should be between 5 and 9")
# throw an custom error by using 'raise' method

b=int(input("Enter your age:"))
if (b<18):
    raise ValueError(f"{b} is not a valid age for this movie")


a= (input("Enter value between 5 and 9:"))
if(a=="quit"):
    print("okay")
elif(int(a)<5 or int(a)>9):
    raise ValueError("the value should be between 5 and 9")
    