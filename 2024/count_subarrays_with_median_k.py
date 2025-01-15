"""
https://leetcode.com/problems/count-subarrays-with-median-k/description/
"""


class Solution:
    """
    Solution
    """

    def count_subarrays(self, nums: list[int], k: int) -> int:
        """
        for any candidate subarray, the numbers greater than k must
        be equal or one more than the numbers less than k.
        """
        memo: dict[int, int] = {}
        pivot = nums.index(k)

        # Check numbers after k.
        balance = 0
        for i in range(pivot, len(nums)):
            if nums[i] > k:
                balance += 1
            elif nums[i] < k:
                balance -= 1

            memo[balance] = memo.get(balance, 0) + 1

        # Then check numbers before k and find the complimentory balance.
        balance = 0
        cnt = 0
        for i in range(pivot, -1, -1):
            if nums[i] > k:
                balance += 1
            elif nums[i] < k:
                balance -= 1

            cnt += memo.get(-balance, 0) + memo.get(-balance + 1, 0)

        return cnt
