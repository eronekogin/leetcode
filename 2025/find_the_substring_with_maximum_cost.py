"""
https://leetcode.com/problems/find-the-substring-with-maximum-cost/description/
"""


class Solution:
    """
    Solution
    """

    def maximum_cost_substring(self, s: str, chars: str, vals: list[int]) -> int:
        """
        maximum cost substring
        """
        memo = dict(zip(chars, vals))
        curr_sum = max_sum = 0
        base = ord('a')

        # Kadane
        for c in s:
            curr_sum = max(curr_sum + memo.get(c, ord(c) - base + 1), 0)
            max_sum = max(max_sum, curr_sum)

        return max_sum


print(Solution().maximum_cost_substring("talaqlt", "tqla", [4, 3, 3, -2]))
