from ShapeModular.shape import Figure

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
        return None
    
#* Now we create the Square class, which inherits from Rectangle.
class Square(Rectangle):

    #* The Square class is initialized with the same parameters as Rectangle.
    #* Besides, we dont need to redefine the methods for area, perimeter, and
    #* inner angles.
    def __init__(self, vertices, edges, inner_angles):
        super().__init__(vertices, edges, inner_angles)