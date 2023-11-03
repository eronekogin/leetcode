"""
https://leetcode.com/problems/maximize-the-confusion-of-an-exam/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def max_consecutive_answers(self, answer_key: str, k: int) -> int:
        """
        max_consecutive_answers
        """
        cnt = Counter()
        curr_max_freq = 0
        start = 0
        for end, c in enumerate(answer_key):
            cnt[answer_key[end]] += 1
            curr_max_freq = max(curr_max_freq, cnt[c])

            if end - start + 1 > curr_max_freq + k:  # not enough action.
                cnt[answer_key[start]] -= 1
                start += 1

        return len(answer_key) - start
