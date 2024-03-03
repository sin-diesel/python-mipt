
from typing import List as _List
from typing import Callable as _Callable

SudokuField = _List[_List[int]]


class Sudoku:
    def __init__(
        self,
        array: SudokuField,
        constraints: _List[_Callable[[SudokuField], bool]]
    ) -> None:
        self._array = array
        self._constraints = constraints

    def check(self) -> bool:
        return all([constraint(self._array) for constraint in self._constraints])


def correct_numbers(field: SudokuField) -> bool:
    return all(
        all(0 <= x <= 9 for x in row)
        for row in field
    )

def correct_dimensions(field: SudokuField) -> bool:
    return len(field) == 9 and all(len(row) == 9 for row in field)


s = Sudoku(
    [[3, 5, 0, 1, 8, 6, 9, 0, 0],
     [2, 9, 8, 7, 4, 3, 6, 0, 5],
     [1, 6, 7, 9, 5, 0, 4, 8, 3],
     [4, 8, 0, 5, 2, 7, 3, 6, 9],
     [0, 3, 2, 6, 1, 4, 5, 7, 8],
     [5, 7, 6, 3, 9, 8, 2, 4, 1],
     [7, 2, 9, 0, 6, 0, 1, 3, 4],
     [8, 4, 5, 2, 3, 1, 7, 9, 6],
     [6, 1, 0, 4, 7, 9, 8, 5, 2]],
    [correct_numbers, correct_dimensions])

print(s.check())
