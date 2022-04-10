"""
https://leetcode.com/problems/summary-ranges/
"""


from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        """
        Presumption: Input list is in ascending order.
        """
        if not nums:  # Input list is empty.
            return []

        start = end = nums[0]
        rslt = []
        # Make sure the last element in nums is processed.
        for num in nums[1:] + [nums[-1] + 2]:
            if num - end > 1:  # Found a new start:
                if end > start:
                    rslt.append('{0}->{1}'.format(start, end))
                else:
                    rslt.append(str(start))

                start = num

            end = num

        return rslt


nums = [-1]
print(Solution().summaryRanges(nums))
