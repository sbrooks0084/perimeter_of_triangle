class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Triangle:
    def __init__(self, a: Point, b: Point, c: Point):
        self.a = a
        self.b = b
        self.c = c


def triangle_perimeter(triangle: Triangle) -> float:
    side_ab = ((triangle.b.x - triangle.a.x)**2 + (triangle.b.y - triangle.a.y)**2)**0.5
    side_bc = ((triangle.c.x - triangle.b.x)**2 + (triangle.c.y - triangle.b.y)**2)**0.5
    side_ca = ((triangle.c.x - triangle.a.x)**2 + (triangle.c.y - triangle.a.y)**2)**0.5

    return round(side_ab + side_bc + side_ca, 6)


a = Point(10, 10)
b = Point(40, 10)
c = Point(10, 50)
triangle = Triangle(a, b, c)
perimeter = triangle_perimeter(triangle)
print(f"This triangle has a perimeter of {perimeter}")

