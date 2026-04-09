"""
https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/description/
"""


class Solution:
    """
    Solution
    """

    def minimum_pushes(self, word: str) -> int:
        """
        minimum pushes
        """
        cnt: dict[str, int] = {}
        for c in word:
            cnt[c] = cnt.get(c, 0) + 1

        freqs = sorted(cnt.values())
        rslt = 0
        for i in range(1, 5):
            if not freqs:
                break

            for _ in range(8):
                if not freqs:
                    break

                rslt += freqs.pop() * i

        return rslt


print(Solution().minimum_pushes('amrvxnhsewkoipjyuclgtdbfq'))
