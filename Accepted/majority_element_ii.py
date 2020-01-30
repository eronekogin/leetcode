"""
https://leetcode.com/problems/majority-element-ii/
"""


from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """
        Still use the Boyer-Moore Majority vote algorithm:

        Try to find three different votes and hide them, repeat until there
        are not three different votes. In the end, a number that originally
        has more than 1/3 of the votes now still has at least one vote.
        """
        cnt = Counter()
        for num in nums:
            cnt[num] += 1
            if len(cnt) == 3:  # Found three different votes now.
                cnt -= Counter(set(cnt))

        chk = len(nums) // 3
        cnt = Counter([num for num in nums if num in cnt])
        return [num for num in cnt if cnt[num] > chk]

    def majority_k_element(self, nums: List[int], k: int) -> List[int]:
        """
        Generalized it to find the majority number who occurs more than 
        n // k times in nums.
        """
        cnt = Counter()
        for num in nums:
            cnt[num] += 1
            if len(cnt) == k:
                cnt -= Counter(set(cnt))

        chk = len(nums) // k
        cnt = Counter([num for num in nums if num in cnt])
        return [num for num in cnt if cnt[num] > chk]
