"""
https://leetcode.com/problems/find-the-original-array-of-prefix-xor/description/
"""


class Solution:
    """
    Solution
    """

    def find_array(self, pref: list[int]) -> list[int]:
        """
        find array
        """
        rslt = [pref[0]]
        for i in range(len(pref) - 1):
            rslt.append(pref[i] ^ pref[i + 1])

        return rslt
