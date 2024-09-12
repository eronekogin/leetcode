"""
https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/description/
"""


class Solution:
    """
    Solution
    """

    def minimum_recolors(self, blocks: str, k: int) -> int:
        """
        minimum recolors
        """
        n = len(blocks)
        whites = recolor = blocks.count('W', 0, k)
        for i in range(k, n):
            whites += (blocks[i] == 'W') - (blocks[i - k] == 'W')
            recolor = min(recolor, whites)

        return recolor


print(Solution().minimum_recolors('WWBBBWBBBBBWWBWWWB', 16))
