"""
https://leetcode.com/problems/sort-array-by-parity-ii/
"""


class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        iOdd = 1
        for iEven in range(0, len(nums), 2):
            if nums[iEven] & 1:
                while nums[iOdd] & 1:
                    iOdd += 2

                nums[iEven], nums[iOdd] = nums[iOdd], nums[iEven]

        return nums


print(Solution().sortArrayByParityII([2, 3, 1, 1, 4, 0, 0, 4, 3, 3]))
