"""
https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/description/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def longest_palindrome(self, words: list[str]) -> int:
        """
        longest_palindrome
        """
        cnt = Counter(words)
        rslt = 0
        visited = set()
        has_remain_self_symmetrical_words = False

        for w in words:
            if w in visited:
                continue

            rw = w[::-1]

            if rw not in cnt:
                continue

            if w[0] != w[1]:  # Not self symmetrical, such as lc
                rslt += min(cnt[w], cnt[rw]) * 2 * 2
                visited.add(rw)
            else:  # Self symmerical, such as gg
                if cnt[w] & 1:
                    has_remain_self_symmetrical_words = True

                rslt += (cnt[w] - (cnt[w] & 1)) * 2

            visited.add(w)

        return rslt + has_remain_self_symmetrical_words * 2


print(Solution().longest_palindrome(["lc", "cl", "gg"]))
