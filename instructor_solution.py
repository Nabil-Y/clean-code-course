# Refactor this code

class Point:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y


class Rectangle:
    def __init__(self, origin, width, height):
        self.origin = origin
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def print_coordinates(self):
        top_right = self.origin.X + self.width
        bottom_left = self.origin.Y + self.height
        print('Starting Point (X)): ' + str(self.origin.X))
        print('Starting Point (Y)): ' + str(self.origin.Y))
        print('End Point X-Axis (Top Right): ' + str(top_right))
        print('End Point Y-Axis (Bottom Left): ' + str(bottom_left))


def build_rectangle():
    rectangle_origin = Point(50, 100)
    rectangle = Rectangle(rectangle_origin, 90, 10)

    return rectangle


rectangle = build_rectangle()

print(rectangle.get_area())
rectangle.print_coordinates()