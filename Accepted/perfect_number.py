"""
https://leetcode.com/problems/perfect-number/
"""


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False

        i, total = 2, 1
        while i * i < num:
            q, r = divmod(num, i)
            if r == 0:
                total += i + q

            i += 1

        if i * i == num:  # When num**0.5 is a divisor.
            total += i

        return total == num


print(Solution().checkPerfectNumber(28))
