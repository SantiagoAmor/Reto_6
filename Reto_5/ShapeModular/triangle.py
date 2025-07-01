from ShapeModular.shape import Figure

import math

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

# Now we inherit all the other triangles from the Triangle class.
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
