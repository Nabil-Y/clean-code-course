class Point:
    def __init__(self, starting_X, starting_Y):
        self.starting_X = starting_X
        self.starting_Y = starting_Y


class Rectangle:
    def __init__(self, starting_point, width, height):
        self.starting_point = starting_point
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def end_points(self):
        bottom_right = self.starting_point.starting_X + self.width
        top_left = self.starting_point.starting_Y + self.height
        print('Starting Point (X)): ' + str(self.starting_point.starting_X))
        print('Starting Point (Y)): ' + str(self.starting_point.starting_Y))
        print('End Point X-Axis (Bottom Right): ' + str(bottom_right))
        print('End Point Y-Axis (Top Left): ' + str(top_left))


def build_new_rectangle():
    main_point = Point(50, 100)
    new_rectangle = Rectangle(main_point, 90, 10)

    return new_rectangle


my_rectangle = build_new_rectangle()

print(my_rectangle.area())
my_rectangle.end_points()