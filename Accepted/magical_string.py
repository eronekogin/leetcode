"""
https://leetcode.com/problems/magical-string/
"""


class Solution:
    def magicalString(self, n: int) -> int:
        s = [1, 2, 2]
        rtIdx = 2  # Index to indicate how many times to repeat.
        while len(s) < n:
            s += [3 - s[-1]] * s[rtIdx]
            rtIdx += 1  # Advance to the next repeat index.

        return s[:n].count(1)


print(Solution().magicalString(4))
