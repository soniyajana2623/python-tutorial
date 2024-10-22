a={1:"apple",2:"banana",3:"pineapple",4:"papaya"}
b={5:"watermelon", 6:"melon", 7:"gauva"}
a.update(b)  #update mein add ho jata hai dusra data bhi 
print(a)


# clear mein pura empty ho jayega dict
c={1:"pineapple",2:"papaya",3:"banana"}
# c.clear()
# print(c)
c.popitem()  #last key hatt jata hai
c.pop(1)  #koi bhi ek key hatane ke liye use hota hai
print(c)
del c # del key pura dict ko delete kar deta hai


 