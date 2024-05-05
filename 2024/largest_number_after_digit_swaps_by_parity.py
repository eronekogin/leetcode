"""
https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/description/
"""


class Solution:
    """
    Solution
    """

    def largest_integer(self, num: int) -> int:
        """
        largest integer
        """
        flags: list[int] = []
        odds: list[int] = []
        evens: list[int] = []
        curr = num
        while curr:
            curr, r = divmod(curr, 10)
            if r & 1:
                odds.append(r)
                flags.append(1)
            else:
                evens.append(r)
                flags.append(0)

        evens.sort()
        odds.sort()

        rslt = 0
        while flags:
            candidate = odds.pop() if flags.pop() else evens.pop()
            rslt = rslt * 10 + candidate

        return rslt


print(Solution().largest_integer(1234))
