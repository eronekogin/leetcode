"""
https://leetcode.com/problems/maximum-points-in-an-archery-competition/description/
"""


class Solution:
    """
    Solution
    """

    def maximum_bob_points(self, num_arrows: int, alice_arrows: list[int]) -> list[int]:
        """
        maximum bob points
        """
        def test(mask: int, remain_arrows: int) -> tuple[int, list[int]]:
            score = 0
            rslt = [0] * 12
            for k in range(12):
                if (mask >> k) & 1:
                    required_arrows = alice_arrows[k] + 1
                    if required_arrows > remain_arrows:
                        return (0, [])  # Not possible

                    score += k
                    rslt[k] = required_arrows
                    remain_arrows -= required_arrows

            rslt[0] += remain_arrows  # In case bob always win
            return (score, rslt)

        best_score = 0
        best_rslt = []
        for mask in range(1 << 12):
            score, rslt = test(mask, num_arrows)
            if score > best_score:
                best_score = score
                best_rslt = rslt

        return best_rslt
