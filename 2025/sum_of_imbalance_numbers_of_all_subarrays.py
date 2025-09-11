"""
https://leetcode.com/problems/sum-of-imbalance-numbers-of-all-subarrays/description/
"""


class Solution:
    """
    Solution
    """

    def sum_imbalance_numbers(self, nums: list[int]) -> int:
        """
        sum imbalance numbers
        """
        n = len(nums)
        cnt = 0

        for start in range(n - 1):
            seen: set[int] = set()
            curr = -1

            for end in range(start, n):
                if nums[end] not in seen:
                    curr += (
                        1 -
                        (nums[end] + 1 in seen) -
                        (nums[end] - 1 in seen)
                    )

                seen.add(nums[end])
                cnt += curr

        return cnt
