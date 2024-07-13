"""
https://leetcode.com/problems/naming-a-company/description/
"""


class Solution:
    """
    Solution
    """

    def distinct_names(self, ideas: list[str]) -> int:
        """
        distinct names
        """
        cnt, offset = 0, ord('a')
        memo = [set() for _ in range(26)]

        for w in ideas:
            memo[ord(w[0]) - offset].add(w[1:])

        for i in range(25):
            for j in range(i + 1, 26):
                dups = len(memo[i] & memo[j])

                cnt += (len(memo[i]) - dups) * (len(memo[j]) - dups)

        return cnt << 1


print(Solution().distinct_names(["coffee", "donuts", "time", "toffee"]))
