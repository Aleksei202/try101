print('Lesson_5.1.1')


class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        s = self.x*self.y
        print(f'Area = {s}')


area1 = Rectangle(3, 4)

print('x=', area1.x)
print('y=', area1.y)
area1.area()

