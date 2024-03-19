"""
https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/description/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def most_frequent(self, nums: list[int], key: int) -> int:
        """
        most_frequent
        """
        cnt: Counter[int] = Counter()
        n = len(nums)
        for i, x in enumerate(nums):
            if i < n - 1 and x == key:
                cnt[nums[i + 1]] += 1

        return cnt.most_common(1)[0][0]
