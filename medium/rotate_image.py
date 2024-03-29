"""
https://leetcode.com/problems/rotate-image/
You are given an n x n 2D matrix representing an image, rotate the image by
90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the
input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""
from copy import deepcopy
from typing import List

import pytest


class Solution:
    """
    Time: O(N) where N is amount cells in the matrix
    Space: O(1)
    """

    def rotate_number(self, matrix, row, col):
        tmp_val = matrix[row][col]
        for _ in range(4):
            new_row = col
            new_col = len(matrix) - 1 - row

            matrix[new_row][new_col], tmp_val = tmp_val, matrix[new_row][new_col]

            row = new_row
            col = new_col

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        mid_col = length // 2

        for col in range(0, mid_col):
            start = length - 1 - col

            for row in range(start, col, -1):
                self.rotate_number(matrix, row, col)


class Solution2:
    """
    Reverse rows and mirror matrix diagonally
    Time: O(N)
    Space: O(k) /as solution holds row in memory

    k - amount of columns
    """
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_num = len(matrix)
        col_num = len(matrix[0])
        for i, row in enumerate(matrix):
            matrix[i] = row[::-1]

        for row in range(row_num):
            for col in range(col_num - row):
                n_row = row_num - 1 - col
                n_col = col_num - 1 - row
                matrix[row][col], matrix[n_row][n_col] = matrix[n_row][n_col], matrix[row][col]


@pytest.mark.parametrize(
    "solution", (Solution, Solution2)
)
@pytest.mark.parametrize(
    "matrix,expected_output", (
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[7, 4, 1], [8, 5, 2], [9, 6, 3]],
        ),
        (
            [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
            [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]],
        ),

    )
)
def test_rotate_matrix(solution, matrix, expected_output):
    m = deepcopy(matrix)
    solution().rotate(m)
    assert m == expected_output
