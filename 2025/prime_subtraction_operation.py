"""
https://leetcode.com/problems/prime-subtraction-operation/description/
"""


SIEVE = [1] * 1001
SIEVE[1] = 0
for i in range(2, int(1001 ** 0.5) + 1):
    if SIEVE[i]:
        for j in range(i * i, 1001, i):
            SIEVE[j] = 0


class Solution:
    """
    Solution
    """

    def prime_sub_operation(self, nums: list[int]) -> bool:
        """
        prime sub operation
        """
        curr_val = 1
        curr_index = 0
        while curr_index < len(nums):
            diff = nums[curr_index] - curr_val

            if diff < 0:
                return False

            if SIEVE[diff] or diff == 0:
                curr_index += 1

            curr_val += 1

        return True
