class Cell:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @staticmethod
    def compute_neighbours(c):
        # print(c)
        return [
            Cell(c.x - 1, c.y - 1),
            Cell(c.x, c.y - 1),
            Cell(c.x + 1, c.y - 1),
            Cell(c.x - 1, c.y),
            Cell(c.x + 1, c.y),
            Cell(c.x - 1, c.y + 1),
            Cell(c.x, c.y + 1),
            Cell(c.x + 1, c.y + 1),
        ]

    @staticmethod
    def has_underpopulated_neighbourhood(neighbour_count):
        return neighbour_count < 2

    @staticmethod
    def has_overpopulated_neighbourhood(neighbour_count):
        return neighbour_count > 3

    @staticmethod
    def has_wellpopulated_neighbourhood(neighbour_count):
        return (not Cell.has_underpopulated_neighbourhood(neighbour_count)) and (
            not Cell.has_overpopulated_neighbourhood(neighbour_count)
        )

    @staticmethod
    def has_reproducable_neighbourhood(neighbour_count):
        return neighbour_count == 3

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __eq__(self, other):
        return (self._x == other.x) and (self._y == other.y)

    def __str__(self):
        return "(%s,%s)" % (self._x, self._y)

    def __repr__(self):
        return "(%s,%s)" % (self._x, self._y)
