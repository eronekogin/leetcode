"""
https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/description/
"""


class Solution:
    """
    Solution
    """

    def min_max_difference(self, num: int) -> int:
        """
        min max difference
        """
        def replace(chars: list[str], d: str):
            origin = '10'
            for i, c in enumerate(chars):
                if len(origin) == 2 and c != d:
                    origin = c

                if c == origin:
                    chars[i] = d

            return int(''.join(chars))

        s = str(num)
        return replace(list(s), '9') - replace(list(s), '0')
