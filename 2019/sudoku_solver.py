"""
https://leetcode.com/problems/sudoku-solver/
"""

from typing import List


class Solution:
    """
    Solution for the sudoku board.
    """

    _ALL_ONES = [1 for _ in range(10)]

    class Cell():
        """
        Object to stand for a single cell on a sudoku board.
        """
        _ALL_ZERO = [0 for _ in range(10)]

        def __init__(self):
            self.value = 0  # Current value in the cell.
            self.numPossibilities = 9  # Total allowed values in the cell.
            # Constraint on each possible value.
            # If constraints[value] is set to 1,
            # the value is not allowed in the cell.
            self.constraints = self._ALL_ZERO.copy()

        def copy_out(self) -> tuple:
            return (self.value, self.numPossibilities, self.constraints.copy())

        def copy_in(self, ref: tuple) -> None:
            self.value, self.numPossibilities, self.constraints = ref

    def __init__(self):
        # Initialize the board.
        self.cells = None  # List to hold all cells on the board.
        self.emptyCells = None  # List to hold empty cells.

    def _backup_cells(self) -> dict:
        """
        Back up the current cells to a reference dictionary.
        """
        rslt = {}
        for row in range(9):
            for col in range(9):
                rslt[(row, col)] = self.cells[row][col].copy_out()

        return rslt

    def _restore_cells(self, ref: dict) -> None:
        """
        Restore the current cells from the reference dictionary.
        """
        for k, v in ref.items():
            row, col = k
            self.cells[row][col].copy_in(v)

    def _update_constraints(
            self, row: int, col: int, excludedValue: int) -> bool:
        """
        Update the constraints of the specified cell based on the
        excluded value. If at the end there is only one possibility left
        for the current cell, it will call the set_value function to
        set that only value to the current cell.
        """
        currCell = self.cells[row][col]

        if currCell.constraints[excludedValue]:  # Already exlcuded.
            return True

        if currCell.value == excludedValue:  # Can't update, conflict found.
            return False

        # Update constraints of the current cell.
        currCell.constraints[excludedValue] = 1
        currCell.numPossibilities -= 1

        if currCell.numPossibilities > 1:
            return True  # Still have more than 1 possibilities.

        # Set value when it has only 1 possibility.
        for i in range(1, 10):
            if not currCell.constraints[i]:
                return self._set_value(row, col, i)

    def _set_value(self, row: int, col: int, value: int) -> bool:
        """
        Set the value of the specified cell to value. Meanwhile propagate 
        constraints to other cells and deduce new values where possible.
        """
        currCell = self.cells[row][col]

        if currCell.value == value:  # Already set.
            return True

        if currCell.constraints[value]:  # Already not allowed.
            return False

        # Set value to the current cell. After value is set, for
        # the current cell, the allowed possibility is only 1 and
        # all the other values are not allowed.
        currCell.constraints = self._ALL_ONES.copy()
        currCell.constraints[value] = 0
        currCell.numPossibilities = 1
        currCell.value = value

        # Propagate constraints to other cells.
        for i in range(9):
            # Walk through rows.
            if i != row and not self._update_constraints(i, col, value):
                return False  # Value set is not allowed.

            # Walk through columns.
            if i != col and not self._update_constraints(row, i, value):
                return False  # Value set is not allowed.

            # Walk through the 3x3 box cells where the current cell stands.
            boxRow = row // 3 * 3 + i // 3
            boxCol = col // 3 * 3 + i % 3
            if boxRow != row and boxCol != col and not self._update_constraints(
                    boxRow, boxCol, value):
                return False  # Value set is not allowed.

        # Successfully set the value.
        return True

    def _find_values_for_empty_cells(self) -> bool:
        """
        Find values for all empty cells.
        """
        # Collect empty cells from the current board.
        self.emptyCells = []
        for row in range(9):
            for col in range(9):
                if not self.cells[row][col].value:
                    self.emptyCells.append((row, col))

        # Sort the empty cells by its number of possibilities
        # in ascending order so that the least possibility cell could be
        # processed first.
        self.emptyCells.sort(
            key=lambda idx: self.cells[idx[0]][idx[1]].numPossibilities)

        # Start back track from the least possibilitiy empty cell.
        return self._back_track(0)

    def _back_track(self, startPos: int) -> bool:
        """
        Start to back track from the cell from the empty cell list at the
        specified start position.
        """
        if startPos >= len(self.emptyCells):  # All empty cells processed.
            return True

        row, col = self.emptyCells[startPos]

        # If value is already set during the back tracking process,
        # go to the next empty cell.
        if self.cells[row][col].value:
            return self._back_track(startPos + 1)

        # If still having more than 1 possibility, backup the original cells
        # on the board.
        originalCells = self._backup_cells()
        constraints = self.cells[row][col].constraints.copy()

        for i in range(1, 10):
            if not constraints[i]:  # Value is allowed to be set.
                if self._set_value(row, col, i):  # Value is set successfully.
                    # Process the next empty cell.
                    if self._back_track(startPos + 1):
                        return True  # All back tracking is done.

                # Conflicts found either during set value or during
                # the other rounds of back tracking. Restoring the cells
                # from the original copy.
                self._restore_cells(originalCells)

        # When coming here, all back trackings are failed.
        return False

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.cells = [[self.Cell() for _ in range(9)] for _ in range(9)]

        # Set values to the inner cells based on the input board.
        for row in range(9):
            for col in range(9):
                value = board[row][col]
                if value != '.' and not self._set_value(row, col, int(value)):
                    return  # Input board is invalid or unsolvable.

        if not self._find_values_for_empty_cells():
            return  # Input board is unsolvable.

        # When coming here, a solution is found. Copy the results from
        # inner cells back to the input board.
        for row in range(9):
            for col in range(9):
                board[row][col] = str(self.cells[row][col].value)


board = [
    [".", ".", "9", "7", "4", "8", ".", ".", "."],
    ["7", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", "2", ".", "1", ".", "9", ".", ".", "."],
    [".", ".", "7", ".", ".", ".", "2", "4", "."],
    [".", "6", "4", ".", "1", ".", "5", "9", "."],
    [".", "9", "8", ".", ".", ".", "3", ".", "."],
    [".", ".", ".", "8", ".", "3", ".", "2", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "6"],
    [".", ".", ".", "2", "7", "5", "9", ".", "."]]

s = Solution()
s.solveSudoku(board)
