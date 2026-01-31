from functools import reduce

l = [111, 23, 876, 9876, 900, 52 ,34,2,45,67,90]

def greater(a,b):
    if a>b:
        return a
    return b

print(reduce(greater, l))