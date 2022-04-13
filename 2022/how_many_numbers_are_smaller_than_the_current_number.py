"""
https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
"""


from collections import Counter


class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        cnt = Counter(nums)
        lessNumsCnt = Counter()
        total = sum(cnt.values())
        for num in sorted(cnt.keys(), reverse=True):
            total -= cnt[num]
            lessNumsCnt[num] = total

        return [lessNumsCnt[num] for num in nums]
