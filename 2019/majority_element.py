"""
https://leetcode.com/problems/majority-element/
"""


from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Two cases:  (Pipes are inserted where count == 0)

            [7, 7, 5, 7, 5, 1 | 5, 7 | 5, 5, 7, 7 | 7, 7, 7, 7]
            [7, 7, 5, 7, 5, 1 | 5, 7 | 5, 5, 7, 7 | 5, 5, 5, 5]

        Eventually we will get the majority element.
        """
        count, candidate = 0, None
        for num in nums:
            if not count:
                candidate = num

            count += 1 if num == candidate else -1

        return candidate
