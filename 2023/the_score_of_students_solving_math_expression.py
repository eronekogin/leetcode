"""
https://leetcode.com/problems/the-score-of-students-solving-math-expression/
"""


from functools import cache


class Solution:
    """
    Solution
    """

    def score_of_students(self, s: str, answers: list[int]) -> int:
        """
        score_of_students
        """
        @cache
        def dp(start: int, end: int):
            if start == end:
                return {int(s[start]): 5}

            rslt = {}
            for m in range(start + 1, end, 2):
                for a in dp(start, m - 1):
                    for b in dp(m + 1, end):
                        curr = a * b if s[m] == '*' else a + b
                        if curr <= 1000:
                            # Answer is limited to be no more than 1000.
                            rslt[curr] = 2

            return rslt

        rslt = {**dp(0, len(s) - 1), **{eval(s): 5}}
        return sum(rslt.get(a, 0) for a in answers)
