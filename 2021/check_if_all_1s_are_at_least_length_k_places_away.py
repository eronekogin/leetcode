"""
https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/
"""


from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        start = None
        for end in range(len(nums)):
            if nums[end]:
                if start is not None and end - start - 1 < k:
                    return False

                start = end

        return True
