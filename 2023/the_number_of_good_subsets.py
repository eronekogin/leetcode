"""
https://leetcode.com/problems/the-number-of-good-subsets/
"""


from collections import Counter


class Solution:
    def numberOfGoodSubsets(self, nums: list[int]) -> int:
        MOD = 10 ** 9 + 7
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]  # Primes less than 30.
        N = len(primes)
        dp = [1] + [0] * (1 << N)
        cnt = Counter(nums)

        for num in cnt:
            # 1 is not a prime.
            # for 4, 9, and 25, it will cause duplicate prime factor.
            if num == 1 or num % 4 == 0 or num % 9 == 0 or num % 25 == 0:
                continue
            
            mask = sum(1 << i for i, p in enumerate(primes) if num % p == 0)

            for i in range(1 << N):
                if i & mask > 0:  # The combination is already used.
                    continue

                # Calculate the number of new combinations.
                dp[i | mask] = (dp[i | mask] + cnt[num] * dp[i]) % MOD
        
        # We can append any number of 1 to the existing combinations.
        # And we should also eliminate the empty set as it is not a good one.
        return ((1 << cnt[1]) * (sum(dp) - 1)) % MOD

        
