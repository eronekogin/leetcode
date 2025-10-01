"""
https://leetcode.com/problems/count-complete-subarrays-in-an-array/description/
"""


class Solution:
    """
    Solution
    """

    def count_complete_subarrays(self, nums: list[int]) -> int:
        """
        count complete subarrays
        """
        cnt = 0
        target = len(set(nums))
        n = len(nums)
        curr_window = {}
        end = 0

        for start in range(n):
            if start > 0:
                remove = nums[start - 1]
                curr_window[remove] -= 1
                if curr_window[remove] == 0:
                    del curr_window[remove]

            while end < n and len(curr_window) < target:
                add = nums[end]
                curr_window[add] = curr_window.get(add, 0) + 1
                end += 1

            if len(curr_window) == target:
                cnt += 1 + n - end
            else:
                break

        return cnt


print(Solution().count_complete_subarrays([1, 3, 1, 2, 2]))
