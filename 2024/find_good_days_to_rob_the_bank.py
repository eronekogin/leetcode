"""
https://leetcode.com/problems/find-good-days-to-rob-the-bank/
"""


class Solution:
    """
    Solution
    """

    def good_days_to_rob_bank(self, security: list[int], time: int) -> list[int]:
        """
        good_days_to_rob_bank
        """
        n = len(security)
        if time == 0:
            return list(range(n))

        left, right = [1], [1]

        # Build left non-increasing list.
        curr = 1
        for i in range(1, n):
            if security[i] <= security[i - 1]:
                curr += 1
            else:
                curr = 1

            left.append(curr)

        # Build right non-decreasing list.
        curr = 1
        for i in range(n - 2, -1, -1):
            if security[i] <= security[i + 1]:
                curr += 1
            else:
                curr = 1

            right.append(curr)

        right.reverse()

        return [i for i in range(n) if left[i] >= time + 1 and right[i] >= time + 1]
