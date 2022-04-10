"""
https://leetcode.com/problems/generate-parentheses/
"""


class Solution:
    def generateParenthesis(self, n: 'int') -> 'List[str]':
        if n <= 0:
            return []

        dp = {1: {'()'}, 2: {'(())', '()()'}}  # Initialize dp[1], dp[2].

        for i in range(3, n + 1):
            # Pattern 1: dp[i] = '(' + x + ')', where x is element of dp[i-1].
            dp[i] = set(['(' + x + ')' for x in dp.get(i - 1, [])])

            # Pattern 2: dp[i] = dp[j] + dp[i - j] as total length for dp[i]
            # is i.
            for j in range(1, i):
                dp[i] = dp[i].union([x + y for x in dp[j] for y in dp[i - j]])

        return list(dp[n])


print(Solution().generateParenthesis(3))
