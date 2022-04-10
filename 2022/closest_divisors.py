"""
https://leetcode.com/problems/closest-divisors/
"""


class Solution:
    def closestDivisors(self, num: int) -> list[int]:
        t1, t2 = num + 1, num + 2
        for a in range(int(t2 ** 0.5), 0, -1):
            if t1 % a == 0:
                return [a, t1 // a]

            if t2 % a == 0:
                return [a, t2 // a]


print(Solution().closestDivisors(1))
