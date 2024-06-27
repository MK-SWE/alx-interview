#!/usr/bin/python3
"""Island Perimeter
"""


def island_perimeter(grid) -> int:
    """
    Create a function island_perimeter(grid):
    that returns the perimeter of the island described in grid:
    """
    perimeter = 0
    for row_index in range(len(grid)):
        for column_index in range(len(grid[row_index])):
            if grid[row_index][column_index] == 1:
                perimeter += 4
                if column_index > 0 and grid[row_index][column_index-1] == 1:
                    perimeter -= 2
                if row_index > 0 and grid[row_index-1][column_index] == 1:
                    perimeter -= 2
    return perimeter
