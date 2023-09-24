import math

from src.Figure import Figure

class Circle(Figure):

    def __init__(self, radius):
        super().__init__()
        self.radius = radius
        self.name = f"Circle {radius}"
        print({self.name})

    def get_area(self):
        return math.pi*(self.radius*self.radius)

    def get_perimeter(self):
        return (2 * math.pi * self.radius)