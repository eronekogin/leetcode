"""
https://leetcode.com/problems/sender-with-largest-word-count/description/
"""


class Solution:
    """
    Solution
    """

    def largest_word_count(self, messages: list[str], senders: list[str]) -> str:
        """
        largest word count
        """
        memo: dict[str, int] = {}
        for s, m in zip(senders, messages):
            memo[s] = memo.get(s, 0) + len(m.split())

        max_cnt = max(memo.values())
        return sorted(k for k, v in memo.items() if v == max_cnt)[-1]
