import time
def usingwhile():
    i=0
    while i<50000:
        i= i+1
        print(i)

def usingfor():
    for i in range(50000):
        print(i)

init= time.time()
usingwhile()
t1=(time.time()-init)

init= time.time()
usingfor()
t2=(time.time()-init)

print(f"Using while loop time: {t1}")
print(f"Using for loop time: {t2}")





'''
Sleep: Printed after sometime
'''
print(5)
time.sleep(5)
print("This is printed after 5 sec")



'''
strf time
'''
t= time.localtime()
formatted_time= time.strftime("%Y-%m-%d, %H:%M:%S",t)
print(formatted_time)