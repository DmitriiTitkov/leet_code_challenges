"""
ou are given an array of k linked-lists lists, each linked-list is sorted in
ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []

Constraints:
k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
"""
import heapq
from typing import List, Optional

from test_tools.linked_lists import ListNode


class Solution:
    """
    Use priority queue to sort the lists:

    Time: O(N * Log k)
    Space: O(N)
    """
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for node in lists:
            while node is not None:
                heapq.heappush(heap, node.val)
                node = node.next

        result = ListNode(val="Dummy")
        cur = result

        while heap:
            val = heapq.heappop(heap)
            cur.next = ListNode(val)
            cur = cur.next

        return result.next
