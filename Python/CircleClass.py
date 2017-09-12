# Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle
import math


class Circle:

    def __init__(self, in_radius):
        self.radius = in_radius
        self.area = None

    def calc_area(self):
        self.area = math.pi*self.radius**2
        print('Area of circle is {}'.format(self.area))

    def calc_perimeter(self):
        self.perimeter = self.radius*2*math.pi
        print('Perimeter of circle is {}'.format(self.perimeter))

my_circ = Circle(9)
my_circ.calc_area()
my_circ.calc_perimeter()