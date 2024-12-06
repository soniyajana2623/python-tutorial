f= open('day42.py','r')    
a=f.read()   #this function will show us the content written on the file which you want
print(a)
f.close()



'''
r = open file for reading 
w = write, means to overwrite in the file, if no such file is there it will create it
a = append, means to add new content in existing file
x = create, create a new file and open it for writng 
t = text, means open in text form
+ = open a disk file for updating(reading and writing)
'''
