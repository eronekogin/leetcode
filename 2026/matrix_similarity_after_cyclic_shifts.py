"""
https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/description/
"""


class Solution:
    """
    Docstring for Solution
    """

    def are_similar(self, mat: list[list[int]], k: int) -> bool:
        """
        Docstring for are_similar

        :param self: Description
        :param mat: Description
        :type mat: list[list[int]]
        :param k: Description
        :type k: int
        :return: Description
        :rtype: bool
        """
        n = len(mat[0])
        for i, row in enumerate(mat):
            r = k % n
            if r == 0:
                continue

            new_row = row + row

            if i & 1:
                new_row = new_row[r: r + n]
            else:
                new_row = new_row[-r - n: -r]

            if new_row != row:
                return False

        return True


print(Solution().are_similar([[7, 7], [10, 10], [4, 4]], 2))
