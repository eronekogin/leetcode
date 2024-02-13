"""
https://leetcode.com/problems/count-the-hidden-sequences/description/
"""


from itertools import accumulate


class Solution:
    """
    Solution
    """

    def number_of_arrays(self, differences: list[int], lower: int, upper: int) -> int:
        """
        number of arrays
        """
        prefix_sum = [0] + list(accumulate(differences))
        x = lower
        max_num, min_num = lower - 1, upper + 1
        for num in prefix_sum:
            original_num = x + num
            max_num = max(max_num, original_num)
            min_num = min(min_num, original_num)

        return max(0, upper - lower + 1 - (max_num - min_num))


print(Solution().number_of_arrays([1, -3, 4], 1, 6))
