def divisble5(n):
    if(n%5 == 0):
        return True
    return False

a = [1,5,67,89,90,76,45,67,45,80,69,55]
b = list(filter(divisble5, a))
print(b)