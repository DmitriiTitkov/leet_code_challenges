"""
There is a robot on an m x n grid. The robot is initially located at the
top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right
corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right
at any point in time.
Given the two integers m and n, return the number of possible unique paths that
the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to
2 * 109.

Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Constraints:

1 <= m, n <= 100
"""
from functools import lru_cache

import pytest


class Solution:
    """DFS solution with memorization"""
    def uniquePaths(self, m: int, n: int) -> int:

        @lru_cache
        def dfs(m: int, n: int) -> int:
            res = 0

            if m == 0 and n == 0:
                return 1

            if m > 0:
                res += dfs(m - 1, n)

            if n > 0:
                res += dfs(m, n - 1)

            return res

        return dfs(m - 1, n - 1)


@pytest.mark.parametrize(
    "m,n,expected_result",
    (
        (3, 7, 28),
        (3, 2, 3),
    )
)
def test_unique_paths(m, n, expected_result):
    assert Solution().uniquePaths(m, n) == expected_result
