# Minesweeper in 66 Lines of Python and Automatic Solver

This repository contains code for a Minesweeper game and an automatic solver, as discussed in the blog post at [Habr](https://habr.com/ru/articles/833494/).

## Features

- **Minesweeper Game**: A compact implementation of the classic Minesweeper game in Python.
- **Automatic Solver**: An intelligent solver that uses heuristics and probability to play Minesweeper.

## How to Play

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ArtUkrainskiy/PythonConsoleMinesweeper.git
   cd PythonConsoleMinesweeper
   ```

2. **Run the Game**:
   ```bash
   python3 minesweeper.py 10 10 10
   ```
   - **Parameters**:
     - `10` is the width of the board.
     - `10` is the height of the board.
     - `10` is the number of mines.

## How the Solver Works

1. **Initial Setup**: Starts by placing mines and revealing an initial cell.
2. **Reveal Safe Cells**: Identifies and reveals cells that are guaranteed to be safe based on the current board state.
3. **Probability Analysis**: If no guaranteed safe cells are found, it analyzes probabilities to select the next cell to reveal.
4. **Victory Condition**: The game ends when all safe cells are revealed or a mine is triggered.

## How to Use the Solver

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ArtUkrainskiy/PythonConsoleMinesweeper.git
   cd PythonConsoleMinesweeper
   ```

2. **Run the Solver**:
   ```bash
   python3 solver.py 10 10 10
   ```
   - **Parameters**:
     - `10` is the width of the board.
     - `10` is the height of the board.
     - `10` is the number of mines.

## Code Overview

- **`minesweeper.py`**: Contains the implementation of the Minesweeper game.
- **`solver.py`**: Contains the Minesweeper solver with heuristic and probability-based algorithms.

## Contributing

Feel free to open issues, submit pull requests, or suggest improvements. Contributions are welcome!
cifics as needed.
