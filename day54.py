# (a is b)  exact location of object in memory, should be immutable 
# (a == b)  value

a=1
b=1
print(a is b)
print(a == b)

a=[1,2,3]
b=[1,2,3]
print(a is b)   #list can be changed therefore, false
print(a == b)

a="Soniya"
b="Soniya"
print(a is b)
print(a == b)