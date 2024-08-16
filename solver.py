import os
import sys
import matplotlib.pyplot as plt

from minesweeper import Minesweeper


class MinesweeperSolver(Minesweeper):
    def __init__(self, rows, cols, mines):
        super().__init__(rows, cols, mines)
        self.probabilities = [0] * self.size
        self.flagged = [False] * self.size

        #  делаем первый шаг
        self.place_mines(int(rows / 2), int(cols / 2))
        self.reveal(int(rows / 2 * cols + cols / 2))
        self.print_board()

    def analyze_and_reveal(self):
        to_reveal = []
        self.probabilities = [0] * self.size
        flag_placed = []

        for idx, cell in enumerate(self.board):
            if cell <= 1:  # клетка не раскрыта или по соседству 0 мин
                continue

            unrevealed_neighbors = [n for n in self.get_neighbors(idx) if self.board[n] <= 0]
            flag_neighbors_count = sum(self.flagged[n] for n in self.get_neighbors(idx))

            #  если количество мин вокруг равно значению клетки то помечаем соседей флагом
            if cell - 1 == len(unrevealed_neighbors):
                for un_idx in unrevealed_neighbors:
                    if not self.flagged[un_idx]:
                        self.flagged[un_idx] = True
                        flag_placed.append(divmod(un_idx, self.cols))

            for un_idx in unrevealed_neighbors:
                # если соседняя клетка не помечена флагом
                if not self.flagged[un_idx]:
                    if cell - 1 == flag_neighbors_count and un_idx not in to_reveal:
                        # если количество помеченных флагом клеток вокруг равно значению клетки
                        # добавляем ее в список для раскрытия
                        to_reveal.append(un_idx)
                    # подсчитываем вероятность клетки быть заминированной на основании ее значения
                    # и количества нераскрытых и не помеченных флагом клеток вокруг
                    self.probabilities[un_idx] += (cell - 1) / (len(unrevealed_neighbors))

        if to_reveal:
            # открываем гарантированно безопасные клетки
            print("Reveal safe cells:", [divmod(safe_idx, self.cols) for safe_idx in to_reveal])
            list(map(self.reveal, to_reveal))
        elif flag_placed:
            # если безопасных клеток нет, но какая-то клетка была помечена флагом, следует проанализировать доску снова
            print("Placed flags:", flag_placed)
            return True
        else:
            # находим клетку с минимальной вероятностью быть заминированной и пытаемся открыть
            probably_safe = (i for i, p in enumerate(self.probabilities) if p > 0 and not self.flagged[i])
            idx = min(probably_safe, key=lambda i: self.probabilities[i], default=None)
            if idx is not None:
                print("Try reveal:", divmod(idx, self.cols), self.board[idx])
                if self.board[idx] == 0:
                    return False
                self.reveal(idx)
            else:
                return False
        return True

    def solve(self):
        not_failed = True
        while not all(cell >= 0 for cell in self.board) and (not_failed := self.analyze_and_reveal()):
            self.print_board()

        if not_failed:
            print("Congratulations! You've cleared the minefield.")
        else:
            print("Auto-solver hit a mine! Game Over.")
        return not_failed


if __name__ == "__main__":
    rows, cols, mines = (int(arg) for arg in sys.argv[1:]) if len(sys.argv) > 1 else (10, 10, 10)
    solver = MinesweeperSolver(rows, cols, mines)
    solver.solve()

