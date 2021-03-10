from cell import Cell


class TestCell:
    def test_compute_neighbours(self):
        actual = Cell.compute_neighbours(Cell(2, 2))
        print(actual)
        expected = [
            Cell(1, 1),
            Cell(2, 1),
            Cell(3, 1),
            Cell(1, 2),
            Cell(3, 2),
            Cell(1, 3),
            Cell(2, 3),
            Cell(3, 3),
        ]
        assert actual == expected

    def test_has_underpopulated_neighbourhood(self):
        assert Cell.has_underpopulated_neighbourhood(2) == False
        assert Cell.has_underpopulated_neighbourhood(1) == True

    def test_has_overpopulated_neighbourhood(self):
        assert Cell.has_overpopulated_neighbourhood(3) == False
        assert Cell.has_overpopulated_neighbourhood(4) == True

    def test_has_wellpopulated_neighbourhood(self):
        assert Cell.has_wellpopulated_neighbourhood(1) == False
        assert Cell.has_wellpopulated_neighbourhood(2) == True
        assert Cell.has_wellpopulated_neighbourhood(3) == True
        assert Cell.has_wellpopulated_neighbourhood(4) == False

    def test_has_reproducable_neighbourhood(self):
        assert Cell.has_reproducable_neighbourhood(2) == False
        assert Cell.has_reproducable_neighbourhood(3) == True
        assert Cell.has_reproducable_neighbourhood(4) == False

    def test_equals(self):
        c12 = Cell(1, 2)
        c21 = Cell(2, 1)
        assert c12 != c21
        assert c12 == Cell(1, 2)
