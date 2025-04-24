from math import sqrt
from points import Point


class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end
        self._divs = 1

    @property
    def divs(self) -> int:
        return self._divs
    
    @divs.setter
    def divs(self, new_divs: int=1) -> None:
        if new_divs <= 0:
            raise ValueError(f"Number of line divisions, {new_divs}, must be positive.")
        elif not isinstance(new_divs, int):
            raise ValueError(f"Number of line divisions, {new_divs}, must be an integer.")
        self._divs = new_divs

    def __repr__(self):
        return f"Line(start={self.start}, end={self.end})"
    
    def get_length(self) -> float:
        """
        Returns the Euclidean distance between start and end points of the line.
        """
        return sqrt((self.start.x - self.end.x)**2 + 
                    (self.start.y - self.end.y)**2 + 
                    (self.start.z - self.end.z)**2)
    
    def get_div_points(self) -> list:
        '''Returns all the points along the length of the line at the div intervals.'''        
        points = []
        for i in range(self.divs + 1):
            x = self.start.x + i * (self.end.x - self.start.x) / self.divs
            y = self.start.y + i * (self.end.y - self.start.y) / self.divs
            point = Point(x, y)
            points.append(point)
        return points
