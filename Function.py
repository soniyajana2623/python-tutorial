def gmean(a,b):
    mean=(a*b)/(a+b)
    print(mean)
def isgreater(a,b):
    if(a>b):
        print("First number is greater")
    elif(a<b):
        print("Secont number is greater")
    else:
        print("both number is equal")


a=3
b=6
c=2
d=9
e=7
f=1

gmean(a,f)
isgreater(a,f)

gmean(a,a)
isgreater(a,a)

gmean(a,b)
isgreater(a,b)