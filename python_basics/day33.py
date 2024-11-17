dict={
    "Apple": "Fruit",  #apple=key, fruit=value
    "1,2,3": "Numbers",
    "Spoon": "Object"
}
print(dict["Apple"])   #will throw error if key does not exist 
print(dict.get("Apple"))  #there are 2 ways to acess , this will say none if key does not exist

Marks={
    "1": "50/100",  #1=key, 50/100=value
    "2": "60/100",
    "3": "100/100",
    "4": "90/100"
}

print(Marks.values())
print(Marks.keys()) #isme saare keys milega
for keys in Marks.keys():
    print(Marks[keys])
