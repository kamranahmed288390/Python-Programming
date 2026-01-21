class Vector:
    def __init__(self, values):
        self.values = values

    def __add__(self, v2):
        result = []
        for i in range(len(self.values)):
            result.append(self.values[i] + v2.values[i])
        return Vector(result)

    def __mul__(self, v2):
        dot_product = 0
        for i in range(len(self.values)):
            dot_product += self.values[i] * v2.values[i]
        return dot_product

    def __str__(self):
        return str(self.values)


v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

print(v1 + v2)   # [5, 7, 9]
print(v1 * v2)   # 32
