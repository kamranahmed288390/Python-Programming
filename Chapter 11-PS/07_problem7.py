class Vector:
    def __init__(self, values):
        self.values = values # must be 3 values

    def __add__(self,v2):
        result = []
        for i in range(len(self.values)):
            result.append(self.values[i] + v2.values[i])
        return Vector(result)
        
    def __mul__(self,v2):
        dot_product = 0
        for i in range(len(self.values)):
            dot_product += self.values[i] * v2.values[i]
        return dot_product
    
    def __str__(self):
        return f"{self.values[0]}i + {self.values[1]}j + {self.values[2]}k"
    
    def __len__(self):
        return len(self.values) 
    
v1 = Vector([7,8,10])
v2 = Vector([1,2,3])

print(v1)
print(v1 + v2)
print(v1 * v2)
print(len(v1))


