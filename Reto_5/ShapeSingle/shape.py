import math

# We start creating the class Point, which inherit from the class Line, this
# class have two attributes x and y, which be the coordinates of the point.
class Point:
    #* Initializing the attributes x and y
    def __init__(self, x, y):
        #* Here we check if the coordinates x and y are numbers (int or float).
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("The coordinates must be numbers (int or float).")
        
        self.x = x
        self.y = y
    #* Here we define a method to compute the distance between two points
    def compute_distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

# Now we create the class Line, which have two attributes start and end,
# which be instances of the Point class. This class also have a metod that
# using the compute_distance method of the Point class, calculate the
# length of the line.
class Line:
    def __init__(self, start, end):
        #* Here we check if the start and end points are instances of the Point
        #* class.
        if not isinstance(start, Point) or not isinstance(end, Point):
            raise TypeError("The start and end points must be instances of the " 
            "Point class.")
        
        self.start = start
        self.end = end
        self.length = start.compute_distance(end)

# Here we have the base class Figure, which will inhirit to all the other
# classes that represent specific figures.
class Figure:
    #* Initializing the attributes vertices, edges and inner_angles
    #* The vertices are a list of Point objects, edges are a list of Line objects
    #* and inner_angles is a list of angles in degrees.
    def __init__(self, vertices, edges, inner_angles):
        #* Here we check if the vertices, edges and inner_angles are of his 
        #* respective types.
        if not isinstance(vertices, list) or not all(isinstance(v, Point) for 
        v in vertices):
            raise TypeError("vertices have to be a list of Point instances.")
        
        if not isinstance(edges, list) or not all(isinstance(e, Line) for e in
         edges):
            raise TypeError("edges have to be a list of Line instances.")
        
        if not isinstance(inner_angles, list) or not all(isinstance(a, 
        (int, float)) for a in inner_angles):
            raise TypeError("inner_angles have to be a list of numbers"
            " (int or float).")

        #* Here we check if the figure is regular, which means that all edges
        #* have the same length. If they don't, we set is_regular to False.
        self.is_regular = True
        for i in range(1, len(edges)):
            if edges[i].length != edges[i-1].length:
                self.is_regular = False
                break
        self.vertices = vertices
        self.edges = edges
        self.inner_angles = inner_angles
        
    #* Here we define the methods that will be implemented in the subclasses
    def compute_area(self):
        pass
    def compute_perimeter(self):
        pass
    def compute_inner_angles(self):
        pass


#* Now we create the Rectangle class, which inherits from Figure.
class Rectangle(Figure):
    #* Intializing with the same parameters as Figure.
    def __init__(self, vertices, edges, inner_angles):
        super().__init__(vertices, edges, inner_angles)

    #* Here we define the method to compute the area of the rectangle, the area
    #* is computed as length * width. To do this, first we check if the
    #* rectangle has 4 vertices.
    def compute_area(self):
        if len(self.vertices) == 4:
            length = self.edges[0].length
            width = self.edges[3].length
            return length * width
        return None
    
    #* Here we define the method to compute the perimeter of the rectangle,
    #* which is the sum of the lengths of all edges. Again, we check if the 
    #* rectangle has 4 vertices.
    def compute_perimeter(self):
        if len(self.vertices) == 4:
            return sum(edges.length for edges in self.edges)
        return None
    
    #* Finally, we define the method to compute the inner angles of the
    #* rectangle, which are always 90 degrees for a rectangle. We check if the
    #* rectangle has 4 vertices and return a list of 90 degrees for each angle.
    def compute_inner_angles(self):
        if len(self.vertices) == 4:
            return [90] * 4
    
#* Now we create the Square class, which inherits from Rectangle.
class Square(Rectangle):

    #* The Square class is initialized with the same parameters as Rectangle.
    #* Besides, we dont need to redefine the methods for area, perimeter, and
    #* inner angles.
    def __init__(self, vertices, edges, inner_angles):
        super().__init__(vertices, edges, inner_angles)

#* Now we create the Triangle class, which also inherits from Figure.
class Triangle(Figure):

    #* Initializing the Triangle class with the same parameters as Figure.
    def __init__(self, vertices, edges, inner_angles):
        super().__init__(vertices, edges, inner_angles)

    #* Here we compute the area of the triangle using Heron's formula.
    def compute_area(self):
        if len(self.vertices) == 3:
            a = self.edges[0].length
            b = self.edges[1].length
            c = self.edges[2].length
            s = (a + b + c) / 2
            return (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return None
    
    #* Here we compute the perimeter of the triangle, which is the sum of the
    #* lengths of all edges. We check if the triangle has 3 vertices.
    def compute_perimeter(self):
        if len(self.vertices) == 3:
            return sum(edge.length for edge in self.edges)
        return None
    
    #* Here we compute the inner angles of the triangle. If the triangle is
    #* regular, we return a list of 60 degrees for each angle. If not, we use
    #* the cosine rule to calculate the angles based on the lengths of the 
    #* edges.
    def compute_inner_angles(self):
        if len(self.vertices) == 3:
            if self.is_regular:
                return [60] * 3
            else:
                a = self.edges[0].length
                b = self.edges[1].length
                c = self.edges[2].length
                angle_A = (b**2 + c**2 - a**2) / (2 * b * c)
                angle_B = (a**2 + c**2 - b**2) / (2 * a * c)
                angle_C = (a**2 + b**2 - c**2) / (2 * a * b)
                #* We use the ValueError and ZeroDivisionError exceptions to handle
                #* cases where the lengths of the edges are 0 or the triangle
                #* cannot be formed with the given lengths. Besides, we use
                #* TypeError to handle cases where the lengths are not numbers.
                try:
                    angle_A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
                    angle_B = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
                    angle_C = math.degrees(math.acos((a**2 + b**2 - c**2) / (2 * a * b)))
                    return [angle_A, angle_B, angle_C]
                except (ValueError, ZeroDivisionError, TypeError):
                    raise ValueError("The inner angles cannot be computed: "
                    "Please check the lengths of the edges.")
                
# Now we inherit all the other triangules from the Triangule class.
class Isosceles(Triangle):
    def __init__(self, vertices, edges, inner_angles):
        super().__init__(vertices, edges, inner_angles)

class Equilateral(Triangle):
    def __init__(self, vertices, edges, inner_angles):
        super().__init__(vertices, edges, inner_angles)

class Scalene(Triangle):
    def __init__(self, vertices, edges, inner_angles):
        super().__init__(vertices, edges, inner_angles) 

class TriRectangle(Triangle):
    def __init__(self, vertices, edges, inner_angles):
        super().__init__(vertices, edges, inner_angles)
