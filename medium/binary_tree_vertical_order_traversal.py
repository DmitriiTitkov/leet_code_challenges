"""
Given the root of a binary tree, return the vertical order traversal of its
nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left
to right.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]

Example 2:
Input: root = [3,9,8,4,0,1,7]
Output: [[4],[9],[3,0,1],[8],[7]]

Example 3:
Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
Output: [[4],[9,5],[3,0,1],[8,2],[7]]


Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""
# Definition for a binary tree node.
import collections
from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Use bfs to store nodes per column and find min max columns.

    Time: O(n)
    Space: O(n)
    """
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        column_map = defaultdict(list)
        queue = collections.deque()
        queue.appendleft((0, root))

        min_col = max_col = 0

        while queue:
            col, node = queue.pop()
            column_map[col].append(node.val)

            min_col = min(min_col, col)
            max_col = max(max_col, col)

            if node.left is not None:
                queue.appendleft((col - 1, node.left))

            if node.right is not None:
                queue.appendleft((col + 1, node.right))

        res = []
        for col in range(min_col, max_col + 1):
            res.append(column_map[col])

        return res
