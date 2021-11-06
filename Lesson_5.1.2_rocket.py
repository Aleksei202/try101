print('Lesson_5.1.2')


class Rocket:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_up(self):
        self.y = self.y + 1
        print(self.x, ',', self.y)

    def move_right(self):
        self.x = self.x + 1
        print(self.x, ',', self.y)

    def move_down(self):
        self.y = self.y - 1
        print(self.x, ',', self.y)

    def move_left(self):
        self.x = self.x - 1
        print(self.x, ',', self.y)

    def current_position(self):
        print('Current position is', self.x,',', self.y)


rocket1 = Rocket()
rocket1.move_up()
rocket1.move_up()
rocket1.move_right()
rocket1.move_down()
rocket1.move_left()
rocket1.current_position()
