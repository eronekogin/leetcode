"""
https://leetcode.com/problems/number-of-unique-good-subsequences/
"""


class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        """
        Consider two kinds of subsequence, one is ended with zero and the other is ended with one, then we have:

            1. When come across a new zero, we can create new sub sequence ends with zero by appending the zero to
                all the previous sub sequence.
            
            2. When come across a new one, we can create new sub sequence ends with one by appending the one to
                all the previous sub sequence, plus one itself. This is because after appending the one to the
                previous sequence, the original single one sequence become 11 now.
            
            3. After processing all the chars, we should also check if 0 is inside the binary string as a single
                zero is allowed to be a good sub sequence.
        """
        MOD = 10 ** 9 + 7
        dp = [0, 0]  # the first is all subsequence ends with zero and the second is ends with one.
        for c in binary:
            dp[int(c)] = (sum(dp) + int(c)) % MOD
        
        return (sum(dp) + ('0' in binary)) % MOD