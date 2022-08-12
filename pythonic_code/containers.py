import enum


class SpotStatus(enum):
    MARKED = 1
    UNMARKED = 2


def mark_coordinate(grid, coord):
    if 0 <= coord.x < grid.width and 0 <= coord.y < grid.height:
        grid[coord] = SpotStatus.MARKED


class Boundaries:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def __contains__(self, coord: tuple):
        x, y = coord
        return 0 <= x < self.width and 0 <= y < self.height


class Grid:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
        self.limits = Boundaries(width, height)

    def __contains__(self, coord: tuple):
        return coord in self.limits


def mark_coordinates(grid, coord: tuple):
    if coord in grid:
        grid[coord] = SpotStatus.MARKED
