import os
if(not os.path.exists("data")):
    os.mkdir("data")
for i in range(1,10):
    os.mkdir(f"data/day {i}")  #new files
    os.rename(f"data/day {i}", f"data/Tutorial {i}")  #to rename
