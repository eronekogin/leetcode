"""
https://leetcode.com/problems/count-alternating-subarrays/description/
"""


class Solution:
    """
    Solution
    """

    def count_alternating_subarrays(self, nums: list[int]) -> int:
        """
        count alternating subarrays
        """
        start = 0
        cnt = 0
        end, n = 0, len(nums)
        while end < n:
            while end + 1 < n and nums[end + 1] != nums[end]:
                end += 1

            items = end - start + 1
            cnt += (1 + items) * items // 2
            end += 1
            start = end

        return cnt


print(Solution().count_alternating_subarrays([0, 1, 1, 1]))
