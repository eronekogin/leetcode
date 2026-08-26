"""
https://leetcode.com/problems/maximum-height-of-a-triangle/description/
"""


class Solution:
    """
    Solution
    """

    def max_height_of_triangle(self, red: int, blue: int) -> int:
        """
        max height of triangle
        """
        def calc(start_with_red: bool, red: int, blue: int) -> int:
            h = 0
            while True:
                if start_with_red:
                    if red >= h + 1:
                        red -= h + 1
                        h += 1
                    else:
                        return h
                else:
                    if blue >= h + 1:
                        blue -= h + 1
                        h += 1
                    else:
                        return h

                start_with_red = not start_with_red

        return max(calc(True, red, blue), calc(False, red, blue))


print(Solution().max_height_of_triangle(2, 4))
