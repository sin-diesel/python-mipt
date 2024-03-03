
from typing import List as _List
from typing import Callable as _Callable

SudokuField = _List[_List[int]]


class Sudoku:
    def __init__(
        self,
        array: SudokuField,
        constraints: _List[_Callable[[SudokuField], bool]]
    ) -> None:
        self.array = array
        self.constraints = constraints

    def check(self) -> bool:
        return all([constraint(self.array) for constraint in self.constraints])


def correct_numbers(field: SudokuField) -> bool:
    return all(
        all(0 <= x <= 9 for x in row)
        for row in field
    )

def correct_dimensions(field: SudokuField) -> bool:
    return len(field) == 9 and all(len(row) == 9 for row in field)


class SudokuOperation:
    def __init__(self, x: int, y: int, value: int) -> None:
        self.x = x
        self.y = y
        self.value = value


class SudokuCommand:
    def __init__(self, sudoku: Sudoku, x: int, y: int, number: int) -> None:
        self.sudoku = sudoku
        self.x = x
        self.y = y
        self.number = number
        self.history = list[SudokuOperation]

    def do(self):
        self.history.append(SudokuOperation(self.x,
                                            self.y,
                                            self.sudoku.array[self.x],
                                            self.sudoku.array[self.y]))
        self.sudoku.array[self.x][self.y] = self.number

    def undo(self):
        prev_value = self.history[-1]
        self.sudoku.array[prev_value.x][prev_value.y] = prev_value.value
        self.history.pop()
