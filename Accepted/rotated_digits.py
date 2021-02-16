"""
https://leetcode.com/problems/rotated-digits/
"""


class Solution:
    def rotatedDigits(self, N: int) -> int:
        """
        For each number from 1 to N, split it into two numbers by its last
        digit, then:
        1. If dp[first] == dp[last] == 1: dp[i] = 1
        2. If dp[first] == 2 and dp[last] > 0 or    
            dp[first] > 0 and dp[last] == 2: dp[i] = 2
        3. Else: dp[i] = 0

        For the above dp list, 0 means not rotatable, 1 means same digits after
        rotation and 2 means different digits after rotation.
        """
        memo = [0] * (N + 1)
        SAME_DIGITS, DIFF_DIGITS = {0, 1, 8}, {2, 5, 6, 9}
        cnt = 0
        for i in range(N + 1):
            if i < 10:
                if i in SAME_DIGITS:
                    memo[i] = 1
                elif i in DIFF_DIGITS:
                    memo[i] = 2
                    cnt += 1
            else:
                curr, pre = memo[i // 10], memo[i % 10]
                if curr == pre == 1:  # Still same number.
                    memo[i] = 1
                elif curr >= 1 and pre >= 1:  # 2, 1 or 1, 2
                    memo[i] = 2
                    cnt += 1

        return cnt


print(Solution().rotatedDigits(857))
