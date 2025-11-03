"""
https://leetcode.com/problems/count-symmetric-integers/description/
"""


class Solution:
    """
    Solution
    """

    def count_symmetric_integers(self, low: int, high: int) -> int:
        """
        count symmetric integers
        """
        cnt = 0

        # n = 1
        for x in range(1, 10):
            y = x * 10 + x
            if y < low:
                continue

            if y > high:
                return cnt

            cnt += 1

        # n = 2
        for x in range(1, 10):
            for y in range(10):
                for z in range(10):
                    for w in range(10):
                        if x + y == z + w:
                            t = x * 1000 + y * 100 + z * 10 + w
                            if t < low:
                                continue

                            if t > high:
                                return cnt

                            cnt += 1

        return cnt
