"""
https://leetcode.com/problems/continuous-subarrays/description/
"""


class Solution:
    """
    Solution
    """

    def continuous_subarrays(self, nums: list[int]) -> int:
        """
        continuous subarrays
        """
        l = r = 0
        curr_window = total = 0
        curr_min = curr_max = nums[0]

        for r, x in enumerate(nums):
            curr_min = min(curr_min, x)
            curr_max = max(curr_max, x)

            if curr_max - curr_min > 2:
                curr_window = r - l
                total += curr_window * (1 + curr_window) // 2

                l = r
                curr_min = curr_max = x

                # Expand the current window to the left
                # and subtract duplicate subarrays
                while l > 0 and abs(x - nums[l - 1]) <= 2:
                    l -= 1
                    curr_min = min(curr_min, nums[l])
                    curr_max = max(curr_max, nums[l])

                if l < r:
                    curr_window = r - l
                    total -= curr_window * (1 + curr_window) // 2

        # Calculate final window
        curr_window = r - l + 1
        total += curr_window * (1 + curr_window) // 2

        return total
