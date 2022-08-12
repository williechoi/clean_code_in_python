from dataclasses import dataclass


@dataclass
class Coordinate2D:
    __slots__ = ("lat", "long")

    lat: float
    long: float

    def __repr__(self):
        return f"{self.__class__.__name__}({self.lat}, {self.long})"


coord = Coordinate2D(2.2, 5.5)
print(coord)

