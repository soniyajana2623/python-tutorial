# f=open('main.txt','r')
# i= 0
# while True:
#     i= i+1
#     line= f.readline()
#     if not line:
#         break
#     m1= line.split(",")[0]   
#     m2= line.split(",")[1]   
#     m3= line.split(",")[2]  
#     m4= line.split(",")[3]  
      
#     print(f"The marks of student {i} is {m1}")
#     print(f"The marks of student {i} is {m2}")
#     print(f"The marks of student {i} is {m3}")
#     print(f"The marks of student {i} is {m4}")
   
#     print(line)




# write 
f=open('main2.txt','w')
lines=('line 1\n', 'line 2\n', 'line 3\n', 'line 4\n')
f.writelines(lines)
f.close()



