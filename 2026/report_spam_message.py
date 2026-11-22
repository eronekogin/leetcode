"""
https://leetcode.com/problems/report-spam-message/description/
"""


class Solution:
    """
    Solution
    """

    def report_spam(self, message: list[str], banned_words: list[str]) -> bool:
        """
        report spam
        """
        banned = set(banned_words)
        cnt = 0
        for w in message:
            if w in banned:
                cnt += 1
                if cnt >= 2:
                    return True

        return False
