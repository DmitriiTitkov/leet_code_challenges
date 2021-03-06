"""
Given an array nums. We define a running sum of an array as runningSum[i] =
sum(nums[0]…nums[i]).
Return the running sum of nums.

Example 1:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Example 2:
Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

Example 3:
Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]

Constraints:
1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6
"""
from typing import List

import pytest


class Solution:
    """
    Replace numbers with sum rolling sum of i and i-1 element
    Time: O(n)
    Space: O(1)
    """
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]
        return nums

@pytest.mark.parametrize(
    "nums,expected_output", (
        ([1,2,3,4], [1,3,6,10]),
        ([1,1,1,1,1], [1,2,3,4,5]),
        ([3,1,2,10,1], [3,4,6,16,17]),
    )
)
def test_running_sum(nums,expected_output):
    assert Solution().runningSum(nums) == expected_output
