"""
https://leetcode.com/problems/reward-top-k-students/description/
"""


class Solution:
    """
    Solution
    """

    def top_students(
        self,
        positive_feedback: list[str],
        negative_feedback: list[str],
        report: list[str],
        student_id: list[int],
        k: int
    ) -> list[int]:
        """
        top students
        """
        memo: dict[int, int] = {}
        pos_set = set(positive_feedback)
        neg_set = set(negative_feedback)
        for i, s in zip(student_id, report):
            score = 0
            for w in s.split():
                if w in pos_set:
                    score += 3

                if w in neg_set:
                    score -= 1

            memo[i] = memo.get(i, 0) + score

        return [
            i
            for i, _ in sorted(
                memo.items(),
                key=lambda x: (-x[1], x[0])
            )[:k]
        ]
