"""
https://leetcode.com/problems/maximize-win-from-two-segments/description/
"""


class Solution:
    """
    Solution
    """

    def maximize_win(self, prize_positions: list[int], k: int) -> int:
        """
        dp[i] stands for the maximum prizes we could get with a single
        length k segment from the first i elements.

        Then we slide the second segment and suppose the segment is
        from index j to i, then the optimal result will be the current
        segement prizes which is i - j + 1, plus the optimal rslt
        from the first j element which is dp[j].
        """
        dp = [0] * (len(prize_positions) + 1)
        rslt = j = 0
        for i, x in enumerate(prize_positions):
            while prize_positions[j] + k < x:
                j += 1

            dp[i + 1] = max(dp[i], i - j + 1)
            rslt = max(rslt, i - j + 1 + dp[j])

        return rslt
