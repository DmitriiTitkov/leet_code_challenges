"""
A message containing letters from A-Z can be encoded into numbers using the
following mapping:
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back
into letters using the reverse of the mapping above (there may be multiple
ways). For example, "11106" can be mapped into:
"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into
'F' since "6" is different from "06".
Given a string s containing only digits, return the number of ways to decode it.
The test cases are generated so that the answer fits in a 32-bit integer.

Example 1:
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF"
(2 2 6).

Example 3:
Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero
("6" is different from "06").

Constraints:
1 <= s.length <= 100
s contains only digits and may contain leading zero(s).
"""
from functools import cache

import pytest

decode_options = set(str(num) for num in range(1, 27))


class Solution:
    """
    Memoization solution. For each index we can consider one digit string or
    two digit string.
    Time: O(n) - consider each char once
    Space: O(n) - to support cache
    """
    def numDecodings(self, s: str) -> int:
        @cache
        def decode_from_index(index) -> int:
            if index == len(s):
                return 1

            num_from_first = num_from_second = 0

            first = s[index]
            if first in decode_options:
                num_from_first = decode_from_index(index + 1)

            if index < len(s) - 1:
                second = s[index:index + 2]
                if second in decode_options:
                    num_from_second = decode_from_index(index + 2)

            return num_from_first + num_from_second

        return decode_from_index(0)


class Solution2:
    """
    DP with tabulation.
    Time: O(n)
    Space: O(n)
    """
    def numDecodings(self, s: str) -> int:
        length = len(s)
        dp = [0] * length
        dp[length - 1] = 1 if s[length - 1] in decode_options else 0

        for i in range(length - 2, -1, -1):
            if s[i] in decode_options:
                dp[i] = dp[i + 1]

            if s[i:i + 2] in decode_options:
                prev_decode_opts = dp[i + 2] if i < length - 2 else 1
                dp[i] += prev_decode_opts

        return dp[0]


@pytest.mark.parametrize(
    "solution", [Solution, Solution2]
)
@pytest.mark.parametrize(
    "s,expected_output", (
        ("12", 2),
        ("226", 3),
        ("06", 0),
    )
)
def test_num_decodings(solution, s, expected_output):
    assert solution().numDecodings(s) == expected_output
