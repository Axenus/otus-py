from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle
import pytest



# Rectangle
@pytest.mark.parametrize(("side_a", "side_b", "area", "perimeter"),
                         [(2, 5, 10, 14)])
def test_rectangle(side_a, side_b, area, perimeter):
    r = Rectangle(side_a, side_b)
    assert r.name == f"Rectangle {side_a} and {side_b}"
    assert r.get_area == area
    assert r.get_perimeter == perimeter

#NegativeRectangle
@pytest.mark.parametrize(("side_a", "side_b", "area", "perimeter"),
                         [(0, 0, 0, 0)])
def test_rectangle_negativ(side_a, side_b, area, perimeter):

  with pytest.raises(ValueError):
    r = Rectangle(side_a, side_b)
    assert r.name == f"Rectangle Can't create {side_a} and {side_b}"



# Square
@pytest.mark.parametrize(("side_a", "area", "perimeter"),
                         [(2, 4, 8)])
def test_square(side_a, area, perimeter):
    s = Square(side_a)
    assert s.name == f"Square {side_a}"
    assert s.get_area == area
    assert s.get_perimeter == perimeter


#Square_Negativ
@pytest.mark.parametrize(("side_a", "area", "perimeter"),
                         [(0, 0, 0)])
def test_square_negative(side_a, area, perimeter):
    with pytest.raises(ValueError):
        s = Square(side_a)
        assert s.name == f"Square {side_a}"




# Circle
@pytest.mark.parametrize(("side_a", "area", "perimeter"),[(2, 12.566370614359172, 12.566370614359172)])
def test_circle(side_a, area, perimeter):
    c = Circle(side_a)
    assert c.name == f"Circle {side_a}"
    assert c.get_area() == area
    assert c.get_perimeter() == perimeter

# CircleNegativ
@pytest.mark.parametrize(("side_a", "area", "perimeter"),[(0, 0, 0)])
def test_circle_negative(side_a, area, perimeter):
    with pytest.raises(ValueError):
        c = Circle(side_a)
        assert c.name == f"Circle {side_a}"



# Triangle
@pytest.mark.parametrize(("side_a","side_b", "side_c", "area", "perimeter"),[(4, 5, 7, 9.797958971132712, 16)])
def test_triangle(side_a, side_b, side_c, area, perimeter):
    x = Triangle(side_a, side_b, side_c)
    assert x.name == f"Triangle {side_a},{side_b},{side_c}"
    assert x.get_area() == area
    assert x.get_perimeter() == perimeter

# TriangleNegativ
@pytest.mark.parametrize(("side_a","side_b", "side_c", "area", "perimeter"),[(0, 0, 0, 0, 0)])
def test_triangle_negative(side_a, side_b, side_c, area, perimeter):
    with pytest.raises(ValueError):
        x = Triangle(side_a, side_b, side_c)
        assert x.name == f"Triangle {side_a},{side_b},{side_c}"