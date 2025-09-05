from collections import defaultdict


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        n = 9
        # size of the Sudoku board (9x9)

        # use hash sets to track numbers seen in each row, column, and 3x3 box
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        # iterate over every cell in the board
        for r in range(n):
            for c in range(n):
                val = board[r][c]

                # skip empty cells
                if val == ".":
                    continue

                    # check if the number already exists in the current row
                if val in rows[r]:
                    return False
                rows[r].add(val)  # record number in row set

                # check if the number already exists in the current column
                if val in cols[c]:
                    return False
                cols[c].add(val)  # record number in column set

                # compute which 3x3 box this cell belongs to
                idx = (r // 3) * 3 + (c // 3)

                # check if the number already exists in the current 3x3 box
                if val in boxes[idx]:
                    return False
                boxes[idx].add(val)  # record number in box set

        # if no duplicates are found, the board is valid
        return True

