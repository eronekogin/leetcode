"""
https://leetcode.com/problems/minimum-suffix-flips/
"""


class Solution:
    def minFlips(self, target: str) -> int:
        # Status stands for the current status of all the remaining bulbs.
        # Each flip will change the status to the other side.
        flips = 0
        status = '0'
        for c in target:
            if c != status:
                flips += 1
                status = '0' if status == '1' else '1'

        return flips
