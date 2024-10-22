for i in range(1,11):
    print(i)
else:
    print("End")

for i in range(5):
    print(i)
    if (i==3):
        break
else:
    print("End")  #isme loop break hua isliye else execute nahi hua, else execute tab hota hai jab range pura khatam ho

for x in range(5):
    print("iteration no {} in for loop".format(x + 1))
else:
    print("else block in loop")
print("Out of loop")
