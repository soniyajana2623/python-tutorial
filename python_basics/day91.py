'''
Genrator:
Instead of generating and storing all items at once (like a list does), a generator produces items
one at a time and only when they are needed, making it useful for handling large datasets or 
continuous data streams.
Doesn't store values in memory
'''

def my_genrator():
    for i in range(5):
        yield i
gen= my_genrator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

for g in gen:
    print(g)