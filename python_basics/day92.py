from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n*5


print("Multiplication table of 5" )
print(f"5 x 1 = {fx(1)} ")
print(f"5 x 2 = {fx(2)}")
print(f"5 x 3 = {fx(3)}")
print(f"5 x 4 = {fx(4)}")
print(f"5 x 5 = {fx(5)}")
# print(f"5 x 6 = {fx(6)}")
# print(f"5 x 7 = {fx(7)}")
# print(f"5 x 8 = {fx(8)}")
# print(f"5 x 9 = {fx(9)}")
# print(f"5 x 10 = {fx(10)}")

print(f"5 x 1 = {fx(1)} ")
print(f"5 x 2 = {fx(2)}")
print(f"5 x 3 = {fx(3)}")
print(f"5 x 4 = {fx(4)}")
print(f"5 x 5 = {fx(5)}")
