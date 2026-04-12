"""
https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-ii/description/
"""


from itertools import accumulate


class Solution:
    """
    Solution
    """

    def count_of_pairs(self, n: int, x: int, y: int) -> list[int]:
        """
        count of pairs
        """
        if x > y:
            x, y = y, x

        # diff[t] stands of number of new burning houses at time t
        diffs = [0] * n

        for i in range(1, n + 1):
            diffs[0] += 2

            # from i and go left, reach house 1 and stop
            t = min(
                i - 1,  # direct
                abs(i - y) + x  # use shortcut
            )
            diffs[t] -= 1

            # from i and go right, reach house n and stop
            t = min(
                n - i,  # direct
                abs(i - x) + 1 + n - y
            )
            diffs[t] -= 1

            # from i to x, and then split branch
            t = min(
                abs(i - x),  # direct,
                abs(i - y) + 1,  # reach y first then to x
            )
            diffs[t] += 1

            # from i to y and then split branch
            t = min(
                abs(i - y),  # direct,
                abs(i - x) + 1,  # reach x first then to y
            )
            diffs[t] += 1

            # calculate distances from i to x and y
            # if i in [x, y], r = 0
            # if i is left of x, r = x - i
            # if i is right of y, r = i - y
            d = max(x - i, 0) + max(i - y, 0)

            # the fire stops when two branches meet
            # in the middle of [x, y] since it no longer
            # generates optimized branches
            diffs[d + (y - x + 0) // 2] -= 1
            diffs[d + (y - x + 1) // 2] -= 1

        return list(accumulate(diffs))
