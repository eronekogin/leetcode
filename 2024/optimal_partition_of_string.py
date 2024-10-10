"""
https://leetcode.com/problems/optimal-partition-of-string/description/
"""


class Solution:
    """
    Solution
    """

    def partition_string(self, s: str) -> int:
        """
        partition string
        """
        cnt = 0
        memo: set[str] = set()
        for c in s:
            if c in memo:
                cnt += 1
                memo = {c}
                continue

            memo.add(c)

        return cnt + (len(memo) > 0)
