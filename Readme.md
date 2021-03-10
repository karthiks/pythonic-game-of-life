# Game Of Life Exercise

**Definition**

The universe of the Game of Life is an infinite 2-d orthogonal grid of square cells,
each of which is in one of two possible states, alive or dead.

Every cell interacts with its 8 neighbors, which are the cells that are horizontally, vertically, or diagonally adjacent.

**Rules**

At each step in time, the following transitions occur:

    1. Any live cell with fewer than two live neighbors dies as if caused by underpopulation.
    2. Any live cell with two or three live neighbors lives on to the next generation.
    3. Any live cell with more than three live neighbors dies, as if by overcrowding.
    4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The initial pattern constitutes the seed of the system.

The first generation is created by applying the above rules simultaneously to every cell in the seed—births and deaths occur simultaneously, and the discrete moment at which this happens is sometimes called a tick (in other words, each generation is a
pure function of the preceding one).

The rules continue to be applied repeatedly to create further generations.

**Objectives**

    1. Implement the game of life data structures and algorithm.
    2. Demonstrate that game of life algorithm works.

**Hints**

    1. To demonstrate that the program works you can print out the state of the universe to the console/output after each generation. There is no need to build a custom UI.
    2. The program must run and work properly (the working program is better than in-progress design).
    3. Use the ‘Glider’ pattern placed in the middle of the 25x25 cell universe for demonstration.

## Dev Setup

### Option 1
```bash
pyenv 3.9.2
python -m venv .env
source .env/bin/activate
pip install pytest
pytest --version
pip freeze > requirements.txt
```

### Option 2
```bash
pip install -r requirements.txt
```

### To execute tests and see output
```bash
pytest -v -s
```

### To run as main program
```bash
cd game-of-life # project root
python main.py
```