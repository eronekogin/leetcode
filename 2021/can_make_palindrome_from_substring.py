"""
https://leetcode.com/problems/can-make-palindrome-from-substring/
"""


class Solution:
    def canMakePaliQueries(self, s: str, queries: list[list[int]]) -> list[bool]:
        def check_query(query: list[int]) -> bool:
            left, right, k = query
            L, R = dp[left], dp[right + 1]

            # Get the total number of chars which are odd numbers. then check
            # if replacing half of them takes less or equal than k steps.
            cnt = 0
            for i in range(26):
                cnt += (R[i] - L[i]) & 1

            return (cnt >> 1) <= k

        N, BASE = len(s), ord('a')
        dp = [[0] * 26]

        # Calculate dp which contains char counter for each position in s.
        for i in range(1, N + 1):
            newDP = dp[-1][:]
            newDP[ord(s[i - 1]) - BASE] += 1
            dp.append(newDP)

        # Calculate result.
        return list(map(check_query, queries))

    def canMakePaliQueries2(self, s: str, queries: list[list[int]]) -> list[bool]:
        """
        For memory efficency, we could store each 26 bytes array as 26 bits
        binary string, then perform xor on each other to get the odd numbers
        """
        def check_query(query: list[int]) -> bool:
            left, right, k = query
            # int.bit_count() is only available in python 3.10 or later
            # cnt = (dp[right] ^ dp[left]).bit_count()
            return (bin(dp[left] ^ dp[right + 1]).count('1') >> 1) <= k

        N, BASE = len(s), ord('a')
        charIndexes = [ord(c) - BASE for c in s]

        # Calculate dp.
        dp = [0] * (N + 1)
        for i in range(1, N + 1):
            dp[i] = dp[i - 1] ^ (1 << charIndexes[i - 1])

        # Calculate result.
        return list(map(check_query, queries))


print(Solution().canMakePaliQueries('abcda', [[1, 2, 0]]))
