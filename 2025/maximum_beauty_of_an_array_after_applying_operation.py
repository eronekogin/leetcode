"""
https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/description/
"""


class Solution:
    """
    Solution
    """

    def maximum_beauty(self, nums: list[int], k: int) -> int:
        """
        maximum beauty
        """
        if len(nums) == 1:
            return 1

        max_value = max(nums)
        cnt = [0] * (max_value + 1)

        for x in nums:
            cnt[max(0, x - k)] += 1
            if x + k + 1 <= max_value:
                cnt[x + k + 1] -= 1

        rslt = 0
        curr_sum = 0
        for x in cnt:
            curr_sum += x
            rslt = max(rslt, curr_sum)

        return rslt
