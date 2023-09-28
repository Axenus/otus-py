import math

from src.Figure import Figure


class Triangle(Figure):


    def __init__(self, side_a, side_b, side_c):
        super().__init__()
        if not (side_a + side_b > side_c and side_b + side_c > side_a and side_c + side_a > side_b):
            raise ValueError("Triangle with given sides does not exist")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.name = f"Triangle {side_a},{side_b},{side_c}"
        print({self.name})

    @property
    def get_area(self):
        s = (self.side_a + self.side_b + self.side_c) / 2
        area = math.sqrt(s*(s-self.side_a)*(s-self.side_b)*(s-self.side_c))
        return area

    @property
    def get_perimeter(self):
        return (self.side_a+self.side_b+self.side_c)



