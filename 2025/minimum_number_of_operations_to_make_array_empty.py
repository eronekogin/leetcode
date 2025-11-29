"""
https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/description/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def min_operations(self, nums: list[int]) -> int:
        """
        the remainder of 3 can be 0, 1, 2:

        case 0: it's already minimum ops total // 3
        case 1: it's (total // 3) - 1 + 4 // 2 = (total // 3) + 1
        case 2: it's (total // 3) + 2 // 2 = (total // 3) + 1

        In summary, it will be ceil(total / 3)
        """
        cnt = Counter(nums)
        rslt = 0
        for v in cnt.values():
            if v == 1:
                return -1

            q, r = divmod(v, 3)
            rslt += q + (r > 0)

        return rslt


print(Solution().min_operations(
    [14, 12, 14, 14, 12, 14, 14, 12, 12, 12, 12, 14, 14, 12, 14, 14, 14, 12, 12]))
