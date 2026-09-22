from cmath import sqrt


class Vector():

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"X: {self.x}. Y: {self.y}"

    def get_magnitude(self):
        return sqrt(self.x**2 + self.y**2)


obj1 = Vector(1,2)
print(obj1)
print(obj1.get_magnitude())