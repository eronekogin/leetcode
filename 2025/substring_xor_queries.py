"""
https://leetcode.com/problems/substring-xor-queries/description/
"""


from collections import defaultdict


class Solution:
    """
    Solution
    """

    def substring_xor_queries(self, s: str, queries: list[list[int]]) -> list[list[int]]:
        """
        substring xor queries
        """
        memo = defaultdict(lambda: [-1, -1])

        # Processing all substrings having length from 1 to 32.
        for curr_len in range(33, 0, -1):
            for i in range(len(s) - curr_len, -1, -1):
                memo[int(s[i: i + curr_len], 2)] = [i, i + curr_len - 1]

        return [memo[y ^ x] for x, y in queries]
