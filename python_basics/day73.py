'''
MAGIC METHOD/DUNDER METHOD
'''


class calculator:
    def __init__(self, base):
        self.base = base

    def __call__(self, x):
        return self.base + x

c = calculator(10)
print(c(5))
