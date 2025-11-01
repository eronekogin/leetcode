"""
https://leetcode.com/problems/maximum-sum-of-almost-unique-subarray/description/
"""


class Solution:
    """
    Solution
    """

    def max_sum(self, nums: list[int], m: int, k: int) -> int:
        """
        max sum
        """
        rslt = 0
        curr_sum = 0
        distinct_nums: dict[int, int] = {}

        for i, x in enumerate(nums):
            if i >= k:
                if len(distinct_nums) >= m:
                    rslt = max(rslt, curr_sum)

                to_delete = nums[i - k]
                curr_sum -= to_delete
                distinct_nums[to_delete] -= 1
                if distinct_nums[to_delete] == 0:
                    del distinct_nums[to_delete]

            curr_sum += x
            distinct_nums[x] = distinct_nums.get(x, 0) + 1

        if len(distinct_nums) >= m:
            return max(rslt, curr_sum)

        return rslt


print(Solution().max_sum([1, 2, 2], 2, 2))
