from gol import Universe
from cell import Cell


class TestUniverse:
    def test_lives_before_seeding(self):
        universe = Universe(5, 5)
        assert universe.lives == []

    def test_lives_after_seeding(self):
        universe = Universe(5, 5)
        lives = [Cell(2, 2)]
        universe.seed(lives)
        assert universe.lives == [Cell(2, 2)]

    def test_is_live_cell(self):
        universe = Universe(5, 5)
        lives = [Cell(2, 2)]
        universe.seed(lives)
        assert universe.is_live_cell(Cell(1, 1)) == False
        assert universe.is_live_cell(Cell(2, 2)) == True

    def test_is_dead_cell(self):
        universe = Universe(5, 5)
        lives = [Cell(2, 2)]
        universe.seed(lives)
        assert universe.is_dead_cell(Cell(1, 1)) == True
        assert universe.is_dead_cell(Cell(2, 2)) == False

    def test_alive_neighbours(self):
        universe = Universe(5, 5)
        lives = [
            Cell(1, 1),
            Cell(3, 3),
        ]
        universe.seed(lives)
        assert universe.alive_neighbours(Cell(2, 2)) == [Cell(1, 1), Cell(3, 3)]

    def test_death_from_underpopulated_neighbourhood(self):
        universe = Universe(5, 5)
        lives = [Cell(2, 2)]
        universe.seed(lives)
        actual = universe.evolve().lives
        expected = []
        assert actual == expected

    def test_death_from_overpopulated_neighbourhood(self):
        universe = Universe(5, 5)
        subjectCell = Cell(2, 2)
        lives = [Cell(1, 1), Cell(3, 1), subjectCell, Cell(3, 1), Cell(3, 3)]
        universe.seed(lives)
        next_gen_lives = universe.evolve().lives
        assert subjectCell not in next_gen_lives

    def test_survival_from_wellpopulated_neighbourhood(self):
        universe = Universe(5, 5)
        subjectCell = Cell(2, 2)
        lives = [Cell(1, 1), Cell(3, 1), subjectCell, Cell(3, 3)]
        universe.seed(lives)
        next_gen_lives = universe.evolve().lives
        assert subjectCell in next_gen_lives

    def test_rebirth_of_dead_cell_from_reproducable_population(self):
        universe = Universe(5, 5)
        subjectCell = Cell(2, 2)
        lives = [Cell(1, 1), Cell(3, 1), Cell(3, 3)]
        universe.seed(lives)
        next_gen_lives = universe.evolve().lives
        assert subjectCell in next_gen_lives

    def test_generations_to_iterate_for_block_lives(self):
        # Ref.: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
        universe = Universe(5, 5)
        block_lives = [
            Cell(1, 1),
            Cell(1, 2),
            Cell(2, 1),
            Cell(2, 2),
        ]
        universe.seed(block_lives)
        universe.generations_to_iterate(3)
        assert universe.lives == block_lives

    def test_generations_to_iterate_for_tub_lives(self):
        # Ref.: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
        universe = Universe(5, 5)
        tub_lives = [
            Cell(1, 2),
            Cell(2, 1),
            Cell(2, 3),
            Cell(3, 2),
        ]
        universe.seed(tub_lives)
        universe.generations_to_iterate(3)
        assert universe.lives == tub_lives

    def test_generations_to_iterate_for_blinker_lives(self):
        # Ref.: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
        universe = Universe(5, 5)
        blinker_lives = [
            Cell(2, 1),
            Cell(2, 2),
            Cell(2, 3),
        ]
        universe.seed(blinker_lives)
        universe.generations_to_iterate(4)
        assert universe.lives == blinker_lives

        universe.generations_to_iterate(3)
        assert universe.lives == [Cell(1, 2), Cell(2, 2), Cell(3, 2)]

    def test_generations_to_iterate_for_glider_lives(self):
        # Ref.: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
        universe = Universe(25, 25)
        glider_lives = [
            Cell(9, 8),
            Cell(10, 9),
            Cell(8, 10),
            Cell(9, 10),
            Cell(10, 10),
        ]
        universe.seed(glider_lives)
        universe.generations_to_iterate(3)
        assert universe.lives == [
            Cell(9, 9),
            Cell(9, 11),
            Cell(10, 10),
            Cell(10, 11),
            Cell(11, 10),
        ]
