"""
https://leetcode.com/problems/3sum/
"""


class Solution:
    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
        total, rslt = len(nums), []
        nums.sort()  # Sort the array first in order to apply binary search.

        for i in range(total):
            if i > 0 and nums[i] == nums[i - 1]:
                """
                If it is not the first element and the current element 
                is the same as the previous one, skip the current element.
                """
                continue

            l = i + 1
            r = total - 1

            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    rslt.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # Skip the element having the same value as the current.
                    while l < r and nums[l] == nums[l - 1] \
                            and nums[r] == nums[r + 1]:
                        l += 1
                        r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1

        return rslt
