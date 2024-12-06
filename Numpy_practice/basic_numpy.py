'''Arrays are immutable unlike list
if you change the list ie. mix the data type array will convert all the value to that same data
'''

import numpy as np

# 1d array 
list1 = [10, 20, 30, 40, 50]
array1 = np.array(list1,dtype=float) 
print(array1)

# 2d array
list2 = [
    [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]
    ]
array2 = np.array(list2)
print(array2)

#Range given (1d)
array3 = np.arange(1,9)
print(array3)

# Range given (2d)
array4 = np.arange(20,30).reshape((2,5))
print(array4)
