from cell import Cell


class Universe:
    def __init__(self, length, bredth):
        self._length = length
        self._bredth = bredth
        self._lives = []

    @property
    def lives(self):
        return self._lives

    # @lives.setter
    # def lives(self, arr):
    #     self._lives = arr

    def seed(self, lives):
        self._lives = lives

    def evolve(self):
        next_gen_lives = []
        for x in range(self._length):
            for y in range(self._bredth):
                cell = Cell(x, y)
                alive_neighbours = self.alive_neighbours(cell)
                neighbour_count = len(alive_neighbours)
                if self.is_live_cell(cell) and Cell.has_wellpopulated_neighbourhood(
                    neighbour_count
                ):
                    next_gen_lives.append(cell)
                elif self.is_dead_cell(cell) and Cell.has_reproducable_neighbourhood(
                    neighbour_count
                ):
                    next_gen_lives.append(cell)
        self._lives = next_gen_lives
        return self

    def is_live_cell(self, cell):
        return cell in self._lives

    def is_dead_cell(self, cell):
        return not self.is_live_cell(cell)

    def alive_neighbours(self, cell):
        neighbouring_cells = Cell.compute_neighbours(cell)
        return list(filter(lambda x: x in neighbouring_cells, self.lives))

    def generations_to_iterate(self, count):
        for x in range(count):
            print("Generation %d is %s" % (x + 1, self.evolve().lives))
        return self
