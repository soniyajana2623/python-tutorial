''' 
Walrus operator:
assings values to variables as part of a larger expression
'''

# num=[1,2,3,4,5]
# while(n := len(num)) >1:
#     print(num.pop())



# foods= list()
# while True:
#     food= input("What food do you like?:")
#     if food == "quit":
#         break
#     foods.append(food)
# print(foods)



foods=list()
while (food := input("What food do you like?:")) !="quit":   #!= not equal to
    foods.append(food)