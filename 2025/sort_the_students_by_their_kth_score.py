"""
https://leetcode.com/problems/sort-the-students-by-their-kth-score/description/
"""


class Solution:
    """
    Solution
    """

    def sort_the_students(self, score: list[list[int]], k: int):
        """
        sort the students
        """
        score.sort(key=lambda x: -x[k])
        return score
