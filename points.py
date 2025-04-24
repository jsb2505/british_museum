from z_functions import calculate_z


class Point:
    def __init__(self, x: float=0.0, y: float=0.0):
        """
        Initializes a 3D point with x, y, z coordinates.
        """
        self._x = x
        self._y = y
        self._z = calculate_z(x, y)

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, value: float) -> None:
        self._x = round(value, 4)
        self._z = calculate_z(self._x, self._y)

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, value: float) -> None:
        self._y = round(value, 4)
        self._z = calculate_z(self._x, self._y)

    @property
    def z(self) -> float:
        return self._z

    def __repr__(self) -> str:
        return f"Point(x={self.x}, y={self.y}, z={self.z})"
    
    def __eq__(self, other: "Point") -> bool:
        return isinstance(other, Point) and self.to_tuple() == other.to_tuple()


    def to_tuple(self) -> tuple:
        """
        Returns the point as a tuple: (x, y, z)
        """
        return (self.x, self.y, self.z)

    def distance_to(self, other: "Point") -> float:
        """
        Returns the Euclidean distance to another Point.
        """
        return ((self.x - other.x)**2 + 
                (self.y - other.y)**2 + 
                (self.z - other.z)**2) ** 0.5
