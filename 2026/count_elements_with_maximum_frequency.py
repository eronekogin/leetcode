"""
https://leetcode.com/problems/count-elements-with-maximum-frequency/description/
"""


class Solution:
    """
    Solution
    """

    def max_frequency_elements(self, nums: list[int]) -> int:
        """
        max frequency elements
        """
        memo: dict[int, int] = {}
        for x in nums:
            memo[x] = memo.get(x, 0) + 1

        max_f, cnt = 0, 0
        for f in memo.values():
            if f > max_f:
                max_f = f
                cnt = 1
            elif f == max_f:
                cnt += 1

        return max_f * cnt
