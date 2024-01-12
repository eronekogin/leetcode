"""
https://leetcode.com/problems/sum-of-subarray-ranges/description
"""


import operator


class Solution:
    """
    Solution
    """

    def sub_array_ranges(self, nums: list[int]) -> int:
        """
        sub_array_ranges
        """
        def count(op):
            total_sum = 0
            stack: list[int] = []
            n = len(nums)

            for i in range(n + 1):
                while stack and (i == n or op(nums[i], nums[stack[-1]])):
                    # op could be lt or gt, when it is gt, it means nums[stack[-1]] is the minimum
                    # number in the subarrays from left boundary to stack[-1], and in the subarrays
                    # from stack[-1] to right boundary.

                    # Here left boundary will be stack[-1] or -1 if stack is empty, and right
                    # boundary will be the current index i.
                    m = stack.pop()
                    right_boundary = i
                    left_boundary = stack[-1] if stack else -1

                    total_sum += (
                        nums[m] *
                        (m - left_boundary) *
                        (right_boundary - m)
                    )

                stack.append(i)

            return total_sum

        return count(operator.gt) - count(operator.lt)
