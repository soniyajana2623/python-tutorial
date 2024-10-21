s1={1,2,4,5,6}
s2={3,4,6,7}
print (s1.union(s2)) #union is merging 2 sets
print(s1.intersection(s2)) #intersection is common value in set 
print(s1.symmetric_difference(s2)) #symmetric diff matlab jo value common nahi hai
print(s1.difference(s2))  #isme s1-s2 hota hai 

# pop function mein koi bhi value nikal sakta hai...there is no chnace ki specific value nikalega
set1={"Mumbai","Delhi","Pune","Kolkata"}
set2={"Jaipur","Hyderabad","Nagpur"}
set3={"Agra","Lucknow","Surat"}
a=set1.pop()
b=set2.pop()
print(set1)
print(a)
print(set2)
print(b)


# del function mein pura set delete hota hai
del set2

# clear function mein set reh jaata hai just uska value clear ho jata hai...end up in empty set
set3.clear()
print(set3)

# to check if there is value toh in use karna hai
if "Mumbai" in set3:
    print("Yes Mumbai is there")
else:
    print("Mumbai is not there")