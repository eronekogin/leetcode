"""
https://leetcode.com/problems/egg-drop-with-2-eggs-and-n-floors/
"""


from functools import cache


class Solution:

    @cache
    def twoEggDrop(self, n: int) -> int:
        """
        Drop the first egg on floor i:
            If the egg is broken, we reduce the range of f to [1, i], and we
            can use the second egg i - 1 times to determine the f floor.

            If the egg is not broken, we reduce the range of f to remaining
            floor after i, and we try it again by dropping the first egg.
        """
        return 1 + min(
            [
                max(i - 1, self.twoEggDrop(n - i))
                for i in range(1, n)
            ],
            default=0
        )
        
