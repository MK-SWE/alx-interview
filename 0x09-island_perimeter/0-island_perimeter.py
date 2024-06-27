#!/usr/bin/python3
"""Island Perimeter
"""


def island_perimeter(grid) -> int:
    """
    Create a function island_perimeter(grid):
    that returns the perimeter of the island described in grid:
    """
    def dfs(rowIndex: int, colIndex: int) -> int:
        """
        for out of bound items, return 1
        for water, return 1, because this side is a perimeter
        for '-1' return 0, because we have been there
        Change the grid value to '-1' to mark it as visited
        """
        if rowIndex < 0 or rowIndex > len(grid)-1 or \
           colIndex < 0 or colIndex > len(grid[rowIndex])-1:
            return 1
        elif grid[rowIndex][colIndex] == -1:
            return 0
        elif grid[rowIndex][colIndex] == 0:
            return 1
        else:
            grid[rowIndex][colIndex] = -1
            return dfs(rowIndex, colIndex - 1) + dfs(rowIndex - 1, colIndex) +\
                dfs(rowIndex, colIndex + 1) + dfs(rowIndex + 1, colIndex)

    if grid is None or len(grid) == 0:
        return 0
    else:
        for current_row in range(len(grid)):
            for current_col in range(len(grid[current_row])):
                if grid[current_row][current_col] == 1:
                    return dfs(current_row, current_col)
