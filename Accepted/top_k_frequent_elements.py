"""
https://leetcode.com/problems/top-k-frequent-elements/
"""


from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Cheating.
        """
        return [x for x, _ in Counter(nums).most_common(k)]

    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        """
        Use bucket sort to filter out the top k frequent numbers.
        """
        memo = {}
        for num in nums:  # Generate memo.
            memo[num] = memo.get(num, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in memo.items():  # Build buckets.
            buckets[freq].append(num)

        rslt = []
        for bucket in reversed(buckets):  # Scan buckets to get results.
            rslt += bucket
            if len(rslt) >= k:
                return rslt[:k]
