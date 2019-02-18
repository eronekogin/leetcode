"""
https://leetcode.com/problems/4sum/
"""


class Solution:
    def fourSum(self, nums: 'List[int]', target: 'int') -> 'List[List[int]]':
        total, rslt = len(nums), []
        nums.sort()

        for i in range(total):
            if i > 0 and nums[i] == nums[i - 1]:
                # Not the first and having the same value as the previous.
                continue

            newTarget = target - nums[i]

            # Convert four_sum to three_sum.
            for j in range(i + 1, total):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                l, r, chkNum = j + 1, total - 1, newTarget - nums[j]

                while l < r:
                    tempSum = nums[l] + nums[r]
                    if tempSum == chkNum:  # Found.
                        rslt.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1

                        # Skip the next element having the same value.
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    elif tempSum < chkNum:
                        l += 1  # Sum is too small, enlarge it.
                    else:
                        r -= 1  # Sum is too big, reduce it.

        return rslt
