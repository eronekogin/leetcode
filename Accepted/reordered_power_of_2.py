"""
https://leetcode.com/problems/reordered-power-of-2/
"""


class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        return sorted(str(N)) in [sorted(str(1 << i)) for i in range(30)]
