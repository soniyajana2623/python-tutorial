'''
STATIC METHOD:
'''


class formula():
    @staticmethod
    def add(a,b):
        return ((a+b)*2 - (2*a*b))

result=formula.add(2,3)
print(result)