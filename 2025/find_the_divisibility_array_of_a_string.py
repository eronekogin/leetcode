"""
https://leetcode.com/problems/find-the-divisibility-array-of-a-string/description/
"""


class Solution:
    """
    Solution
    """

    def divisibility_array(self, word: str, m: int) -> list[int]:
        """
        divisibility array
        """
        curr_num = 0
        rslt: list[int] = [0] * len(word)
        for i, x in enumerate(map(int, word)):
            curr_num = (curr_num * 10 + x) % m
            if not curr_num:
                rslt[i] = 1

        return rslt
