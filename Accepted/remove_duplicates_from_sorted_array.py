"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""


class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> 'int':
        if not nums:  # list is empty.
            return 0

        chkIdx = 0

        for num in nums:
            if num != nums[chkIdx]:
                chkIdx += 1
                nums[chkIdx] = num

        return chkIdx + 1


nums = [1, 1, 2]
print(Solution().removeDuplicates(nums))
print(nums)
