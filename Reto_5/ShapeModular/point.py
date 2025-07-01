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