"""
https://leetcode.com/problems/apply-operations-to-maximize-score/description/
"""

MOD = 10 ** 9 + 7
SIZE = 10 ** 5 + 1
PRIMES: list[int] = []
is_prime = [True] * SIZE

for y in range(2, SIZE):
    if not is_prime[y]:
        continue

    PRIMES.append(y)

    for z in range(y, SIZE, y):
        is_prime[z] = False


class Solution:
    """
    Solution
    """

    def maximum_score(self, nums: list[int], k: int) -> int:
        """
        maximum score
        """
        n = len(nums)
        scores = [0] * n

        for i, x in enumerate(nums):
            for p in PRIMES:
                if p * p > x:
                    break

                if x % p != 0:
                    continue

                scores[i] += 1
                while x % p == 0:
                    x //= p

            if x > 1:
                scores[i] += 1

        left, right = [-1] * n, [n] * n
        stack: list[int] = []

        for i, x in enumerate(nums):
            while (
                stack and
                scores[stack[-1]] < scores[i]
            ):
                right[stack.pop()] = i

            if stack:
                left[i] = stack[-1]

            stack.append(i)

        subarrays = [(right[i] - i) * (i - left[i]) for i in range(n)]
        sorted_nums = sorted(enumerate(nums), key=lambda x: -x[1])

        score = 1
        j = 0
        while k > 0:
            i, x = sorted_nums[j]
            j += 1

            operations = min(k, subarrays[i])

            score = (score * pow(x, operations, MOD)) % MOD

            k -= operations

        return score
