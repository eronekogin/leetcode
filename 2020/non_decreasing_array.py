"""
https://leetcode.com/problems/non-decreasing-array/
"""


from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        """
        Consider all the pairs nums[i] > nums[i + 1], which prevents the given
        list to become non-decreasing. Then we have the following cases:
            1. There is zero pair: No need to modify anything.
            2. There is 2 or more pairs: Too many modifications needed.
            3. i = 0: Simply set nums[0] = nums[1]
            4. i = n - 2: Simply set nums[n - 1] = nums[n - 2].
            5. If nums[i - 1] < nums[i] > nums[i + 1] < nums[i + 2]:
                5.1 If nums[i - 1] <= nums[i + 1], set nums[i] in between.
                5.2 If nums[i] <= nums[i + 2], set nums[i + 1] in between.
                5.3 Otherwise, too many modifications needed.
        """
        t, n = None, len(nums)
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                if t is not None:  # More than 1 pair.
                    return False

                t = i

        return t is None or t == 0 or t == n - 2 or nums[t - 1] <= nums[t + 1] \
            or nums[t] <= nums[t + 2]


print(Solution().checkPossibility([4, 2, 3]))
