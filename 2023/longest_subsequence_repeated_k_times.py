"""
https://leetcode.com/problems/longest-subsequence-repeated-k-times/
"""


from collections import Counter, deque


class Solution:
    """
    Solution
    """

    def longest_subsequence_repeated_k(self, s: str, k: int) -> str:
        """
        longest_subsequence_repeated_k
        """
        def is_sub_sequence(s: str, t: str):
            it = iter(t)
            return all(c in it for c in s)

        cnt = Counter(s)
        words = [w for w, v in cnt.items() if v >= k]
        words.sort()

        queue = deque([''])
        rslt = ''
        while queue:
            for _ in range(len(queue)):
                curr_word = queue.popleft()
                rslt = curr_word
                for w in words:
                    next_word = curr_word + w
                    if is_sub_sequence(next_word * k, s):
                        queue.append(next_word)

        return rslt
