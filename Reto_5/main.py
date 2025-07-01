# This is to use the ShapeSingle packpage
#from ShapeSingle.shape import Point, Line, Rectangle, Triangle

# This is to use the ShapeModular packpage
from ShapeModular.point import Point
from ShapeModular.line import Line
from ShapeModular.rectangle import Rectangle
from ShapeModular.triangle import Triangle


if __name__ == "__main__":
    # Example usage Rectangle
    #* Here we create the 4 points of the rectangle.
    p1 = Point(0, 0)
    p2 = Point(3, 0)
    p3 = Point(3, 3)
    p4 = Point(0, 3)
    #* Then we create the edges of the rectangle using the points.
    edge1 = Line(p1, p2)
    edge2 = Line(p2, p3)
    edge3 = Line(p3, p4)
    edge4 = Line(p4, p1)
    #* Finally, we create the rectangle using the points and edges.
    rectangle = Rectangle([p1, p2, p3, p4], [edge1, edge2, edge3, edge4], [90, 90, 90, 90])
    #* Now we can compute the area, perimeter, inner angles and check if the
    #* rectangle is regular.
    print("Area of rectangle:", rectangle.compute_area())
    print("Perimeter of rectangle:", rectangle.compute_perimeter())
    print("Inner angles of rectangle:", rectangle.compute_inner_angles())
    print("Is rectangle regular?", rectangle.is_regular)
    
    # Example usage Triangle
    #* Here we create the 3 points of the triangle.
    p5 = Point(0, 0)
    p6 = Point(1, 0)
    p7 = Point(0.5, (3**0.5)/2)
    #* Then we create the edges of the triangle using the points.
    edge5 = Line(p5, p6)
    edge6 = Line(p6, p7)
    edge7 = Line(p7, p5)
    #* Finally, we create the triangle using the points and edges.
    triangle = Triangle([p5, p6, p7], [edge5, edge6, edge7], [])
    #* Now we can compute the area, perimeter, inner angles and check if the
    #* triangle is regular.
    print("Area of triangle:", triangle.compute_area())
    print("Perimeter of triangle:", triangle.compute_perimeter())
    print("Inner angles of triangle:", triangle.compute_inner_angles())
    print("Is triangle regular?", triangle.is_regular)