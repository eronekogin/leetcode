"""
https://leetcode.com/problems/maximum-split-of-positive-even-integers/description/
"""


class Solution:
    """
    Solution
    """

    def maximum_even_split(self, final_sum: int) -> list[int]:
        """
        maximum even split
        """
        if final_sum & 1 > 0:
            return []

        rslt: list[int] = []
        remain_sum = final_sum
        curr_num = 2
        while remain_sum >= curr_num + curr_num + 2:
            rslt.append(curr_num)
            remain_sum -= curr_num
            curr_num += 2

        return rslt + [remain_sum]


print(Solution().maximum_even_split(12))
