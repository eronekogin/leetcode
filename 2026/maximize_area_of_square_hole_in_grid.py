"""
https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/description/
"""


class Solution:
    """
    Docstring for Solution
    """

    def maximize_square_hole_area(self, n: int, m: int, h_bars: list[int], v_bars: list[int]) -> int:
        """
        Docstring for maximize_square_hole_area

        :param self: Description
        :param n: Description
        :type n: int
        :param m: Description
        :type m: int
        :param h_bars: Description
        :type h_bars: list[int]
        :param v_bars: Description
        :type v_bars: list[int]
        :return: Description
        :rtype: int
        """
        def get_consecutive_bars(bars: list[int]) -> int:
            max_bars = curr_bars = 1

            for i in range(1, len(bars)):
                if bars[i] == bars[i - 1] + 1:
                    curr_bars += 1
                else:
                    curr_bars = 1

                max_bars = max(max_bars, curr_bars)

            return max_bars

        max_h = get_consecutive_bars(sorted(h_bars))
        max_v = get_consecutive_bars(sorted(v_bars))
        side = min(max_h, max_v) + 1

        return side * side
