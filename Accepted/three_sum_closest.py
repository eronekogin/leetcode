"""
https://leetcode.com/problems/3sum-closest/
"""


class Solution:
    def threeSumClosest(self, nums: 'List[int]', target: 'int') -> 'int':
        total, rslt = len(nums), None
        nums.sort()  # Sort first to imporve search efficency.

        for i in range(total):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip the same element.

            l, r = i + 1, total - 1

            while l < r:
                tempSum = nums[i] + nums[l] + nums[r]

                if tempSum == target:
                    return target
                elif tempSum < target:
                    l += 1
                else:
                    r -= 1

                if rslt is None or abs(tempSum - target) < abs(rslt - target):
                    rslt = tempSum

        return rslt


print(Solution().threeSumClosest([0, 0, 0], 1))
