from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Number of rows in the grid
        ROWS = len(board)
        # Number of columns in the grid (assumes at least one row)
        COLS = len(board[0])

        # Set to keep track of cells currently in the path of our search
        # (prevents reusing the same cell for the current word construction)
        path = set()

        def dfs(r, c, i):
            # If we have matched all characters in 'word', success
            if i == len(word):
                return True
            # Fail if:
            # - outside grid bounds
            # - current board cell does not match needed character word[i]
            # - cell already used in current path
            if (
                    r < 0 or c < 0 or
                    r >= ROWS or c >= COLS or
                    board[r][c] != word[i] or
                    (r, c) in path
            ):
                return False

            # Mark this cell as used in the current path
            path.add((r, c))

            # Explore all 4 neighboring directions looking for next character
            found = (
                    dfs(r + 1, c, i + 1) or  # Down
                    dfs(r - 1, c, i + 1) or  # Up
                    dfs(r, c + 1, i + 1) or  # Right
                    dfs(r, c - 1, i + 1)     # Left
            )

            # Backtrack: remove the cell so it can be used in other paths
            path.remove((r, c))

            # Return whether any path worked
            return found

        # Try starting the search from every cell in the grid
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True

        # If no starting point leads to success, word not found
        return False