from .point import Point
from .line import Line

# Here we have the base class Figure, which will inhirit to all the other
# classes that represent specific figures.
class Figure:
    #* Initializing the attributes vertices, edges and inner_angles
    #* The vertices are a list of Point objects, edges are a list of Line
    #* objects and inner_angles is a list of angles in degrees.
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

