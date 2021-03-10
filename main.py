from cell import Cell
from gol import Universe


def main():
    # Configure your Universe Gride size here
    universe = Universe(25, 25)
    number_of_gens_to_iterate = 3

    # Different seed data to try
    tub_lives = [Cell(1, 2), Cell(2, 1), Cell(2, 3), Cell(3, 2)]
    glider_lives = [
        Cell(9, 8),
        Cell(10, 9),
        Cell(8, 10),
        Cell(9, 10),
        Cell(10, 10),
    ]
    # Configure your seed data here
    seed_data = glider_lives

    universe.seed(seed_data)
    universe.generations_to_iterate(number_of_gens_to_iterate)


if __name__ == "__main__":
    main()