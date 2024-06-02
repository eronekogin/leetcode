"""
https://leetcode.com/problems/total-appeal-of-a-string/description/
"""


from collections import defaultdict


class Solution:
    """
    Solution
    """

    def appeal_sum(self, s: str) -> int:
        """
        for any substring end at index j, suppose we have xxxaxxb,
        suppose a is at index i, then we have xxxaxxb, xxaxxb, xaxxb, axxb
        substrings that having char a, in total it is i + 1. Then we do it
        for every char in the sub string.
        """
        last = {}
        cnt = 0
        for i, c in enumerate(s):
            last[c] = i + 1
            cnt += sum(last.values())

        return cnt

    def appeal_sum2(self, s: str) -> int:
        """
        consider each char in a substring, suppose the char start at index i,
        then any duplicate char after index i will not count in the final
        score. And in order for the char at index i to score, the substring
        must start after the previous occurrence index of char s[i], otherwise
        the previous one will count.

        So for start position, we have i - prev[s[i]] choices, and for end
        position of the substring we have n - i choices. In total, they
        contribute a score of (i - prev[s[i]] * (n - i))
        """
        prevs: defaultdict[str, int] = defaultdict(lambda: -1)
        cnt = 0
        n = len(s)
        for i, c in enumerate(s):
            cnt += (i - prevs[c]) * (n - i)
            prevs[c] = i

        return cnt


print(Solution().appeal_sum('code'))
