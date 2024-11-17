import os
if(not os.path.exists("Exercise")):
    os.mkdir("Exercise")
for i in range (1,11):
    os.mkdir(f"Exercise/day {i}")
    os.rename(f"Exercise/day {i}",f"Exercise/{i}.png")


