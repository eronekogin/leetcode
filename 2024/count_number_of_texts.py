"""
https://leetcode.com/problems/count-number-of-texts/description/
"""


class Solution:
    """
    Solution
    """

    def count_texts(self, pressed_keys: str) -> int:
        """
        count texts
        """
        m = 10 ** 9 + 7
        dp = [1]
        prev = None
        for k in pressed_keys:
            keep = 1 if k != prev else 3 + (k in '79')
            del dp[:-keep]
            dp.append(sum(dp) % m)
            prev = k

        return dp[-1]


print(Solution().count_texts('222222222222222222222222222222222222'))
