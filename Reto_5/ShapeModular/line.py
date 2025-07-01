from .point import Point

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