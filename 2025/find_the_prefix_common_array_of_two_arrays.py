"""
https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/description/
"""


class Solution:
    """
    Solution
    """

    def find_the_prefix_common_array(self, a: list[int], b: list[int]) -> list[int]:
        """
        find the prefix common array
        """
        n = len(a)
        cnt = [0] * (n + 1)
        rslt: list[int] = []
        common_nums = 0
        for x, y in zip(a, b):
            cnt[x] += 1
            if cnt[x] == 2:
                common_nums += 1

            cnt[y] += 1
            if cnt[y] == 2:
                common_nums += 1

            rslt.append(common_nums)

        return rslt
