# a=(input("Enter the number:"))
# print(f"Multiplication of number {a} is:")

# #try mein we can try code if there is an error it will show but the remaining code will still execute
# try:
#     for i in range(1,11):
#         print(f"{int(a)}x{int(i)}={int(a*i)}")
# except:
#     print("There is an error") 



# print("My name is soniya")
# print("I am 21 years old")

try:
    num=int(input("enter the number:"))
    a=[2,3,4]
    print(a[num])
except ValueError:
    print("The value given is not an integer")
except IndexError:
    print("Index error!")
