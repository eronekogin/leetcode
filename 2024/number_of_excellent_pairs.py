"""
https://leetcode.com/problems/number-of-excellent-pairs/description/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def count_excellent_pairs(self, nums: list[int], k: int) -> int:
        """
        bits(x & y) + bits(x | y) = bits(x) + bits(y)
        """
        cnt = Counter(map(int.bit_count, set(nums)))
        return sum(cnt[k1] * cnt[k2] for k1 in cnt for k2 in cnt if k1 + k2 >= k)


print(Solution().count_excellent_pairs([1, 2, 3, 1], 3))
