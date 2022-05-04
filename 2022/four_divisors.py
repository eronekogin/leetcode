"""
https://leetcode.com/problems/four-divisors/
"""


class Solution:
    def sumFourDivisors(self, nums: list[int]) -> int:
        def sum_divisors(x: int) -> int:
            divisors = {1, x}
            for i in range(2, int(x ** 0.5) + 1):
                q, r = divmod(x, i)
                if r == 0:
                    divisors.add(i)
                    divisors.add(q)

                if len(divisors) > 4:
                    return 0

            if len(divisors) < 4:
                return 0

            return sum(divisors)

        return sum(map(sum_divisors, nums))


print(Solution().sumFourDivisors([21, 4, 7]))
