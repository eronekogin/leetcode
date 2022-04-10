"""
https://leetcode.com/problems/additive-number/
"""


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        """
        Python does not have integer overflow, in case we need
        to handle overflow on very big integers in other languages,
        we could use string add instead.
        """
        n = len(num)
        for i in range(1, (n - 1) // 2 + 1):
            if num[0] == '0' and i > 1:  # The first number has leading zero.
                break

            j = i + 1
            while n - j >= max(j - i, i):
                # The second number has leading zero.
                if num[i] == '0' and j - i > 1:
                    break

                k, a, b = j, num[:i], num[i:j]
                while k < n:
                    c = str(int(a) + int(b))
                    if not num.startswith(c, k):
                        break  # No additive number in this path.

                    k += len(c)
                    a, b = b, c

                if k == n:
                    return True

                j += 1  # Check the next combination.

        return False


print(Solution().isAdditiveNumber("199001200"))
