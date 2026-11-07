"""
https://leetcode.com/problems/find-indices-of-stable-mountains/description/
"""


class Solution:
    """
    Solution
    """
    def stable_mountains(self, height: list[int], threshold: int) -> list[int]:
        """
        stable moutains
        """
        n = len(height)
        rslt: list[int] = []
        for i in range(1, n):
            if height[i - 1] > threshold:
                rslt.append(i)

        return rslt
