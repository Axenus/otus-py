from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle
import pytest

def test_add_area():
    r = Rectangle(2, 5)
    s = Square(10)
    c = Circle(10)
    x = Triangle(side_a=4,side_b=4,side_c=4)
    assert r.add_area(r) == 20
    assert s.add_area(s) == 200
    assert x.add_area(x) == 13.856406460551018


# def test_add_area_negative():
#    r = Rectangle(2, 5)
#    s = Square(10)
#    c = Circle(10)
#    x = Triangle(side_a=4, side_b=4, side_c=7)
#    assert r.add_area(r) == 25
#    assert s.add_area(s) == 201
#    assert x.add_area(x) == 13.856406460551017

# Rectangle
@pytest.mark.parametrize(("side_a", "side_b", "area", "perimeter"),
                         [(2, 5, 10, 14)])
def test_rectangle(side_a, side_b, area, perimeter):
    r = Rectangle(side_a=2, side_b=5)
    assert r.name == f"Rectangle {side_a} and {side_b}"
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter



@pytest.mark.parametrize(("side_a", "side_b", "area", "perimeter"),
                         [(-2, -5, -10, -14)])
def test_rectangle_negative(side_a, side_b, area, perimeter):
    r = Rectangle(side_a=2, side_b=5)
    assert r.name == f"Rectangle {side_a} and {side_b}"
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter

# Square
@pytest.mark.parametrize(("side_a", "area", "perimeter"),
                         [(2, 4, 8)])
def test_square(side_a, area, perimeter):
    s = Square(side_a)
    assert s.name == f"Square {side_a}"
    assert s.get_area() == area
    assert s.get_perimeter() == perimeter



@pytest.mark.parametrize(("side_a", "area", "perimeter"),
                         [(-2, -4, -8)])
def test_square_negative(side_a, area, perimeter):
    s = Square(side_a)
    assert s.name == f"Square {side_a}"
    assert s.get_area() == area
    assert s.get_perimeter() == perimeter



# Circle
@pytest.mark.parametrize(("side_a", "area", "perimeter"),[(2, 12.566370614359172, 12.566370614359172)])
def test_circle(side_a, area, perimeter):
    c = Circle(side_a)
    assert c.name == f"Circle {side_a}"
    assert c.get_area() == area
    assert c.get_perimeter() == perimeter


@pytest.mark.parametrize(("side_a", "area", "perimeter"),[(3, 3, 3)])
def test_circle_negative(side_a, area, perimeter):
    c = Circle(side_a)
    assert c.name == f"Circle {side_a}"
    assert c.get_area() == area
    assert c.get_perimeter() == perimeter





# Triangle
@pytest.mark.parametrize(("side_a","side_b", "side_c", "area", "perimeter"),[(4, 5, 7, 9.797958971132712, 16)])
def test_triangle(side_a, side_b, side_c, area, perimeter):
    x = Triangle(side_a, side_b, side_c)
    assert x.name == f"Triangle {side_a},{side_b},{side_c}"
    assert x.get_area() == area
    assert x.get_perimeter() == perimeter


@pytest.mark.parametrize(("side_a","side_b", "side_c", "area", "perimeter"),[(4, 6, 7, 8, 16)])
def test_triangle_negative(side_a, side_b, side_c, area, perimeter):
    x = Triangle(side_a, side_b, side_c)
    assert x.name == f"Triangle {side_a},{side_b},{side_c}"
    assert x.get_area() == area
    assert x.get_perimeter() == perimeter